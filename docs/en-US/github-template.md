# GitHub Template repository and clean scaffolds

The owner requested reusable defaults for projects, not ordinary chats or tasks.
This repo includes a clean Proposal-based scaffold and AGENTS instructions.

## Template setting

The repository Template flag is verified as enabled and visibility remains private.
An owner can inspect it under Settings → General → Template repository.
A private template remains subject to GitHub access rules.

With the setting enabled, GitHub's Use this template copies the whole repository,
including the toolkit. For a clean unrelated project, prefer the generator:

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

Edit Proposal.md first. Null repository/landing-page URLs remain absent in the
generated JSON-LD. Review public attribution, source credits and the selected
license. The generator refuses a nonempty destination and does not create a repo.

After reviewing the generated project, create a separate private repository only
when you have chosen its name and authorized that action. Do not run git init or
add another origin inside the existing clone. New projects should retain upstream
starter attribution and honor its noncommercial license.

## File-level templates

- README.md.tmpl and six localized README templates.
- LICENSE.md.tmpl, LICENCE.md.tmpl, and .gitignore.tmpl.
- note.md.tmpl with flat YAML and single-prefix callouts.
- source.py.tmpl with role, contract, data and attribution guidance.
- THIRD_PARTY_NOTICES.md.tmpl, CHANGELOG.md.tmpl and AGENTS.md.tmpl.

Templates are starting contracts, not proof that code works or reused material is
licensed. Never fill missing results, source credits or URLs with invented facts.

The generator accepts public author/company/contact values only from the explicitly approved attribution policy. Raw Proposal body text is not copied automatically; add reviewed scope to the generated Proposal.md manually. Generated language metadata follows the README files actually delivered.
