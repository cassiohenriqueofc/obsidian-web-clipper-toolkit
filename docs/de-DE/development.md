# Entwicklung

Für Projekte einen lokalen Git-Klon und ein privates GitHub-Repository verwenden. Mit Branches, sachlichen Commits, geprüften Änderungen und datiertem Änderungsprotokoll arbeiten. Für Alltagsaufgaben oder einfache Chats kein Repository anlegen.

```bash
git clone https://github.com/cassiohenriqueofc/obsidian-web-clipper-toolkit.git obsidian-web-clipper-git
cd obsidian-web-clipper-git
git switch -c feat/describe-change
python3 scripts/validate.py
git diff
git add CHANGELOG.md
git diff --cached
git commit -m "docs: describe the verified change"
git push -u origin feat/describe-change
```

Den vollständigen lokalen Klon und das private Remote behalten. Nach Prüfung committen und pushen; GitHub synchronisiert Dateien nicht automatisch. Ignorierte Einstellungen separat sichern. Doppelte ZIPs und entbehrliche Vorschauen entfernen, nicht Vorlagen oder Skripte.

[Projektleitfaden](guide.md)
