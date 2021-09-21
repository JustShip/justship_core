# The JustShip Core
Núcleo de [Just Ship](https://justship.to).

## Apoya este proyecto!
Este proyecto es de la comunidad para la comunidad

## Estructura de carpetas:

    .
    ├── config                      # Contiene todos los archivos de configuración
    │   ├── settings                # Contiene la configuración
    │   │   ├── base.py             # contiene las configuraciones base
    │   │   ├── develop.py          # configuración específica para desarrollo
    │   │   ├── production.py       # configuración específica para producción
    │   │   └── staging.py          # configuración específica para staging
    │   ├── asgi.py                 # configuración de despliegue asíncrono
    │   ├── wsgi.py                 # configuración de despliegue
    │   └── urls.py                 # raíz de las url del proyecto
    ├── justship_core               # carpeta contenedora de aplicaciones
    │   ├── accounts                # aplicación para gestionar cuentas
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py           # modelos
    │   │   └── views.py            # vistas
    │   └── core                    # aplicación núcleo del proyecto
    │   │   ├── apps.py             
    │   │   ├── middleware.py       # middlewares del núcleo
    │   │   ├── models.py           # modelos básicos que pueden ser usados por cualquier aplicación
    │   │   └── views.py
    ├── requirements                # carpeta que contiene los requerimientos del proyecto
    │   ├── base.txt                # requerimientos base
    │   ├── develop.txt             # requerimientos para desarrollo
    │   ├── production.txt          # requerimientos para producción
    │   ├── staging.txt             # requerimientos para staging
    │   └── test.txt                # requerimientos para testing
    └── manage.py                   



## Ejecutar
Ejecutar el proyecto localmente
### Instalar dependencias
Para instalar las dependencias solo debe ejecutar:

    pip install -r requirements/develop.txt

### Base de datos
Este proyecto en modo desarrollo usa SQlite por lo que solo tienes que ejecutar las migraciones:

    python manage.py migrate
Después creas un usuario administrador:

    python manage.py createsuperuser
Rellenas toda la información que te pide y ya está listo para ejecutar:

    python manage.py runserver
Abre tu navegador en http://localhost:8000 y verás el sitio ejecutándose


## Desplegar
TODO (Dockerizar)

## Contribuidores:

