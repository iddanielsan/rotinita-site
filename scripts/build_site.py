#!/usr/bin/env python3
"""Package the static site for GitHub Pages, without repository documentation."""

import json
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
ROOT_FILES = {"CNAME", ".nojekyll", "robots.txt", "sitemap.xml", "site.webmanifest", "browserconfig.xml"}
ASSET_SUFFIXES = {".css", ".js", ".svg", ".png", ".jpg", ".webp", ".mp4", ".ico"}
ASSOCIATIONS = {"apple-app-site-association", "assetlinks.json"}


def public_files():
    for path in ROOT.iterdir():
        if path.is_file() and (path.name in ROOT_FILES or path.suffix in ASSET_SUFFIXES | {".html"}):
            yield path
    for directory in ("assets", "css", "js", "auth", ".well-known"):
        for path in (ROOT / directory).rglob("*"):
            if not path.is_file():
                continue
            if directory == ".well-known":
                if path.name in ASSOCIATIONS:
                    yield path
            elif path.suffix in ASSET_SUFFIXES | {".html"}:
                yield path


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = set()
        self.canonical = None
        self.noindex = False
        self.h1_count = 0
        self.json_ld = []
        self.reading_json = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("name") == "robots":
            self.noindex = "noindex" in attrs.get("content", "")
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.reading_json = True
            self.json_ld.append("")
        for attribute in ("href", "src", "poster", "data-src"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])

    def handle_data(self, data):
        if self.reading_json:
            self.json_ld[-1] += data

    def handle_endtag(self, tag):
        if tag == "script":
            self.reading_json = False


def validate():
    pages = {}
    for path in OUTPUT.rglob("*.html"):
        page = Page()
        page.feed(path.read_text())
        assert page.h1_count == 1, f"Expected one h1: {path}"
        for block in page.json_ld:
            json.loads(block)
        if not page.noindex:
            route = "/" if path.name == "index.html" else "/" + path.relative_to(OUTPUT).as_posix()
            assert page.canonical == "https://rotinita.com.br" + route, f"Canonical: {path}"
        pages[path.resolve()] = page
    for path, page in pages.items():
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            target = ((OUTPUT if url.path.startswith("/") else path.parent) / unquote(url.path).lstrip("/")).resolve() if url.path else path
            if target.is_dir():
                target /= "index.html"
            assert target.is_relative_to(OUTPUT.resolve()) and target.is_file(), f"Missing reference: {path.name}: {reference}"
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f"Missing anchor: {reference}"
    assert pages[(OUTPUT / "auth/callback/index.html").resolve()].noindex
    for name in ASSOCIATIONS:
        json.loads((OUTPUT / ".well-known" / name).read_text())
    json.loads((OUTPUT / "site.webmanifest").read_text())
    tree = ET.parse(OUTPUT / "sitemap.xml")
    for location in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        route = urlsplit(location.text).path
        path = OUTPUT / (route.lstrip("/") or "index.html")
        assert path.resolve() in pages and not pages[path.resolve()].noindex, f"Sitemap: {location.text}"
    assert not list(OUTPUT.rglob("*.md"))
    assert not list(OUTPUT.rglob(".DS_Store"))
    print(f"Validated {len(pages)} HTML pages, JSON-LD, links, sitemap and app associations.")


def main():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for source in public_files():
        assert not source.is_symlink(), f"Symlinks are not publishable: {source}"
        target = OUTPUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    validate()
    print(f"GitHub Pages artifact: {OUTPUT}")


if __name__ == "__main__":
    main()
