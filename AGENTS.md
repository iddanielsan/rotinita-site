# Rotinita site

This repository is a static Portuguese-language website for Rotinita. `CNAME` and `.nojekyll` configure GitHub Pages for the custom domain. There is no package manager, build script, or test suite in the repository.

## Structure

- `index.html` is the landing page. The other root HTML files cover legal information and the 404 page.
- `css/style.css` holds the shared visual tokens, layout, and responsive rules; `js/main.js` holds navigation and scroll behavior.
- `auth/callback/index.html` is the app callback fallback page. `.well-known/` contains app association files.
- Favicons, logos, social images, `site.webmanifest`, `robots.txt`, and `sitemap.xml` are published from the repository root.
- `design-assets/` contains source design material and is ignored by Git. Copy only assets needed by the published site into tracked paths.

## Editing and verification

- Preserve the existing Portuguese copy style and the Fraunces/Outfit typography and colors in `css/style.css`.
- Keep page titles, descriptions, social tags, structured data, store links, and the sitemap consistent with the published content.
- Escape `&` as `&amp;` in HTML attributes containing query strings.
- Review the diff and check local references, metadata, and desktop/mobile layout after edits. No repository-defined lint, typecheck, build, or test commands exist.
- Preview locally with `python3 -m http.server 8765 --bind 127.0.0.1` and inspect the page in a browser. The installed `tidy` does not recognize this site's HTML5 semantic tags, so use browser rendering for HTML checks.
- Validate `sitemap.xml` with `xmllint --noout sitemap.xml` when available; parse `site.webmanifest` and the landing page JSON-LD as JSON after metadata edits.
