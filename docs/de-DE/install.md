# Installation

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

Demodaten verwenden. Lokale Einstellungen, Zugangsdaten, private Notizen und persönliche Pfade ausschließen. Ein privates Repository schützt kein bereits eingechecktes Geheimnis. Der Rechteinhaber hat nur die unten genannte öffentliche Zuordnung genehmigt.

Der Originalinhalt kann nur Auswahl oder Markierungen enthalten. Der KI-Kontext ist begrenzt. Clipper 1.7.1 kann wörtliche Vorlagenausdrücke in KI-Varianten erneut auswerten; dafür Archive ohne Interpreter verwenden. Automatisches Kopieren zwischen Vaults ist nicht implementiert.

[Projektleitfaden](guide.md)
