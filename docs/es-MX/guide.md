# Guía del proyecto

[English (US)](../en-US/guide.md) · [Português (Brasil)](../pt-BR/guide.md) · [Español (Argentina)](../es-AR/guide.md) · [Español (México)](../es-MX/guide.md) · [Español (España)](../es-ES/guide.md) · [Deutsch](../de-DE/guide.md) · [Français](../fr-FR/guide.md)

Actualizado: 2026-11-18 · 0.1.2 · Versión privada para revisión

## Objetivo

Usa JSON y Markdown portables, revisa las sugerencias del modelo, conserva la evidencia y mantén una alternativa sin IA.

## Instalación

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

## Desarrollo

Para proyectos, usa un clon Git local y un repositorio privado en GitHub. Trabaja con ramas, commits concretos, revisión de cambios y registro fechado. No crees repositorios para tareas cotidianas o conversaciones sencillas.

## Privacidad

Usa datos de demostración. Excluye configuraciones locales, credenciales, notas privadas y rutas personales. Un repositorio privado no protege un secreto incorporado al historial. El titular autorizó únicamente la atribución indicada abajo.

## Licencia

Licencia de código disponible para uso no comercial. El uso comercial requiere permiso separado. Las versiones modificadas compartidas deben incluir código correspondiente, atribución, la misma licencia y un registro fechado. No exige publicar cambios privados. No es código abierto aprobado por OSI. La LICENSE inglesa es la válida.

## Fuentes y atribución

Usa enlaces Markdown con URL verificadas en GitHub y wikilinks separados para notas existentes de Obsidian. Registra URL de origen, revisión, licencia, archivos reutilizados y cambios. No inventes créditos ni compatibilidad entre licencias.

## Plantilla reutilizable de proyecto

Edita los metadatos simples de project-template/Proposal.md y genera una carpeta nueva y vacía con new_project.py. El generador no crea remotos, no hace push, no publica ni implementa la aplicación. Revisa nombres, correo, URL y licencia antes de compartir.

```powershell
py -3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

```bash
python3 scripts/new_project.py --proposal project-template/Proposal.md --output local-only/new-project
```

## Almacenamiento local y remoto

Conserva el clon local completo y el remoto privado. Haz commit y push después de revisar; GitHub no sincroniza archivos automáticamente. Respalda por separado los ajustes excluidos. Para ahorrar espacio, elimina ZIP duplicados y vistas descartables, no fuentes ni scripts.

## Publicación y metadatos

Revisa la vista local primero. Publicar y cambiar la visibilidad requiere aprobación separada. El sitio usa noindex por defecto. Indica la URL HTTPS real y aprobada para generar canonical, Open Graph, hreflang y sitemap. Los archivos llms no garantizan posicionamiento.

## Validación y límites

Se verifican localmente estructura, enlaces, patrones de privacidad, paquete e interacciones del sitio. Pasaron las pruebas aisladas anteriores del renderizador 1.7.1. Faltan proveedor real, guardado desde la extensión y pruebas completas en Windows, macOS y Linux.

El contenido original puede ser una selección o destacados. El contexto de IA tiene límites. Clipper 1.7.1 puede reprocesar expresiones literales en variantes con IA; usa Archive sin Interpreter si afecta la fuente. No hay copia automática entre bóvedas.

Cada archivo nuevo debe indicar su función real, clasificación de datos, fuentes aplicables y validación relevante. Las notas usan YAML simple; el código lleva un encabezado breve y útil. Los comentarios explican motivos y restricciones, sin repetir código. No inventes pruebas ni resultados.

**Desarrollado por:** Cassio Henrique · Múltipla Tecnologia · [cassiohenriqueofc@gmail.com](mailto:cassiohenriqueofc@gmail.com)
