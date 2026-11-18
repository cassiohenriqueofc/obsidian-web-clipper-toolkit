# Search and repository presentation review — 2026-11-18

## Positioning

Preferred display name: **Obsidian Web Clipper Toolkit**.
Repository slug: **obsidian-web-clipper-toolkit**. The owner has now renamed the
public GitHub repository; the previous `obsidian-web-cliper` spelling omitted a
`p`. The project remains a community template toolkit, not an official Obsidian
extension.

Recommended GitHub About description:

> Source-preserving Obsidian Web Clipper templates for manual AI interpretation and structured Markdown notes.

Recommended page description:

> Capture webpages with Obsidian Web Clipper templates, run interpretation prompts manually, and save source-preserving Markdown notes with structured callouts.

Use these phrases naturally where they describe the actual project: **Obsidian
Web Clipper templates**, **manual AI interpretation**, **source-preserving web
capture**, **Markdown notes**, and **knowledge management**. Do not repeat them as
keyword lists or promise rank positions.

## Search findings

The official Obsidian Web Clipper repository describes the extension as a way to
highlight and capture web pages in a browser. Public GitHub search results also
show multiple community repositories labeled as Web Clipper template collections.
The toolkit should therefore distinguish its purpose: English prompts run only
when the user starts Interpreter manually; supplied source content remains in the
saved note; and one template offers capture without model interpretation.

This review is a qualitative search-result and repository-page review. It does
not include Google Keyword Planner volume, Google Search Console performance, or
stable star/fork rankings. The repository is now public; search ranking and indexing results still require time and Search Console data.

## Current implementation

- The root README uses the generated banner, language links, a template table, quick-start commands, example links, navigation, and a prominent animated feature flow.
- Seven language READMEs and seven language pages are linked from the project.
- The site builder creates locale-specific titles/descriptions, absolute canonical URLs, seven `hreflang` alternates plus `x-default`, Open Graph/Twitter metadata, and `SoftwareSourceCode` JSON-LD. The indexable build includes crawlable robots rules and a sitemap. The language chooser and 404 are noindex and excluded from the sitemap.
- The new static Open Graph/Twitter preview is 1200 × 630 JPEG. The original banner and animated workflow remain distinct assets. The animation is not used as social preview.
- Sitemap `lastmod` is drawn from the reviewed Proposal date. Keep that date aligned with content changes; omit `changefreq` and `priority`, which Google ignores.
- GitHub Pages is configured at the repository URL, but the site is not live: GitHub Actions is blocked by an account billing lock, the Pages API returned 403, and the deployed URL returned 404 during the prior check. The owner authorized publishing and indexing; deployment still needs a successful workflow.
- No stars, trending badges, contributor totals, or release counts are hard-coded. Do not claim rankings, indexing, or rich results.
- GitHub confirms that the repository is public and template-enabled. The connected API returned HTTP 403 for About-description and topic changes; browser settings access was unavailable. The repository description remains its earlier wording.

## Publication controls

After publication:

1. Review the entire Git diff, release ZIP, settings, and privacy scan.
2. The canonical URL is the GitHub Pages project URL. Confirm a successful deploy before treating it as live or requesting indexing.
3. Verify titles, descriptions, canonical URLs, language alternates, social image,
   JSON-LD, robots policy, and sitemap on the live site. Register and verify the
   property in Google Search Console before requesting indexing.
4. GitHub topic tags are still pending because the connected settings API and browser UI could not update them.
5. The GitHub social-preview image remains a manual Settings item; use `assets/social-preview-1200x630.jpg`. The animated feature flow is separate and available in the README/site.
6. Do not add an `FAQPage` rich-result strategy: Google removed FAQ rich results
   in May 2026. Keep helpful FAQ prose only if it answers real user questions.

Google says its generative search features do not require special schema.org
markup, and `llms.txt` does not change Google Search visibility or rankings.
Structured data remains useful for describing the software and can make eligible
pages qualify for supported search features; it does not guarantee a rich result.

## Sources

- [Official Obsidian Web Clipper repository](https://github.com/obsidianmd/obsidian-clipper)
- [Google guidance for AI features in Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google title-link guidance](https://developers.google.com/search/docs/appearance/title-link)
- [Google snippet and description guidance](https://developers.google.com/search/docs/appearance/snippet)
- [Google Search documentation updates](https://developers.google.com/search/updates)
- [Google sitemap guidance (`lastmod`, `changefreq`, and `priority`)](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google AI features and website guidance](https://developers.google.com/search/docs/appearance/ai-features)
- [GitHub Pages custom 404 guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site)
- [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub topic guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub social preview guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [GitHub repository search guidance](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)


## Technical corrections (2026-11-18)

The reusable, Obsidian-ready reference is [SEO signals and website proposal playbook](seo-signals-and-indexing-playbook.md). It includes the current indexing state, page metadata, platform mockups, and a proposal checklist.

The supplied SEO notes mixed a personal portfolio identity and the personal domain with this toolkit. They were not imported: the repository has its own GitHub Pages URL and no authorized custom domain. The notes' recommendations were checked against the actual static Python build instead of treating their personal-site instructions as project requirements.

Google guidance does not require special markup for AI Overviews/AI features; structured data must describe visible content and does not guarantee enhanced results. `llms.txt` has no documented Google ranking effect. `robots.txt` is not a way to remove an already indexed URL. A meta refresh is not an HTTP 301; GitHub Pages does not provide server-side redirects or custom response headers. The toolkit now uses a custom 404 page, but legacy redirects remain unavailable without a separate redirect service.

Before indexing: restore Actions billing, verify a successful deployment and live metadata, verify site ownership in Search Console/Bing, then submit the sitemap. These operations require working GitHub/account access and were not performed in this local SEO change.
