# Guía del proyecto

[English (US)](../en-US/guide.md) · [Português (Brasil)](../pt-BR/guide.md) · [Español (Argentina)](../es-AR/guide.md) · [Español (México)](../es-MX/guide.md) · [Español (España)](../es-ES/guide.md) · [Deutsch](../de-DE/guide.md) · [Français](../fr-FR/guide.md)

Actualizado: 2026-11-18 · 0.1.3 · Versión pública · GitHub Pages configurado

## Objetivo

Usá JSON y Markdown portables, revisá las sugerencias del modelo, conservá la evidencia y mantené una alternativa sin IA.

## Instalación

Instalá Obsidian y Web Clipper oficial en un navegador compatible. Creá la carpeta de la bóveda, importá una plantilla y verificá la bóveda y el destino. Dejá desactivada la ejecución automática. Con IA, hacé clic manualmente en Interpret, revisá y guardá. En Archive no ejecutes Interpreter.

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

## Desarrollo

Para proyectos, usá un clon Git local y un repositorio privado en GitHub. Trabajá con ramas, commits concretos, revisión de cambios y registro fechado. No crees repositorios para tareas cotidianas o conversaciones simples.

## Privacidad

Usá datos de demostración. Excluí configuraciones locales, credenciales, notas privadas y rutas personales. Un repositorio privado no protege un secreto ya incorporado al historial. El titular autorizó únicamente la atribución indicada abajo.

## Licencia

Licencia de código disponible para uso no comercial. El uso comercial requiere permiso separado. Las versiones modificadas compartidas deben incluir código correspondiente, atribución, la misma licencia y un registro fechado. No exige publicar cambios privados. No es código abierto aprobado por OSI. La LICENSE inglesa es la válida.

## Fuentes y atribución

Usá enlaces Markdown con URL verificadas en GitHub y wikilinks separados para notas existentes de Obsidian. Registrá URL de origen, revisión, licencia, archivos reutilizados y cambios. No inventes créditos ni compatibilidad entre licencias.

## Plantilla reutilizable de proyecto

Editá los metadatos simples de project-template/Proposal.md y generá una carpeta nueva y vacía con new_project.py. El generador no crea repositorios remotos, no hace push, no publica ni implementa la aplicación. Revisá nombres, correo, URL y licencia antes de compartir.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

## Almacenamiento local y remoto

Conservá el clon local completo y el remoto privado. Hacé commit y push después de revisar; GitHub no sincroniza archivos automáticamente. Respaldá por separado los ajustes excluidos. Para ahorrar espacio, borrá ZIP duplicados y vistas descartables, no fuentes ni scripts.

## Publicación y metadatos

El workflow de GitHub Pages está configurado para https://cassiohenriqueofc.github.io/obsidian-web-clipper-toolkit/. La primera ejecución debe terminar antes de considerar el sitio publicado. La versión publicada usa canonical, Open Graph/Twitter, hreflang, JSON-LD, sitemap y robots indexable. Los archivos llms no garantizan posicionamiento.

## Validación y límites

Se verifican localmente estructura, enlaces, patrones de privacidad, paquete e interacciones del sitio. Pasaron las pruebas aisladas anteriores del renderizador 1.7.1. Faltan proveedor real, guardado desde la extensión y pruebas completas en Windows, macOS y Linux.

El contenido original puede ser una selección o destacados. El contexto de IA tiene límites. Clipper 1.7.1 puede reprocesar expresiones literales en variantes con IA; usá Archive sin Interpreter si afecta la fuente. No hay copia automática entre bóvedas.

Cada archivo nuevo debe indicar su función real, clasificación de datos, fuentes aplicables y validación relevante. Las notas usan YAML simple; el código lleva un encabezado breve y útil. Los comentarios explican motivos y restricciones, sin repetir código. No inventes pruebas ni resultados.

**Desarrollado por:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)
