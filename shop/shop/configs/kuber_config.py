import os

SECRET_KEY = os.environ.get('SECRET_KEY', '__SECRET_KEY__')
DEBUG = True
SSL = True
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '__ALLOWED_HOSTS__')]
API_VERSION = 'v1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', '__DB_NAME__'),
        'USER': os.environ.get('DB_USER', '__DB_USER__'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '__DB_PASSWORD__'),
        'HOST': os.environ.get('DB_HOST', '__DB_HOST__'),
        'PORT': os.environ.get('DB_PORT', '__DB_PORT__'),
    }
}

CELERY_BROKER_PROTOCOL = os.environ.get('CELERY_BROKER_PROTOCOL', '__CELERY_BROKER_PROTOCOL__')
CELERY_BROKER_HOST = os.environ.get('CELERY_BROKER_HOST', '__CELERY_BROKER_HOST__')
CELERY_BROKER_PORT = os.environ.get('CELERY_BROKER_PORT', '__CELERY_BROKER_PORT__')

REDIS_HOST = os.environ.get('REDIS_URL', '__REDIS_URL__')
REDIS_PORT = os.environ.get('REDIS_PORT', '__REDIS_PORT__')
REDIS_PASSWORD = ''