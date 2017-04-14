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


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
