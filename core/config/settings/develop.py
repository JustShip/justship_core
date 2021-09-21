"""
This is the settings file that you use when you're working on the project locally.
Local development-specific include DEBUG mode, log level, and activation of developer tools like django-debug-toolsbar
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production.py secret!
SECRET_KEY = 'django-insecure-z^onbry)(r7-o6ej1hr&h=y3pxrqqq^3+@#uha!x)+a9rhhe)m'

# SECURITY WARNING: don't run with debug turned on in production.py!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
