from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['bilolsolih.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS = ['']
