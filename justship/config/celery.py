import os
from dotenv import load_dotenv
from celery import Celery

load_dotenv()

# Set the default Django settings module for the 'celery' program.
if os.getenv('ENV') == 'develop':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justship.config.settings.develop')

elif os.getenv('ENV') == 'staging':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justship.config.settings.staging')

elif os.getenv('ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justship.config.settings.production')

# Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('justship')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
