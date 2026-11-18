---
title: "SEO Signals, Indexing, and Website Proposal Playbook"
date: 2026-11-18
status: "Metadata implemented; public Pages deployment blocked"
tags:
  - website/seo
  - github-pages
  - indexing
  - open-graph
  - project-proposal
---

# SEO Signals, Indexing, and Website Proposal Playbook

> [!NOTE]+ Purpose
> Keep this note in Obsidian as a reusable reference for planning, implementing,
> auditing, and fixing SEO on a future website. Examples use this toolkit's
> current metadata as realistic sample content. Preview panels are mockups, not
> screenshots or proof of indexing.

## Current session snapshot

**Checked:** 2026-11-18 (America/Sao_Paulo)

**Repository:** cassiohenriqueofc/obsidian-web-clipper-toolkit

**Version at session start:** 0.1.4 on main; this playbook is bundled as 0.1.5

**Planned Pages URL:** https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/

**Locale routes:** /en-US/, /pt-BR/, /es-AR/, /es-MX/, /es-ES/, /de-DE/, /fr-FR/

### Implemented title and description values

These are the page-level values in the generated HTML. Google may rewrite its
title link or snippet to match a query.

| Locale | Page title | Description |
| --- | --- | --- |
| en-US | Web Clipper templates with source-preserving AI notes \| Obsidian Web Clipper Toolkit | Use Obsidian Web Clipper templates to capture webpages, run AI interpretation manually, and save structured Markdown notes that preserve the source content. |
| pt-BR | Templates do Web Clipper com notas de IA e fontes preservadas \| Obsidian Web Clipper Toolkit | Use templates do Obsidian Web Clipper para capturar páginas, interpretar com IA manualmente e salvar notas Markdown estruturadas que preservam o conteúdo original. |
| es-AR | Plantillas de Obsidian Web Clipper: captura y fuentes \| Obsidian Web Clipper Toolkit | Usá plantillas de Obsidian Web Clipper para capturar páginas, interpretar contenido manualmente con IA y guardar notas Markdown estructuradas con sus fuentes. |
| es-MX | Plantillas de Obsidian Web Clipper para interpretar páginas \| Obsidian Web Clipper Toolkit | Usa plantillas de Obsidian Web Clipper para capturar páginas, interpretar contenido manualmente con IA y guardar notas Markdown estructuradas con sus fuentes. |
| es-ES | Plantillas de Obsidian Web Clipper para notas con fuentes \| Obsidian Web Clipper Toolkit | Usa plantillas de Obsidian Web Clipper para capturar páginas, analizar contenido con IA manualmente y guardar notas Markdown estructuradas que conservan las fuentes. |
| de-DE | Obsidian-Web-Clipper-Vorlagen für Markdown-Notizen mit Quellen \| Obsidian Web Clipper Toolkit | Nutze Obsidian-Web-Clipper-Vorlagen, interpretiere Seiten manuell mit KI und speichere strukturierte Markdown-Notizen mit den Quellen der Seiten. |
| fr-FR | Modèles Obsidian Web Clipper pour des notes Markdown sourcées \| Obsidian Web Clipper Toolkit | Utilisez les modèles Obsidian Web Clipper pour capturer des pages, interpréter manuellement avec l’IA et conserver les sources dans des notes Markdown. |

| State | Verified status |
| --- | --- |
| SEO implementation | Merged to main in [PR #6](https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit/pull/6) |
| Post-merge status notes | Merged in [PR #7](https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit/pull/7) and [PR #8](https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit/pull/8) |
| Site build | Seven locale pages generated with indexable metadata |
| GitHub Actions | The [Pages run](https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit/actions/runs/44419965141) and [validation run](https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit/actions/runs/44419965197) fail before steps start; GitHub reports an account billing lock |
| GitHub Pages configuration | API creation request returned 403; public Pages URL returned 404 |
| Sitemap availability | Generated at site/sitemap.xml; not publicly reachable while Pages is unavailable |
| Search Console / Bing verification | Not completed; sitemap not submitted |
| Search results | Search probe returned no relevant listing; this does not prove the repository or site is unindexed |
| Share card | 1200 × 630 JPEG is available in assets/social-preview-1200x630.jpg; live platform rendering not tested |
| GitHub About, topics, repository social image | Manual Settings changes remain pending |

> [!IMPORTANT]+ Current indexing conclusion
> The generated build contains SEO tags and crawl files, but Google and Bing
> cannot fetch the planned Pages site while its public URL returns 404. The
> Search Console property is not verified and the sitemap is not submitted.
> Treat the website as not deployed and not verified for indexing. The public
> GitHub repository is a separate destination and may be discoverable on its
> own. A failed search probe is not proof that a page is absent from an index.

## Session log

| Session | Work completed | Status / next action |
| --- | --- | --- |
| 2026-11-18 · SEO implementation | Reviewed the Python builder; separated unrelated personal-site material; added locale metadata, canonical and language alternates, Open Graph/Twitter fields, JSON-LD, share image, noindex chooser/404, robots and sitemap; updated seven publishing guides. | Source merged. Wait for GitHub billing/Pages access, deploy, and inspect live output. |
| 2026-11-18 · Handoff and release | Merged PRs #6, #7 and #8. Uploaded sanitized ZIP, manifest and checksums to artifacts/v0.1.4. Local validation, smoke checks, metadata assertions and package integrity passed. | Search Console/Bing, GitHub Settings and installed-app/OS acceptance are pending. |
| 2026-11-18 · SEO playbook | Added the metadata reference, preview mockups, two Mermaid graphs, session record, and reusable proposal checklist; updated README and generated site index. Local checks pass. | Included in the v0.1.5 package; deployment/indexing remain blocked externally. |
| Next session · 2026-11-19 | Start from the dated project handoff and check latest Actions status. | Retry deployment only after the billing lock is resolved. |

**Time estimate:** The elapsed duration was not measured, so no duration is claimed. After GitHub restores Actions and Pages access, allow about 30–60 minutes for deployment setup and live technical checks if credentials and settings are available. Search crawling may take days or weeks and is not guaranteed.

## How the current SEO setup works

The static builder is scripts/build_site.py. It writes one HTML page per locale and, for the indexable build, emits crawl metadata, robots.txt, and sitemap.xml.

| Signal | Purpose | Current implementation |
| --- | --- | --- |
| Page title and visible H1 | State the page topic and language | Descriptive titles and headings for each locale |
| Meta description | Offer a concise summary that may become a search snippet | One description per locale; Google may choose page text instead |
| Canonical | Identify the preferred URL for equivalent content | Absolute canonical URL per locale route |
| hreflang and x-default | Connect language alternatives | Seven locale routes plus x-default |
| Open Graph | Supply title, description, URL, type and image for share cards | Unique title/description, canonical URL, static 1200 × 630 image, alt text and dimensions |
| Twitter Card | Supply X card type and matching share fields | summary_large_image, title, description, image and alt text |
| JSON-LD SoftwareSourceCode | Describe the toolkit in machine-readable form | Uses known project facts; does not guarantee rich results |
| robots.txt | State crawl policy and sitemap location | Indexable build allows crawling and lists the sitemap |
| noindex,follow | Keep selected HTML pages out of search while leaving links followable | Root language chooser and 404 page |
| Sitemap | Help crawlers discover canonical routes | Seven locale pages only; lastmod uses the Proposal date |
| Custom 404 | Help visitors recover from a missing route | site/404.html; effective after Pages is deployed |

The sitemap lastmod value must reflect a real significant page update. This
project derives it from the reviewed Proposal date; update that date when
substantive documented content changes. Google ignores changefreq and priority,
so the generator omits them.

llms.txt is a navigation aid for clients that choose to use it. Do not present
it as a Google ranking signal or an AI search requirement. Google says standard
Search fundamentals apply to AI Overviews and AI Mode; no special schema.org
markup is needed for those features.

### Discovery and preview flow

> [!NOTE]+ Indexing is a sequence, not a switch
> A metadata change does not instantly create a search result. A page must be
> reachable, crawled, eligible, selected for indexing, and then rendered by a
> search product. Each stage may be delayed or declined.

> ~~~mermaid
> flowchart LR
>   A["Proposal and page content"] --> B["Build static HTML"]
>   B --> C["Live HTTPS page"]
>   C --> D["Crawler can fetch page"]
>   D --> E["Canonical and language signals processed"]
>   E --> F["Index decision"]
>   F --> G["Google or Bing result"]
>   F --> H["AI search may cite page"]
>   C --> I["Social crawler reads Open Graph"]
>   I --> J["Link preview card"]
>   C --> K["GitHub repository metadata"]
>   K --> L["GitHub repository search and README"]
>   X["Current blocker: Pages returns 404"] -. blocks .-> C
> ~~~

For this project, the path stops before “Live HTTPS page.” The metadata is in
the generated files, but the configured Pages URL currently returns 404.

### Content-to-metadata build graph

> [!NOTE]+ Keep SEO fields tied to approved page content
> Proposal facts feed the route copy and metadata. The build should derive
> structured data from the same evidence, then validation checks the generated
> result before deployment.

> ~~~mermaid
> flowchart TB
>   P["Reviewed website proposal"] --> R["Route and locale content"]
>   R --> G["Static site generator"]
>   I["Approved identity and project facts"] --> G
>   A["Share image and alt text"] --> G
>   G --> H["HTML title, description, canonical, hreflang"]
>   G --> S["Open Graph, X Card, JSON-LD"]
>   G --> C["robots.txt and sitemap.xml"]
>   H --> V["Local validation and preview review"]
>   S --> V
>   C --> V
>   V --> D["Deployment after access is ready"]
>   D --> M["Search Console, Bing, and social preview checks"]
> ~~~

## Search and sharing preview mockups

These examples use the project's current English metadata and show where it
could appear after deployment. They are mockups, not actual indexed results.
Search engines and social platforms control their final text, cropping, caches,
and display; they may rewrite or omit fields.

### Google organic result

> [!EXAMPLE]+ Google Search mockup
> ~~~text
> Obsidian Web Clipper Toolkit
> cassiohenriqueofc.github.io › obsidian-web-clipper-toolkit › en-US
> Web Clipper templates with source-preserving AI notes | Obsidian Web Clipper Toolkit
> Use Obsidian Web Clipper templates to capture webpages, run AI interpretation
> manually, and save structured Markdown notes that preserve the source content.
> ~~~

Google may build the title link from page titles, headings, prominent text,
Open Graph title, and links. It usually selects snippet text from the page and
may use the meta description when it better matches the query.

### Google AI result

> [!EXAMPLE]+ Possible citation layout
> ~~~text
> AI Overview
> [Answer assembled by Google from selected sources]
>
> Sources
> [Obsidian Web Clipper Toolkit]  [Another selected source]
> ~~~

This is only a layout illustration. There is no guarantee that an AI result
will appear, cite this site, or use these words.

### Bing result

> [!EXAMPLE]+ Bing Search mockup
> ~~~text
> Web Clipper templates with source-preserving AI notes
> https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/en-US/
> Use Obsidian Web Clipper templates to capture webpages, run AI interpretation
> manually, and save structured Markdown notes that preserve the source content.
> ~~~

Bing chooses its own final result text. After deployment, verify the property
and sitemap in Bing Webmaster Tools.

### GitHub repository search

> [!EXAMPLE]+ GitHub search mockup
> ~~~text
> cassiohenriqueofc / obsidian-web-clipper-toolkit
> Source-preserving Obsidian Web Clipper templates for manual AI interpretation
> and structured Markdown notes.
> Topics: obsidian · web-clipper · markdown · templates · knowledge-management
> ~~~
> The repository is public. The About text and topics above are recommendations,
> not confirmed live settings. GitHub search can consider repository name,
> description, topics, and README contents.

### Open Graph share card: Facebook, LinkedIn, and chat apps

> [!EXAMPLE]+ Link preview mockup
> ~~~text
> ┌──────────────────────────────────────────────────────────────┐
> │ [assets/social-preview-1200x630.jpg]                         │
> ├──────────────────────────────────────────────────────────────┤
> │ Obsidian Web Clipper Toolkit                                  │
> │ Use Obsidian Web Clipper templates to capture webpages, run  │
> │ AI interpretation manually, and save structured notes.      │
> │ cassiohenriqueofc.github.io                                   │
> └──────────────────────────────────────────────────────────────┘
> ~~~
> The generated page points to this image with an absolute HTTPS URL. Until the
> page and asset are publicly reachable, a platform cannot fetch this preview.
> After deployment, inspect the exact route in LinkedIn Post Inspector and the
> relevant platform preview/debugger; refresh caches after changes.

### X card

> [!EXAMPLE]+ X / Twitter Card mockup
> ~~~text
> ┌──────────────────────────────────────────┐
> │ [Large image: 1200 × 630 share artwork]  │
> ├──────────────────────────────────────────┤
> │ Web Clipper templates with source-       │
> │ preserving AI notes                      │
> │ Capture webpages, interpret manually,    │
> │ and preserve source content in Markdown. │
> └──────────────────────────────────────────┘
> ~~~
> The generated HTML sets twitter:card to summary_large_image. X controls the
> actual rendering and may apply its own cache and presentation rules.

### Social image file

![Static 1200 × 630 social-preview artwork](../assets/social-preview-1200x630.jpg)

This is the static share-card image. The five-stage GIF on the site and README
explains the workflow; it is a separate asset and is not used for social cards.

## Where results can appear

| Destination | Main input | How to check after deployment | Current state |
| --- | --- | --- | --- |
| Google Search | Crawlable HTML, internal links, canonical, title, page content | Search Console URL Inspection and sitemap report; a site: query is only a probe | Not live or verified |
| Google AI Overviews / AI Mode | Search-eligible pages and helpful content; no special AI markup | Search Console reports where available; inspect actual citations | No site listing verified; citation is not guaranteed |
| Bing Search | Crawlable page and sitemap | Bing Webmaster Tools URL Inspection and sitemap report | Not live or verified |
| GitHub repository search | Repository name, About description, topics, README | Search with in:name, in:description, in:topics, and in:readme | Public repo; About/topics are pending |
| Facebook / LinkedIn / chat previews | Open Graph values and reachable image | LinkedIn Post Inspector and platform share preview/debug tools | Untested; Pages is unavailable |
| X | Twitter Card and Open Graph values; accessible image | Inspect the post composer or current card preview tool | Untested; Pages is unavailable |
| GitHub repo share card | Separate image in repository Settings | Open repository page and inspect its preview | Image ready; setting pending |

A GitHub repository page and a GitHub Pages website are separate. Repo About,
topics, and repository social preview do not replace the website's canonical,
sitemap, Open Graph, or Twitter metadata.

## Reusable proposal-driven workflow

### 1. Gather verified proposal facts

Record real, owner-approved answers before implementation:

- Project or organization name and one-sentence purpose
- Audience, user problem, actual services and deliverables
- Primary language and every supported locale
- Canonical domain and hosting platform; label planned versus verified
- Route list, navigation, and page purpose
- Approved public identity and contact information
- Repository, license, maintainer, and verified social accounts
- Primary user action and accurate call to action
- Real screenshots/share art, source, ownership, dimensions, and alt text
- Privacy, analytics, consent, form handling, and retention rules
- Webmaster account owner authorized to verify the property
- Build, tests, release, access, and deployment constraints

Do not invent facts, testimonials, traffic, awards, affiliations, dates, addresses,
schema fields, or search-volume claims. Keep secrets, personal settings exports,
and unrelated personal-site content out of a public repository.

### 2. Plan each route

For every indexable URL, record its locale, purpose, page title, visible H1,
unique description, canonical URL, language alternates, internal links, crawl
policy, sitemap inclusion, and structured data facts. Plan share title,
description, URL, image path, dimensions, and accessible alt text. Use
structured data only when it accurately matches visible content.

### 3. Build and audit locally

1. Inspect generated HTML; ensure metadata appears in the initial response.
2. Check URL host, casing, trailing slash, canonical, locales, status codes,
   redirects, and 404 behavior.
3. Parse JSON-LD and compare every field with visible, approved content.
4. Check robots policy and sitemap routes; exclude noindex and 404 pages.
5. Open the preview image URL; confirm HTTPS, file type, dimensions, file size,
   alt text, and safe cropping.
6. Test keyboard access, mobile layout, headings, performance, and image sizes.
7. Check links and remove broken download, navigation, and preview URLs.
8. Scan for secrets, personal paths, unapproved email addresses, and claims.
9. Record commands and results; label local checks separately from live checks.

### 4. Publish and verify

1. Confirm owner authorization, domain, HTTPS, hosting, and deployment access.
2. Deploy reviewed source and inspect the workflow run.
3. Fetch the public page, image, robots.txt, sitemap, canonical routes, and 404.
4. Verify ownership in Search Console and Bing Webmaster Tools.
5. Submit the live sitemap and inspect priority URLs.
6. Test social previews in platform tools; allow for cache refresh delays.
7. Monitor crawl issues, queries, and performance; save date-stamped evidence.
8. Update the Proposal, changelog, SEO note, and handoff after each session.

A sitemap helps discovery; it does not guarantee crawling, indexing, ranking, or
AI citations. A crawl request is not a guarantee. A noindex directive must be
crawlable so that a crawler can see it; do not block that page in robots.txt when
you rely on its noindex tag.

## Copy-ready SEO section for a new website proposal

> [!SUMMARY]+ Website search, indexing, and sharing plan
> Replace each placeholder with a verified fact. Mark unknown values as pending.
>
> ~~~markdown
> ## Search, indexing, and share-preview plan
>
> - Project name:
> - Purpose and audience:
> - User need and primary action:
> - Canonical domain:
> - Hosting and deployment method:
> - Routes and page purpose:
> - Primary language and locale routes:
> - Approved public organization/person facts:
> - Contact and social links:
> - Indexing policy by route:
> - Sitemap and robots.txt:
> - Page titles and descriptions:
> - Canonical and hreflang rules:
> - Structured data type and evidence per property:
> - Open Graph and X card title, description, and URL:
> - Preview image path, source, dimensions, format, and alt:
> - Accessibility and mobile requirements:
> - Analytics, consent, privacy, and retention:
> - Search Console / Bing property owner:
> - Local validation steps:
> - Deployment acceptance checks:
> - Unverified facts:
> - Risks, blockers, and dependencies:
> - Session owner and next review date:
> ~~~

## Project files and official references

- Builder: scripts/build_site.py
- Generated locale pages: site/{locale}/index.html
- Crawl policy and sitemap: site/robots.txt and site/sitemap.xml
- Share artwork: assets/social-preview-1200x630.jpg
- SEO decisions: project/seo-review.md
- Next-session checklist: project/handoff-2026-11-19.md
- Deployment record: project/release-checks.md

Official guidance (check for updates before a new site launch):

- [Google Search title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google Search snippets and descriptions](https://developers.google.com/search/docs/appearance/snippet)
- [Google AI features and websites](https://developers.google.com/search/docs/appearance/ai-features)
- [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google request to recrawl URLs](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
- [Google Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start/)
- [Google crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq)
- [Open Graph Protocol](https://ogp.me/)
- [LinkedIn shareable websites](https://www.linkedin.com/help/linkedin/answer/a521928)
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)
- [GitHub repository search](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
- [GitHub repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub social preview settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [GitHub Pages custom 404](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site)

## Obsidian note links

- [[project/seo-review]] · [Markdown file](seo-review.md)
- [[project/handoff-2026-11-19]] · [Markdown file](handoff-2026-11-19.md)
- [[project/release-checks]] · [Markdown file](release-checks.md)
- [[Proposal]] · [Markdown file](../Proposal.md)
