# Rotinita site

This repository is a static Portuguese-language website for Rotinita. `CNAME` and `.nojekyll` configure GitHub Pages for the custom domain. There is no package manager, build script, or test suite in the repository.

## Structure

- `index.html` is the landing page. The other root HTML files cover legal information and the 404 page.
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
- Review the diff and check local references, metadata, and desktop/mobile layout after edits. No repository-defined lint, typecheck, build, or test commands exist.
- Keep hero video playback muted and start it automatically only when reduced motion is not requested; preserve the static poster fallback. When illustrative footage is used, retain the visible disclosure and do not describe it as real product footage.
- On the landing page, the fixed header stays transparent with the logo visually hidden while it overlaps the hero; after the hero it returns to the standard light header and logo.
- Preview locally with `python3 -m http.server 8765 --bind 127.0.0.1` and inspect the page in a browser. The installed `tidy` does not recognize this site's HTML5 semantic tags, so use browser rendering for HTML checks.
- Before linking the privacy policy in the Alexa skill store, keep its description of parent account linking, voice interpretation, reminder text and cancellation consistent with `routine-gateway/docs/alexa-certificacao.md`. The public policy must be deployed separately from the gateway.
- Validate `sitemap.xml` with `xmllint --noout sitemap.xml` when available; parse `site.webmanifest` and the landing page JSON-LD as JSON after metadata edits.
- The `como-funciona` demonstration uses a Flutter component capture with fictional
  repositories/data, not a family account. Preserve its visible disclosure and
  the provenance in `assets/images/README.md`. It does not prove release state,
  clinical efficacy or completed purchases. Keep the Free entry separate from
  Plus expansion; individual price and terms come from the store offer.
- GitHub Pages was verified as deploying `main` from `/` (root). A push to that
  branch starts publication; verify the Pages run and public content afterward.
  Do not include unrelated dirty files in a commercial publication.
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
- Root publication also serves tracked technical Markdown files. Keep secrets
  and private documentation out of this repository; changing deploy inclusion
  requires preserving `.well-known`, callback and required assets.

## Qualidade arquitetural obrigatória

Seguir SOLID e Clean Code pragmaticamente: responsabilidades coesas, dependências
explícitas, nomes claros, tratamento de erros e testes dos efeitos observáveis.
É proibido introduzir triggers, stored procedures ou funções armazenadas para
regras de negócio/efeitos implícitos. Regras e orquestração ficam na aplicação;
migrations cuidam do schema/dados. Preservar transações, integridade, índices,
unicidade, locks e SQL nativo de calendário. Não criar camadas/abstrações sem
necessidade. Consultar [guia compartilhado](../guides.md) antes de implementar.
