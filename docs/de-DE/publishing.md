# Veröffentlichung und Indexierung

[English](../en-US/publishing.md) · [Startseite](../../README.md)

## Aktueller Stand

Der Inhaber hat die Veröffentlichung und Indexierung unter `https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/` autorisiert. Der Workflow ist eingerichtet, aber GitHub Actions wurde wegen einer Kontosperre aufgrund eines Abrechnungsproblems nicht gestartet. Die Website ist noch nicht veröffentlicht. Reiche die Sitemap erst ein und behaupte keine Indexierung, wenn eine erfolgreiche Veröffentlichung bestätigt wurde.

## Erzeugte Metadaten

Der indexierbare Build erstellt je Sprache einen eigenen Titel und eine Beschreibung, absolute Canonical-URLs, `hreflang` und `x-default`, Open-Graph- und Twitter-Metadaten sowie `SoftwareSourceCode`-JSON-LD. Das statische Social-Bild ist 1200 × 630 Pixel groß; das GIF ist davon getrennt. Sprachauswahl und 404-Seite verwenden `noindex,follow` und stehen nicht in der Sitemap. `robots.txt` erlaubt das Crawling und nennt die Sitemap. `lastmod` verwendet das geprüfte Proposal-Datum; aktualisiere es bei Änderungen am dokumentierten Projektinhalt.

Diese Angaben helfen Suchmaschinen beim Verstehen und Darstellen der Seiten, garantieren aber weder Ranking noch Indexierung oder erweiterte Suchergebnisse. `llms.txt` dient kompatiblen Clients als Inhaltsverzeichnis und verbessert nicht das Google-Ranking.

## Erstellen und prüfen

```bash
python3 scripts/build_site.py --base-url https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/ --indexable
python3 scripts/validate.py
```

Nach Aufhebung der Actions-Sperre starte den Workflow und prüfe alle sieben Sprachen, `robots.txt`, Sitemap und 404-Seite. Bestätige die Inhaberschaft in Google Search Console und Bing Webmaster Tools, bevor du die veröffentlichte Sitemap einreichst. Prüftokens gehören nicht in dieses Repository. GitHub-Beschreibung, Themen und Social-Bild sind separate Einstellungen und noch offen.
