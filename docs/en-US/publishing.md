# Publishing and indexing

[Português](../pt-BR/publishing.md) · [Home](../../README.md)

## Live destination

The owner authorized public indexing and deployment. The project uses GitHub Pages at:

`https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/`

`.github/workflows/deploy-pages.yml` builds the multilingual `site/` directory with the canonical URL and `--indexable`, validates it, enables Pages, and deploys the artifact after pushes to `main`. Check the Actions run and open all locale paths after the first deployment; a configured workflow alone does not prove the site is live.

The generated output includes canonical URLs, hreflang alternatives, Open Graph and Twitter metadata, SoftwareSourceCode JSON-LD, `robots.txt`, `sitemap.xml`, `llms.txt`, and `llms-full.txt`. Search indexing can take time and is not guaranteed.

## Preview or rebuild

```bash
python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable
python3 scripts/validate.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

The builder does not deploy. GitHub Actions performs deployment. The default build without `--indexable` remains noindex for local previews.

The Open Graph image is static (`assets/social-preview.jpg`); the animated feature flow is separate. Set the repository's social-preview image through GitHub Settings if desired. Repository About metadata and topics are managed separately and remain pending if the connected settings access rejects them.

Check page titles, descriptions, canonical destinations, language alternates, image URLs, robots policy, sitemap, and mobile layout after deployment. `llms.txt` may help compatible clients navigate documentation; it does not change Google rankings. Structured data describes the software but does not guarantee rich results.
