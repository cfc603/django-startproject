from .base import *


ALLOWED_HOSTS = []
DEBUG = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "myproject",
        "USER": "dev",
        "PASSWORD": get_secrets("DATABASE_PASS_LOCAL"),
        "HOST": "localhost",
        "PORT": "3306",
    }
}
