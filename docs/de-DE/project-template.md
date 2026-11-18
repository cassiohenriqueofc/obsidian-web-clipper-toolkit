# Wiederverwendbare Projektvorlage

[Projektleitfaden](guide.md)

Die einfachen Metadaten in project-template/Proposal.md bearbeiten und mit new_project.py ein neues leeres Verzeichnis erzeugen. Der Generator erstellt kein Remote-Repository, pusht nicht, veröffentlicht nicht und implementiert keine Anwendung. Namen, E-Mail, URLs und Lizenz vor Veröffentlichung prüfen.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

Jede neue Datei braucht einen tatsächlichen Zweck, eine Datenklassifikation, gegebenenfalls Quellenangaben und passende Prüfungen. Notizen verwenden einfaches YAML; Code einen kurzen nützlichen Kopfkommentar. Kommentare erklären Gründe und Einschränkungen, statt Code zu wiederholen. Keine Tests oder Ergebnisse erfinden.

Der Generator übernimmt nur öffentliche Felder, nicht den Rohtext des Vorschlags. Ergänzen Sie den geprüften Umfang in der erzeugten Proposal.md. Öffentliche Angaben müssen der freigegebenen Richtlinie entsprechen; Sprachen folgen den gelieferten Dateien.
