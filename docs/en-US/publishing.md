# Publishing and indexing

[Português](../pt-BR/publishing.md) · [Home](../../README.md)

## Deployment status

The owner authorized public indexing and GitHub Pages deployment at:

`https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`

The workflow is configured, but GitHub Actions has not started because the account is billing-locked. The Pages API also returned 403. The site is not live; do not submit its sitemap or claim indexing until a successful deployment is verified.

## Generated SEO signals

The indexable build emits a unique title and description for each of seven locale pages, absolute canonical URLs, `hreflang` links plus `x-default`, Open Graph and Twitter image metadata, and `SoftwareSourceCode` JSON-LD. The social image is a static 1200 × 630 JPEG; the animated workflow image is separate. The language chooser and 404 page are `noindex,follow` and are excluded from the sitemap. `robots.txt` permits crawling and names the sitemap in the indexable build. Sitemap `lastmod` uses the reviewed Proposal date; update that date when the documented project content changes.

These signals help crawlers understand and preview pages; they do not guarantee ranking, indexing, or rich results. `llms.txt` is a navigation aid for compatible clients, not a Google ranking feature. JSON-LD describes the project and is not a special requirement for AI search.

## Build and verify

```bash
python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable
python3 scripts/validate.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

The builder does not deploy. After Actions billing is restored, run the workflow, verify all locale URLs, metadata, `robots.txt`, `sitemap.xml`, and 404 behavior. Then verify ownership in Google Search Console and Bing Webmaster Tools and submit the live sitemap. Search Console verification tokens and owner account access are not stored in this repository.

GitHub's repository About text, topics, and social preview are separate Settings fields. The recommended About description is recorded in [the SEO review](../../project/seo-review.md); these settings have not been changed. No custom domain is configured.
