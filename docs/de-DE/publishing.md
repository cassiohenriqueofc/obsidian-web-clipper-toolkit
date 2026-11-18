# Veröffentlichung und Metadaten

Zuerst lokal ansehen. Öffentliche Bereitstellung und Sichtbarkeitsänderungen benötigen eine gesonderte Freigabe. Standard ist noindex. Die tatsächliche freigegebene HTTPS-URL angeben, um Canonical-, Open-Graph-, hreflang- und Sitemap-Angaben zu erzeugen. llms-Dateien garantieren keine Platzierung.

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Demodaten verwenden. Lokale Einstellungen, Zugangsdaten, private Notizen und persönliche Pfade ausschließen. Ein privates Repository schützt kein bereits eingechecktes Geheimnis. Der Rechteinhaber hat nur die unten genannte öffentliche Zuordnung genehmigt.

[Projektleitfaden](guide.md)
