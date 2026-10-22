# Rotinita site

This repository is a static Portuguese-language website for Rotinita. `CNAME` and `.nojekyll` configure GitHub Pages for the custom domain. There is no package manager or framework. Python's standard library packages and validates the public files for Pages.

## Structure

- `index.html` is the landing page. The other root HTML files cover visual routines, communication, help, legal information and the 404 page.
- `css/style.css` holds the shared visual tokens, layout, and responsive rules; `js/main.js` holds navigation and scroll behavior.
- `assets/video/` contains the published hero video and its static poster. Source renders stay in the ignored `design-assets/video/` directory.
- `auth/callback/index.html` is the app callback fallback page. `.well-known/` contains app association files.
- Favicons, logos, social images, `site.webmanifest`, `robots.txt`, and `sitemap.xml` are published from the repository root.
- `design-assets/` contains source design material and is ignored by Git. Copy only assets needed by the published site into tracked paths.

## Editing and verification

- Preserve the existing Portuguese copy style and the Fraunces/Outfit typography and colors in `css/style.css`.
- Keep page titles, descriptions, social tags, structured data, store links, and the sitemap consistent with the published content.
- The official Instagram is `https://www.instagram.com/rotinita/`, supplied by
  the owner. Keep it in the home page publisher's `Organization.sameAs` and in
  the home/legal footer links (`rel="me"`). Reuse the existing footer styles;
  no Instagram embed or SDK is needed. Local markup does not prove publication
  or recognition by search engines. See WS-055 in `../docs/decisoes.md`.
- Escape `&` as `&amp;` in HTML attributes containing query strings.
- Run `python3 scripts/build_site.py`, `node --check js/main.js` and `git diff --check`. The build validates HTML references/anchors, one H1, canonical URLs, JSON-LD, sitemap and association JSON. There is no separate lint/typecheck framework. Review desktop/mobile rendering and behavior as well; syntax checks do not replace those checks.
- Keep hero video playback muted and start it automatically only when reduced motion is not requested; preserve the static poster fallback. When illustrative footage is used, retain the visible disclosure and do not describe it as real product footage.
- On the landing page, the fixed header stays transparent with the logo visually hidden while it overlaps the hero; after the hero it returns to the standard light header and logo.
- Preview the actual public artifact with `python3 -m http.server 8765 --bind 127.0.0.1 --directory _site` after building. The installed `tidy` does not recognize this site's HTML5 semantic tags, so use browser rendering for HTML checks.
- Before linking the privacy policy in the Alexa skill store, keep its description of parent account linking, voice interpretation, reminder text and cancellation consistent with `routine-gateway/docs/alexa-certificacao.md`. The public policy must be deployed separately from the gateway.
- Validate `sitemap.xml` with `xmllint --noout sitemap.xml` when available; parse `site.webmanifest` and the landing page JSON-LD as JSON after metadata edits.
- The `como-funciona` demonstration uses a Flutter component capture with fictional
  repositories/data, not a family account. Preserve its visible disclosure and
  the provenance in `assets/images/README.md`. It does not prove release state,
  clinical efficacy or completed purchases. Keep the Free entry separate from
  Plus expansion; individual price and terms come from the store offer.
- `.github/workflows/pages.yml` validates pull requests and publishes pushes to
  `main` through GitHub Actions. Pages must use `build_type: workflow` rather
  than legacy root publication. Verify the run and public content after a push.
  Do not include unrelated dirty files in a publication.
- The cross-ecosystem SEO baseline and proposed acceptance checks are in
  `../docs/seo-ecossistemas-20261022.md` (WS-056). A Lighthouse SEO score is not
  evidence of indexing, AI citations, store accuracy or native integration.
  Recheck public state before reusing dated findings. Keep essential content
  visible without JavaScript; animation should progressively enhance it.
- App association files currently cover authentication, not all website pages.
  Preserve callback paths/query parameters when consolidating URLs. Validate
  AASA MIME/origin and Apple CDN separately; a CDN response is not a device test.
  Android validation needs the distributed Play signing certificate. Public
  crawler User-Agent probes do not establish access from real crawler IPs.
- `scripts/build_site.py` uses an allowlist to generate ignored `_site/` without
  technical Markdown, scripts, workflows or `.DS_Store`. Preserve `.well-known`,
  callback and assets. The workflow archives `_site` explicitly: the default
  `upload-pages-artifact` exclusion for dot directories would omit `.well-known`.
  Do not commit `_site` or return to direct root publication.
- SEO transport rules live in Cloudflare, scoped to the public site hosts:
  `/index` and `/index.html` redirect to the HTTPS apex first; then HTTP and
  `www` redirect preserving paths and query strings (308). The AASA response
  on the apex receives `Content-Type: application/json`. GitHub's HTTPS switch
  returned "certificate does not exist yet" during setup; do not change
  zone-wide SSL, DNS or app/API subdomains to work around it. See WS-057 and
  `../docs/seo-implementacao-20261022.md` for evidence and remaining checks.
- Keep essential content visible by default. Hero playback respects reduced
  motion, data saving and page visibility; the poster is available before the
  video loads. Fonts load from HTML rather than a CSS `@import` chain.
- Smart App Banner uses the verified App Store ID `6761869737`; do not add an
  `app-argument` for unsupported routes. Structured data connects Organization,
  WebSite and SoftwareApplication without invented ratings or reviews.

## Qualidade arquitetural obrigatória

Seguir SOLID e Clean Code pragmaticamente: responsabilidades coesas, dependências
explícitas, nomes claros, tratamento de erros e testes dos efeitos observáveis.
É proibido introduzir triggers, stored procedures ou funções armazenadas para
regras de negócio/efeitos implícitos. Regras e orquestração ficam na aplicação;
migrations cuidam do schema/dados. Preservar transações, integridade, índices,
unicidade, locks e SQL nativo de calendário. Não criar camadas/abstrações sem
necessidade. Consultar [guia compartilhado](../guides.md) antes de implementar.
