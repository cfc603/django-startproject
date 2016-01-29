import sys

from .base import *

DEBUG = False

ALLOWED_HOSTS = [STAGING_URL,]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': '',
            'PASSWORD': get_secrets('DATABASE_PASS_STAGING'),
            'HOST': '',
        }
    }