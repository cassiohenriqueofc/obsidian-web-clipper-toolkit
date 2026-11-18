# Review before publication

[Português](../pt-BR/publishing.md) · [Home](../../README.md)

The first release is private. This project does not enable GitHub Pages, change
repository visibility, or deploy a public website automatically. GitHub Pages
eligibility for private repositories depends on account/plan. A private source
repository does not by itself guarantee that a deployed website is private.
Check [GitHub's Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages).

## Preview locally

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8000/en-US/ or /pt-BR/. On Windows use py -3.

## Prepare a reviewed public URL

Only after choosing the actual destination, build absolute metadata with the
actual approved URL; the following is a demonstration, not a deployed site:

```bash
python3 scripts/build_site.py --base-url https://example.invalid/obsidian-web-clipper/ --indexable
python3 scripts/validate.py
```

Replace example.invalid. This enables canonical, hreflang, og:url, og:image,
Twitter image, JSON-LD URLs, sitemap, and indexable robots output. Deploy only the
site/ directory to the approved host. The builder does not deploy anything.

Open Graph previews are static social metadata; the clickable animated file
map is an independent HTML/SVG feature. Banner dimensions are 1774 × 887.
Links to repository files still require GitHub access while the repository is private.

## SEO and LLM review

Verify both language pages, title/description, canonical destination, absolute
image URL, robots policy, and the sitemap after hosting. Review llms.txt and
llms-full.txt: they improve discovery for supporting clients, not guaranteed
ranking or model behavior. There is no A2A service, automated agent endpoint, or
promise that private content is publicly crawlable.

Review license terms, screenshots, Git history, staged files, sample data, local
paths, and credentials before any public visibility change. Enabling public
Pages or changing a repo to public is a separate owner approval, not a side
effect of creating a private release.
