# Project working rules

Read Proposal.md when present, handoff.md, CHANGELOG.md, and the relevant docs
before making changes. Use only facts supported by the repository or verified
sources. Follow the user's explicit task and approval boundaries.

- This is project work: prefer a local Git clone and a private GitHub repository.
  Do not create repositories for ordinary chat or small everyday tasks.
- Do not change repository visibility, deploy publicly, or run paid provider
  requests without explicit authorization. A private release is not public hosting.
- Keep owner-specific settings in ignored local-only/. Never add settings exports,
  credentials, private notes or personal paths. Only attribution explicitly allowed
  by .privacy-policy.json may be included as public identity.
- Use demo data in examples. Inspect diffs and run python3 scripts/validate.py.
- Write concise factual docs, code comments, commits and PR descriptions. No filler,
  invented benchmarks, unsupported claims, false test results or guessed URLs.
- Preserve upstream licenses and credits; document actual modifications.
- Use coherent commits, feature branches, and pull requests. Never force-push main.
- Preserve manual Interpreter operation, full supplied source, English prompts,
  single structural quote prefixes, and tasks outside fences.
- Update relevant en-US, pt-BR, es-AR, es-MX, es-ES, de-DE and fr-FR documentation.
- Report what changed, what was checked, and material remaining limits.

Portable defaults: aimemory/project-defaults.md. This file does not create
account-wide persistence beyond repositories or conversations where it is loaded.
