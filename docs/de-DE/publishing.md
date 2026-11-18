# Veröffentlichung und Metadaten

Zuerst lokal ansehen. Öffentliche Bereitstellung und Sichtbarkeitsänderungen benötigen eine gesonderte Freigabe. Standard ist noindex. Die tatsächliche freigegebene HTTPS-URL angeben, um Canonical-, Open-Graph-, hreflang- und Sitemap-Angaben zu erzeugen. llms-Dateien garantieren keine Platzierung.

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Demodaten verwenden. Lokale Einstellungen, Zugangsdaten, private Notizen und persönliche Pfade ausschließen. Ein privates Repository schützt kein bereits eingechecktes Geheimnis. Der Rechteinhaber hat nur die unten genannte öffentliche Zuordnung genehmigt.

[Projektleitfaden](guide.md)

Das README ist gerendertes Markdown; Open-Graph-, Twitter-, Canonical- und JSON-LD-
Metadaten gehören zur generierten Website. Das kompakte Vorschaubild liegt unter
[assets/social-preview.jpg](../../assets/social-preview.jpg). Bei Bedarf kann es
unter GitHub Settings → Social preview hochgeladen werden. GitHub-Themennamen sind
auch bei privaten Repositories öffentlich; erst nach Freigabe hinzufügen. Google
bestätigt, dass llms.txt die Sichtbarkeit und das Ranking in Google Search nicht
verändert und keine besondere Schema.org-Auszeichnung für die KI-Suche erforderlich ist.
