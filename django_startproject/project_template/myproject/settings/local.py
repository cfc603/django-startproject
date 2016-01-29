import sys

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

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
            'NAME': 'myproject',
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }