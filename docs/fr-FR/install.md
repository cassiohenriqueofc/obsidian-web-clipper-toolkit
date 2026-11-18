# Installation

Installez Obsidian et Web Clipper officiel dans un navigateur compatible. Créez le dossier du coffre, importez un modèle et vérifiez le coffre et la destination. Désactivez l’exécution automatique. Avec l’IA, lancez Interpret manuellement, vérifiez puis enregistrez. Pour Archive, ne lancez pas Interpreter.

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

Utilisez des données de démonstration. Excluez paramètres locaux, identifiants, notes privées et chemins personnels. Un dépôt privé ne protège pas un secret déjà enregistré dans l’historique. Le titulaire a autorisé uniquement l’attribution indiquée ci-dessous.

Le contenu original peut être une sélection ou des passages surlignés. Le contexte IA est limité. Clipper 1.7.1 peut réévaluer des expressions littérales dans les variantes IA ; utilisez Archive sans Interpreter si nécessaire. La copie automatique entre coffres n’est pas implémentée.

[Guide du projet](guide.md)
