# Projektleitfaden

[English (US)](../en-US/guide.md) · [Português (Brasil)](../pt-BR/guide.md) · [Español (Argentina)](../es-AR/guide.md) · [Español (México)](../es-MX/guide.md) · [Español (España)](../es-ES/guide.md) · [Deutsch](../de-DE/guide.md) · [Français](../fr-FR/guide.md)

Aktualisiert: 2026-11-18 · 0.1.0 · Private Prüffassung

## Zweck

Portable JSON- und Markdown-Dateien nutzen, Modellvorschläge prüfen, Quellenbelege erhalten und eine Variante ohne KI bereithalten.

## Installation

Obsidian und den offiziellen Web Clipper in einem unterstützten Browser installieren. Einen Ordner im Vault anlegen, eine Vorlage importieren und Vault sowie Zielordner prüfen. Automatische Interpretation deaktiviert lassen. Bei KI-Vorlagen Interpret manuell ausführen, Ergebnis prüfen und speichern. Bei Archive Interpreter nicht ausführen.

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

## Entwicklung

Für Projekte einen lokalen Git-Klon und ein privates GitHub-Repository verwenden. Mit Branches, sachlichen Commits, geprüften Änderungen und datiertem Änderungsprotokoll arbeiten. Für Alltagsaufgaben oder einfache Chats kein Repository anlegen.

## Datenschutz

Demodaten verwenden. Lokale Einstellungen, Zugangsdaten, private Notizen und persönliche Pfade ausschließen. Ein privates Repository schützt kein bereits eingechecktes Geheimnis. Der Rechteinhaber hat nur die unten genannte öffentliche Zuordnung genehmigt.

## Lizenz

Quellverfügbare Lizenz für nichtkommerzielle Nutzung. Kommerzielle Nutzung benötigt eine gesonderte Erlaubnis. Weitergegebene geänderte Versionen müssen Quelltext, Urheberhinweise, dieselbe Lizenz und ein datiertes Änderungsprotokoll enthalten. Private Änderungen müssen nicht veröffentlicht werden. Keine OSI-anerkannte Open-Source-Lizenz. Maßgeblich ist die englische LICENSE.

## Quellen und Urheberhinweise

Auf GitHub geprüfte Markdown-URL-Links verwenden; Wikilinks getrennt für vorhandene Obsidian-Notizen. Vor Weitergabe Herkunfts-URL, Revision, Lizenz, übernommene Dateien und Änderungen dokumentieren. Keine Quellenangaben oder Lizenzkompatibilität erfinden.

## Wiederverwendbare Projektvorlage

Die einfachen Metadaten in project-template/Proposal.md bearbeiten und mit new_project.py ein neues leeres Verzeichnis erzeugen. Der Generator erstellt kein Remote-Repository, pusht nicht, veröffentlicht nicht und implementiert keine Anwendung. Namen, E-Mail, URLs und Lizenz vor Veröffentlichung prüfen.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

## Lokale und entfernte Speicherung

Den vollständigen lokalen Klon und das private Remote behalten. Nach Prüfung committen und pushen; GitHub synchronisiert Dateien nicht automatisch. Ignorierte Einstellungen separat sichern. Doppelte ZIPs und entbehrliche Vorschauen entfernen, nicht Vorlagen oder Skripte.

## Veröffentlichung und Metadaten

Zuerst lokal ansehen. Öffentliche Bereitstellung und Sichtbarkeitsänderungen benötigen eine gesonderte Freigabe. Standard ist noindex. Die tatsächliche freigegebene HTTPS-URL angeben, um Canonical-, Open-Graph-, hreflang- und Sitemap-Angaben zu erzeugen. llms-Dateien garantieren keine Platzierung.

## Validierung und Grenzen

Vorlagenstruktur, Links, Datenschutzmuster, Paket und Seiteninteraktionen werden lokal geprüft. Die früheren isolierten Renderer-Tests für 1.7.1 waren erfolgreich. Reale Provider-Aufrufe, Speichern mit der Erweiterung und vollständige Tests auf Windows, macOS und Linux stehen noch aus.

Der Originalinhalt kann nur Auswahl oder Markierungen enthalten. Der KI-Kontext ist begrenzt. Clipper 1.7.1 kann wörtliche Vorlagenausdrücke in KI-Varianten erneut auswerten; dafür Archive ohne Interpreter verwenden. Automatisches Kopieren zwischen Vaults ist nicht implementiert.

Jede neue Datei braucht einen tatsächlichen Zweck, eine Datenklassifikation, gegebenenfalls Quellenangaben und passende Prüfungen. Notizen verwenden einfaches YAML; Code einen kurzen nützlichen Kopfkommentar. Kommentare erklären Gründe und Einschränkungen, statt Code zu wiederholen. Keine Tests oder Ergebnisse erfinden.

**Entwickelt von:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)
