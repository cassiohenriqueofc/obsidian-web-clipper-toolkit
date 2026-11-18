[English (US)](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español (Argentina)](README.es-AR.md) · [Español (México)](README.es-MX.md) · [Español (España)](README.es-ES.md) · [Deutsch](README.de-DE.md) · [Français](README.fr-FR.md)

![Web → Notes](assets/banner.png)

# Obsidian Web Clipper Toolkit


[Instalación](docs/es-ES/install.md) · [Plantillas](templates/) · [Mapa de prompts](docs/es-ES/prompt-map.md) · [Ejemplos](examples/) · [Licencia](LICENSE)

Actualizado: 2026-11-18 · 0.1.1 · Versión privada para revisión

## Resumen

Plantillas reutilizables de Web Clipper con interpretación manual y conservación de la fuente.

Utiliza JSON y Markdown portables, revisa las sugerencias del modelo, conserva las evidencias y mantén una alternativa sin IA.

## Entregas

| Template | Prompts | Source |
| --- | --- | --- |
| [Balanced](templates/01-balanced-original-callout-clipper.json) | 6 | Callout |
| [Compact](templates/02-compact-original-footer-clipper.json) | 4 | Footer |
| [Archive](templates/03-source-archive-clipper.json) | 0 | Callout |

## Instalación

Instala Obsidian y Web Clipper oficial en un navegador compatible. Crea la carpeta de la bóveda, importa una plantilla y comprueba la bóveda y el destino. Desactiva la ejecución automática. Con IA, pulsa manualmente Interpret, revisa y guarda. En Archive no ejecutes Interpreter.

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


## Plantilla reutilizable de proyecto

Edita los metadatos simples de project-template/Proposal.md y genera una carpeta nueva y vacía con new_project.py. El generador no crea remotos, no hace push, no publica ni implementa la aplicación. Revisa nombres, correo, URL y licencia antes de compartir.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```


## Almacenamiento local y remoto

Conserva el clon local completo y el remoto privado. Haz commit y push tras revisar; GitHub no sincroniza archivos automáticamente. Guarda aparte una copia de seguridad de los ajustes excluidos. Para ahorrar espacio, elimina ZIP duplicados y vistas desechables, no fuentes ni scripts.

## Privacidad

Utiliza datos de demostración. Excluye configuraciones locales, credenciales, notas privadas y rutas personales. Un repositorio privado no protege un secreto incorporado al historial. El titular ha autorizado únicamente la atribución indicada abajo.

## Validación y límites

Se comprueban localmente estructura, enlaces, patrones de privacidad, paquete e interacciones del sitio. Pasaron las pruebas aisladas anteriores del renderizador 1.7.1. Faltan proveedor real, guardado desde la extensión y pruebas completas en Windows, macOS y Linux.

El contenido original puede ser una selección o destacados. El contexto de IA tiene límites. Clipper 1.7.1 puede reprocesar expresiones literales en variantes con IA; utiliza Archive sin Interpreter si afecta a la fuente. No hay copia automática entre bóvedas.

## Licencia

Licencia de código disponible para uso no comercial. El uso comercial requiere un permiso separado. Las versiones modificadas compartidas deben incluir código correspondiente, atribución, la misma licencia y un registro fechado. No exige publicar cambios privados. No es código abierto aprobado por OSI. La LICENSE inglesa es la válida.

[Guía del proyecto](docs/es-ES/guide.md) · [LICENSE](LICENSE) · [CHANGELOG](CHANGELOG.md)

**Desarrollado por:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)

<details>
<summary>Animated workflow / Fluxo animado</summary>

![Page to template, manual interpretation, source-preserving Markdown and private Git versions](assets/workflow.gif)

</details>
