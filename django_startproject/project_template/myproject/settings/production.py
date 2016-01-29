from .base import *

DEBUG = False

ALLOWED_HOSTS = [PRODUCTION_URL, ]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': get_secrets('DATABASE_PASS_PRODUCTION'),
        'HOST': '',
    }
}

# SECURE_SSL_REDIRECT = True