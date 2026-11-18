# Capture specification

- Baseline: Web Clipper 1.7.1 and Obsidian 1.15.1; user reported, not fully live-tested.
- Template language: English. Documentation languages: en-US and pt-BR.
- Execution: always manual Interpreter; no template can enforce the global setting alone.
- Tracked destination: Demo Vault / clippings. Private customization is ignored by Git.
- Optional copy: manual copy of saved Markdown; no automatic dual-vault save claimed.
- Formatting: separate foldable callouts with one structural > prefix. No authored
  > > nesting. Prefix blank lines and code fences as well as content lines.
- Copyable explanations, source evidence, and briefs are fenced. Interactive
  tasks are outside fences inside their callout.
- Original content variable is not sliced. It can represent page extraction,
  selection, or highlights; it does not guarantee full-page or video access.
- Model evidence is bounded: Markdown 24000, HTML 8000, JSON-LD 12000 characters.
- Preserve uncertainty; no invented external search results or existing vault links.
- Preserve a deterministic Archive option for provider failures and syntax-heavy sources.
- Source-preservation limit: literal Clipper expressions can be reprocessed in AI
  variants in 1.7.1. Prefer Archive without Interpreter for such source pages.
