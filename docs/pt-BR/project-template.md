# Modelo reutilizável de projeto

[Guia do projeto](guide.md)

Edite o frontmatter simples de project-template/Proposal.md. Gere uma pasta nova e vazia com new_project.py. O gerador não cria remoto, não envia commits, não publica site e não implementa a aplicação. Revise nome, contato, URLs e licença antes de publicar.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

Cada arquivo novo deve indicar função real, classificação dos dados, fonte quando aplicável e validação relevante. Notas usam YAML simples; código usa um cabeçalho útil e curto. Comentários explicam motivos e restrições, sem repetir o código. Não invente testes ou resultados.

O gerador copia apenas campos públicos, não o texto bruto da proposta. Acrescente o escopo revisado ao Proposal.md gerado. A atribuição deve corresponder à política aprovada; os idiomas seguem os arquivos entregues.
