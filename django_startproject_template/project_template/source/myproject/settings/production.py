from .base import *

DEBUG = False

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salesranktable$myproject',
        'USER': 'salesranktable',
        'PASSWORD': get_secrets('DATABASE_PASS_PRODUCTION'),
        'HOST': 'salesranktable.mysql.pythonanywhere-services.com',
    }
}
