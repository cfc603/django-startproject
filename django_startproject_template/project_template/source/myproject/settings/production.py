from .base import *

DEBUG = False

ALLOWED_HOSTS = [PRODUCTION_URL, ]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myproject',
        'PASSWORD': get_secrets('DATABASE_PASS_PRODUCTION'),
        'HOST': 'localhost',
    }
}
