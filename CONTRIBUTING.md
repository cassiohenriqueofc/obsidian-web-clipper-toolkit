# Contributing / Como contribuir

**English:** Use a feature branch and a descriptive commit for each coherent
change. Run validation, inspect the staged diff for private data, update the
change log, then open a pull request. Contributions are accepted under LICENSE;
by submitting, you confirm you have the rights to grant those terms. Do not upload
private vault notes, personal settings exports, real credentials, or user-specific
filesystem paths. Use demo data. Do not run paid provider tests without approval.

**Português:** Use uma branch, commits descritivos, validação e revisão do diff.
Atualize o changelog e abra um pull request. Ao contribuir, você confirma que tem
os direitos necessários para aplicar a LICENSE. Não envie dados pessoais,
exportações reais ou credenciais. Use dados demonstrativos.

```bash
git switch -c feature/describe-your-change
python3 scripts/validate.py
git diff
git add templates docs scripts README.md README.pt-BR.md CHANGELOG.md
git diff --cached
git commit -m "feat: describe the observable improvement"
git push -u origin feature/describe-your-change
```

On Windows use py -3 instead of python3. Do not use force-push on main. Do not
commit local-only, private, dist, .env files, or settings backups. Select explicit
paths rather than adding the entire workspace blindly.

## Required review

- Preserve manual Interpreter behavior and full supplied content.
- Keep template prompts English and docs multilingual where relevant.
- Prefix callout/code lines once; keep interactive checkboxes outside fences.
- Record validation limits rather than claiming unperformed tests.
- Disclose evidence limits and preserve the no-AI fallback.
- Distributed modified versions need a dated change log and corresponding source.
