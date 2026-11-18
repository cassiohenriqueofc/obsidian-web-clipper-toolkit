# Veröffentlichung und Indexierung

[English](../en-US/publishing.md) · [Startseite](../../README.md)

GitHub Pages ist unter `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/` eingerichtet. Der Workflow erstellt die siebensprachige Website mit Canonical-, Open-Graph/Twitter-, JSON-LD- und Sitemap-Angaben sowie indexierbaren robots-Regeln. Nach jedem Push auf `main` wird sie veröffentlicht. Prüfe den ersten Actions-Lauf, bevor die Website als verfügbar gilt.

Lokaler Build: `python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable`. Das Skript veröffentlicht nicht; GitHub Actions übernimmt das Deployment.

Das Open-Graph-Bild ist statisch (`assets/social-preview.jpg`); das erklärende GIF ist unabhängig. About-Text, Themen und GitHub-Social-Bild werden in Settings verwaltet; die aktuelle Verbindung kann sie nicht ändern.
