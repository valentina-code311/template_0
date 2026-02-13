# Plantilla Copier

Este repositorio contiene una plantilla para generar proyectos con [Copier](https://copier.readthedocs.io/).

## Estructura

- `copier.yml`: configuración y preguntas de la plantilla.
- `template/`: archivos que se renderizan al crear un nuevo proyecto.
- `scripts/`: scripts auxiliares ejecutados desde los tasks de Copier.

## Uso rápido

```bash
copier copy . ../mi-proyecto
```

## Tasks de Copier

La plantilla ejecuta tasks definidos en `copier.yml` para realizar acciones posteriores a la generación del proyecto.

Actualmente se usa el script:

- `scripts/post_copy_message.sh`: muestra un resumen después de crear el proyecto.
