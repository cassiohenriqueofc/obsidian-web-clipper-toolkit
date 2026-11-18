# Project guide

[English (US)](../en-US/guide.md) · [Português (Brasil)](../pt-BR/guide.md) · [Español (Argentina)](../es-AR/guide.md) · [Español (México)](../es-MX/guide.md) · [Español (España)](../es-ES/guide.md) · [Deutsch](../de-DE/guide.md) · [Français](../fr-FR/guide.md)

Updated: 2026-11-18 · 0.1.3 · Public release · GitHub Pages configured

## Purpose

Use portable JSON and Markdown, inspect model suggestions, preserve source evidence, and keep a no-AI fallback.

## Installation

Install Obsidian and the official Web Clipper in a supported browser. Create a vault folder, import a template, verify the vault name and folder, and keep automatic Interpreter execution disabled. For AI styles click Interpret manually, review, and save. Do not run Interpreter for Archive.

```powershell
# Windows — project root
py -3 scripts/configure_templates.py --vault "Demo Vault" --folder "clippings"
py -3 scripts/build_site.py
py -3 scripts/validate.py
```

```bash
# macOS / Linux — project root
python3 scripts/configure_templates.py --vault 'Demo Vault' --folder 'clippings'
python3 scripts/build_site.py
python3 scripts/validate.py
```

## Development

Use a local Git clone and a private GitHub repository for projects. Use feature branches, factual commits, reviewed diffs and a dated change log. Do not create repositories for everyday tasks or simple chats.

## Privacy

Use demo data. Ignore local-only settings, credentials, private notes and personal paths. Private GitHub access does not make committed secrets safe. The owner expressly authorized the attribution below; no other personal data is approved.

## License

Noncommercial source-available license. Commercial use requires separate permission. Shared modified versions need corresponding source, attribution, the same license and a dated modification log. Private edits do not require publication. This is not OSI-approved open source. The English LICENSE is authoritative.

## Sources and attribution

Use verified Markdown URL links on GitHub and separate wikilinks for existing Obsidian notes. Record upstream URL, revision, license, reused files and changes before distributing reused work. Do not invent attribution or assume license compatibility.

## Reusable project starter

Edit the flat frontmatter in project-template/Proposal.md. Render a new, empty directory using new_project.py. The generator never creates a remote, pushes, deploys, or implements the application. Review names, email, URLs and license before publishing.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

## Local and remote storage

Keep the full local clone and the private remote. Commit and push reviewed work; GitHub is not automatic synchronization. Keep a separate backup for ignored settings. Remove duplicate ZIPs and disposable previews to reduce disk usage, not source templates or scripts.

## Publication and metadata

The GitHub Pages workflow is configured for https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/. Its first deployment must complete before the site is considered live. Published output uses canonical URLs, Open Graph/Twitter, hreflang, JSON-LD, sitemap and indexable robots. llms files do not guarantee ranking.

## Validation and limits

Template structure, local links, privacy patterns, packaging and browser page interactions are checked locally. Earlier isolated 1.7.1 renderer checks passed. Live provider execution, installed extension saves and Windows/macOS/Linux end-to-end acceptance remain pending.

The original content variable may contain a selection or highlights. The AI context is bounded. In Clipper 1.7.1 literal template expressions can be reprocessed in AI variants; use Archive without Interpreter when this matters. Automatic second-vault copying is not implemented.

For each new file, state its real purpose, data classification, source credit when applicable, and meaningful validation. Notes use flat YAML; source files use a short useful header; comments explain reasons and constraints instead of repeating code. Never invent tests or results.

**Developed by:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)
