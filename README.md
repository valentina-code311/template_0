# Project Template

Una plantilla de [Copier](https://copier.readthedocs.io/) para inicializar proyectos con GitLab CI/CD preconfigurado.

## Características

Esta plantilla genera un proyecto con:

- **Configuración de GitLab CI/CD** con pipeline básico:
  - Etapa de lint
  - Etapa de test
  - Etapa de build
  - Etapa de deploy (manual)
- **Archivo .gitignore** completo con patrones comunes para:
  - Archivos del sistema operativo
  - Editores de código
  - Variables de entorno
  - Logs
  - Dependencias (Node.js, Python)
  - Archivos de build
  - Cobertura de código
- **README.md** base con información del proyecto y autor

## Requisitos

- [Copier](https://copier.readthedocs.io/) instalado
- Python 3.7+ (requerido por Copier)

## Instalación de Copier

```bash
# Con pip
pip install copier

# O con pipx (recomendado)
pipx install copier
```

## Uso

### Crear un nuevo proyecto

```bash
copier copy https://github.com/tu-usuario/template_0.git mi-nuevo-proyecto
```

O si estás trabajando localmente:

```bash
copier copy . /ruta/destino/mi-nuevo-proyecto
```

### Durante la creación

El generador te pedirá la siguiente información:

- **Nombre del proyecto**: Nombre legible del proyecto
- **Slug del proyecto**: Versión normalizada del nombre (se genera automáticamente)
- **Descripción del proyecto**: Descripción breve (opcional)
- **Nombre del autor**: Tu nombre completo
- **Email del autor**: Tu dirección de email

### Actualizar un proyecto existente

Si la plantilla se actualiza, puedes actualizar tu proyecto:

```bash
cd mi-proyecto
copier update
```

## Estructura generada

```
mi-nuevo-proyecto/
├── .copier-answers.yml    # Respuestas guardadas para futuras actualizaciones
├── .gitignore             # Patrones de archivos a ignorar en Git
├── .gitlab-ci.yml         # Pipeline de GitLab CI/CD
└── README.md              # Documentación del proyecto
```

## Personalización

Puedes personalizar esta plantilla modificando:

- `copier.yml`: Agregar o modificar preguntas
- `template/`: Agregar o modificar archivos de plantilla
- Usar sintaxis Jinja2 para hacer los archivos dinámicos

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

[Especifica tu licencia aquí]

## Autor

[Tu nombre]
