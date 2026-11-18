# Reusable project starter

[Project guide](guide.md)

Edit the flat frontmatter in project-template/Proposal.md. Render a new, empty directory using new_project.py. The generator never creates a remote, pushes, deploys, or implements the application. Review names, email, URLs and license before publishing.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

For each new file, state its real purpose, data classification, source credit when applicable, and meaningful validation. Notes use flat YAML; source files use a short useful header; comments explain reasons and constraints instead of repeating code. Never invent tests or results.
