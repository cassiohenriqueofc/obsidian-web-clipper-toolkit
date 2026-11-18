# Plantilla reutilizable de proyecto

[Guía del proyecto](guide.md)

Editá los metadatos simples de project-template/Proposal.md y generá una carpeta nueva y vacía con new_project.py. El generador no crea repositorios remotos, no hace push, no publica ni implementa la aplicación. Revisá nombres, correo, URL y licencia antes de compartir.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

Cada archivo nuevo debe indicar su función real, clasificación de datos, fuentes aplicables y validación relevante. Las notas usan YAML simple; el código lleva un encabezado breve y útil. Los comentarios explican motivos y restricciones, sin repetir código. No inventes pruebas ni resultados.
