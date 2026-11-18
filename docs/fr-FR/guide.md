# Guide du projet

[English (US)](../en-US/guide.md) · [Português (Brasil)](../pt-BR/guide.md) · [Español (Argentina)](../es-AR/guide.md) · [Español (México)](../es-MX/guide.md) · [Español (España)](../es-ES/guide.md) · [Deutsch](../de-DE/guide.md) · [Français](../fr-FR/guide.md)

Mis à jour: 2026-11-18 · 0.1.2 · Version privée à vérifier

## Objectif

Utilisez des fichiers JSON et Markdown portables, vérifiez les suggestions du modèle, conservez les preuves et gardez une solution sans IA.

## Installation

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

## Développement

Pour les projets, utilisez un clone Git local et un dépôt GitHub privé. Travaillez avec des branches, des commits factuels, une revue des différences et un journal daté. Ne créez pas de dépôt pour les tâches courantes ou les conversations simples.

## Confidentialité

Utilisez des données de démonstration. Excluez paramètres locaux, identifiants, notes privées et chemins personnels. Un dépôt privé ne protège pas un secret déjà enregistré dans l’historique. Le titulaire a autorisé uniquement l’attribution indiquée ci-dessous.

## Licence

Licence à code source disponible, réservée à un usage non commercial. L’usage commercial nécessite une autorisation distincte. Les versions modifiées partagées doivent fournir les sources correspondantes, l’attribution, la même licence et un journal daté. Les modifications privées ne doivent pas être publiées. Ce n’est pas une licence open source approuvée par l’OSI. La LICENSE anglaise fait foi.

## Sources et attribution

Utilisez des liens Markdown vers des URL vérifiées sur GitHub et des wikiliens distincts pour les notes Obsidian existantes. Documentez URL d’origine, révision, licence, fichiers repris et modifications avant diffusion. N’inventez ni crédits ni compatibilité des licences.

## Modèle de projet réutilisable

Modifiez les métadonnées simples de project-template/Proposal.md puis générez un nouveau dossier vide avec new_project.py. Le générateur ne crée pas de dépôt distant, ne pousse rien, ne publie pas et n’implémente pas l’application. Vérifiez noms, courriel, URL et licence avant diffusion.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

## Stockage local et distant

Conservez le clone local complet et le dépôt distant privé. Faites commit et push après vérification ; GitHub ne synchronise pas les fichiers automatiquement. Sauvegardez séparément les paramètres ignorés. Supprimez les ZIP en double et les aperçus jetables, pas les sources ni les scripts.

## Publication et métadonnées

Prévisualisez localement. La publication et les changements de visibilité demandent une approbation distincte. Le site utilise noindex par défaut. Indiquez l’URL HTTPS réelle et approuvée pour générer canonical, Open Graph, hreflang et sitemap. Les fichiers llms ne garantissent aucun classement.

## Validation et limites

Structure, liens, motifs de confidentialité, paquet et interactions du site sont vérifiés localement. Les précédents tests isolés du moteur 1.7.1 ont réussi. Les appels réels au fournisseur, l’enregistrement par l’extension et les tests complets Windows, macOS et Linux restent à effectuer.

Le contenu original peut être une sélection ou des passages surlignés. Le contexte IA est limité. Clipper 1.7.1 peut réévaluer des expressions littérales dans les variantes IA ; utilisez Archive sans Interpreter si nécessaire. La copie automatique entre coffres n’est pas implémentée.

Chaque nouveau fichier doit préciser son rôle réel, sa classification des données, ses sources pertinentes et ses vérifications utiles. Les notes utilisent un YAML simple ; le code un en-tête bref et utile. Les commentaires expliquent raisons et contraintes sans répéter le code. N’inventez ni tests ni résultats.

**Développé par:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)
