# Instalación

Instala Obsidian y Web Clipper oficial en un navegador compatible. Crea la carpeta de la bóveda, importa una plantilla y revisa la bóveda y el destino. Desactiva la ejecución automática. Con IA, haz clic manualmente en Interpret, revisa y guarda. En Archive no ejecutes Interpreter.

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

Usa datos de demostración. Excluye configuraciones locales, credenciales, notas privadas y rutas personales. Un repositorio privado no protege un secreto incorporado al historial. El titular autorizó únicamente la atribución indicada abajo.

El contenido original puede ser una selección o destacados. El contexto de IA tiene límites. Clipper 1.7.1 puede reprocesar expresiones literales en variantes con IA; usa Archive sin Interpreter si afecta la fuente. No hay copia automática entre bóvedas.

[Guía del proyecto](guide.md)
