# Plantilla reutilizable de proyecto

[Guía del proyecto](guide.md)

Edita los metadatos simples de project-template/Proposal.md y genera una carpeta nueva y vacía con new_project.py. El generador no crea remotos, no hace push, no publica ni implementa la aplicación. Revisa nombres, correo, URL y licencia antes de compartir.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

Cada archivo nuevo debe indicar su función real, clasificación de datos, fuentes aplicables y validación relevante. Las notas usan YAML simple; el código lleva un encabezado breve y útil. Los comentarios explican motivos y restricciones, sin repetir código. No inventes pruebas ni resultados.

El generador copia solo campos públicos, no el cuerpo original de la propuesta. Añade el alcance revisado al Proposal.md generado. La atribución debe coincidir con la política aprobada; los idiomas se derivan de los archivos entregados.
