# The JustShip Core

> El nombre lo dice todo 🚀

![Django CI](https://github.com/JustShip/justshipto_core/actions/workflows/django.yml/badge.svg)
![GitHub Repo stars](https://img.shields.io/github/stars/justship/justshipto_core)
[![GitNFT](https://img.shields.io/badge/%F0%9F%94%AE-Open%20in%20GitNFT-darkviolet?style=flat)](https://gitnft.quine.sh/app/commits/list/repo/justshipto_core)

![GitHub Sponsors](https://img.shields.io/github/sponsors/JustShip?logo=sponsors)
![GitHub](https://img.shields.io/github/license/justship/justshipto_core)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/JustShip/justshipto_core)
![GitHub last commit](https://img.shields.io/github/last-commit/JustShip/justshipto_core)
![GitHub contributors](https://img.shields.io/github/contributors/JustShip/justshipto_core)
![GitHub issues](https://img.shields.io/github/issues/justship/justshipto_core)
![GitHub repo size](https://img.shields.io/github/repo-size/justship/justshipto_core)

Núcleo de [Just Ship](https://justship.to).

Si deseas conocer sobre que va este proyecto te recomiendo que leas [este artículo](https://medium.com/justship/de-la-idea-al-producto-justship-fd5d9fd3ae83)
o visites nuestras [redes sociales](https://bio.link/justship).

## ¡Apoya este proyecto!
Este proyecto es de la comunidad para la comunidad. Si deseas contribuir monetariamente puedes hacerlo a través de [Ko-fi](https://ko-fi.com/justship),
[QvaPay](https://qvapay.com/payme/justshipto) o con cripto (ver en nuestra [web](https://justship.to)).

## Estructura de carpetas:

    .
    ├── apps                                # contiene todas las aplicaciones
    │   ├── accounts                        # aplicación para gestionar cuentas
    │   │   ├── api                         # contiene los GraphQL
    │   │   │  ├── mutations.py             # mutaciones de GraphQL
    │   │   │  ├── queries.py               # consultas de GraphQL
    │   │   │  ├── schema.py                # esquema de  GraphQL
    │   │   │  └── types.py                 # declaración de los tipos de modelos para GraphQL
    │   │   ├── management                  # comandos personalizados
    │   │   │   └── commands
    │   │   │       └── inituseradmin.py
    │   │   ├── migrations                  # migraciones
    │   │   ├── tests                       # carpeta contenedora de tests
    │   │   │   ├── test_api_mutations.py
    │   │   │   └── test_models.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── constants.py                # constantes
    │   │   ├── models.py                   # modelos de la BBDD
    │   │   ├── urls.py
    │   │   ├── utils.py                    # funciones útiles usadas por la aplicación accounts
    │   │   └── views.py
    │   ├── api                             # aplicación api
    │   │   ├── tests                       # contiene todos los tests de api
    │   │   ├── apps.py
    │   │   └── schema.py                   # llama a todos los esquemas de todas las aplicaciones
    │   ├── billing                         # aplicación de pagos
    │   │   ├── api                         # contiene los GraphQL
    │   │   │   ├── mutations.py            # mutaciones de GraphQL
    │   │   │   ├── queries.py              # consultas de GraphQL
    │   │   │   ├── schema.py               # esquema de  GraphQL
    │   │   │   └── types.py                # declaración de los tipos de modelos para GraphQL
    │   │   ├── migrations                  # migraciones
    │   │   ├── tests                       # test de la aplicación billing
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── constants.py                # constantes de la aplicación
    │   │   ├── models.py                   # modelos
    │   │   └── views.py
    │   ├── core                            # aplicación núcleo del proyecto
    │   │   ├── migrations                  # migraciones
    │   │   ├── tests                       # tests
    │   │   │   ├── test_forms.py
    │   │   │   ├── test_middleware.py
    │   │   │   ├── test_models.py
    │   │   │   ├── test_validators.py
    │   │   │   └── test_views.py
    │   │   ├── apps.py
    │   │   ├── middleware                  # middlewares del núcleo
    │   │   ├── models.py                   # modelos básicos que pueden ser usados por cualquier aplicación
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── mails                           # aplicación asíncrona para envíos de emails
    │   │   ├── migrations                  # migraciones
    │   │   ├── templates                   # plantillas de correos
    │   │   │   └── mails
    │   │   │       └── password_reset.html # plantilla de correo para reestablecer contraseña
    │   │   ├── tests                       # tests de la aplicación
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── constants.py                # constantes de la aplicación
    │   │   ├── models.py                   # modelos
    │   │   ├── recievers.py
    │   │   └── tasks.py                    # métodos asícronos con Celery
    │   ├── products                        # aplicación de productos
    │   │   ├── api                         # contiene los GraphQL
    │   │   │   ├── mutations.py            # mutaciones de GraphQL
    │   │   │   ├── queries.py              # consultas de GraphQL
    │   │   │   ├── schema.py               # esquema de  GraphQL
    │   │   │   └── types.py                # declaración de los tipos de modelos para GraphQL
    │   │   ├── migrations                  # migraciones Django
    │   │   ├── tests                       # tests de la aplicación
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── constants.py                # constantes
    │   │   ├── models.py                   # modelos
    │   │   └── views.py
    │   └── resources                       # aplicación de recursos
    │       ├── api                         # contiene los GraphQL
    │       │   ├── mutations.py            # mutaciones de GraphQL
    │       │   ├── queries.py              # consultas de GraphQL
    │       │   ├── schema.py               # esquema de  GraphQL
    │       │   └── types.py                # declaración de los tipos de modelos para GraphQL
    │       ├── migrations                  # migraciones Django
    │       ├── tests                       # tests de la aplicación
    │       ├── admin.py
    │       ├── apps.py
    │       ├── models.py                   # modelos
    │       └── views.py
    ├── config                              # Contiene todos los archivos de configuración
    │   ├── settings                        # Contiene la configuración
    │   │   ├── base.py                     # contiene las configuraciones base
    │   │   ├── develop.py                  # configuración específica para desarrollo
    │   │   ├── production.py               # configuración específica para producción
    │   │   └── staging.py                  # configuración específica para staging
    │   ├── asgi.py                         # configuración de despliegue asíncrono
    │   ├── celery
    │   ├── wsgi.py                         # configuración de despliegue
    │   └── urls.py                         # raíz de las url del proyecto
    ├── requirements                        # carpeta que contiene los requerimientos del proyecto
    │   ├── base.txt                        # requerimientos base
    │   ├── develop.txt                     # requerimientos para desarrollo
    │   ├── production.txt                  # requerimientos para producción
    │   ├── staging.txt                     # requerimientos para staging
    │   └── test.txt                        # requerimientos para testing
    ├──tests
    │  └── test_env_settings.py
    └── manage.py


## Ejecutar
Ejecutar el proyecto localmente

### Instalar dependencias
Para instalar las dependencias solo debe ejecutar:

    pip install -r requirements/develop.txt

### Instalar pre-commit
Instalar pre-commit para evitar posibles errores en el código antes del push

    pre-commit install

### Base de datos
Este proyecto en modo desarrollo usa SQlite por lo que solo tienes que ejecutar las migraciones:

    python manage.py migrate
Ejecutar celery:

    celery -A core.config worker -l INFO
Después creas un usuario administrador:

    python manage.py createsuperuser
Rellenas toda la información que te pide y ya está listo para ejecutar:

    python manage.py runserver
Abre tu navegador en http://localhost:8000 y verás el sitio ejecutándose


## Desplegar
Este proyecto está dockerizado por lo que solo se deben crear las variables de entorno y levantar el contenedor

### Variables de entorno
Crea un fichero `.env` en la raíz del proyecto y agrega estas variables de entorno:

- `SECRET_KEY` Firma criptográfica que usa Django para encriptar contraseñas y otros elementos de seguridad
- `DJANGO_ALLOWED_HOSTS` Dirección del host en la que se ejecuta
- `DJANGO_SETTINGS_MODULE` Solo necesario en producción. Dirección del módulo de configuración (`config.settings.develop`)
- `DB_NAME` nombre de la base de datos
- `DB_HOST` dirección del host de la base de datos
- `DB_USER` nombre de usuario de la base de datos
- `DB_PASSWORD` contraseña de la base de datos
- `EMAIL_HOST` dirección del host email con el que se va a enviar correos electrónicos
- `EMAIL_PORT` puerto del host email con el que se va a enviar correos electrónicos
- `EMAIL_HOST_USER` dirección de correo del email con el que se va a enviar correos electrónicos
- `EMAIL_HOST_PASSWORD` contraseña de correo del email con el que se va a enviar correos electrónicos
- `EMAIL_USE_TLS` boolean que indica si se va a usar el correo sobre TLS o no
- `GOOGLE_RECAPTCHA_PRIVATE_KEY` llave privada de [Google Recaptcha](https://www.google.com/recaptcha/admin/)

### Ejecutar Docker
Para crear la imagen de Docker:

     docker-compose build --tag justshipto_core:1.0 .

Para crear y correr la imagen de docker:

    docker-compose up  # para ejecutarlo en segundo plano hay que agregar -d

Para detener la imagen de docker:

    docker-compose down

Para hacer despliegue rápido:

    ./build.sh

## Contribuidores:

## Licencia:

[GPL-3.0](LICENSE)

## Guía de contribución

Si desea contribuir con el proyecto por favor, lea nuestra [Guía de contribución](CONTRIBUTING.md)

## Código de conducta

[Código de conducta](CODE_OF_CONDUCT.md)
