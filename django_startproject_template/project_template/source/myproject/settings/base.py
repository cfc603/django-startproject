import json
from unipath import Path

from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: Path(BASE_DIR, ...)
BASE_DIR = Path(__file__).ancestor(3)


# get secrets from json file
with open(Path(BASE_DIR.parent + '/secrets/secrets.json')) as f:
    secrets = json.loads(f.read())

def get_secrets(setting, secrets=secrets):
    """Get setting variable or return exception"""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} enviroment variable'.format(setting)
        raise ImproperlyConfigured


# Application definition

INSTALLED_APPS = [
    'djangocms_admin_style', # must be before 'django.contrib.admin'

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # django cms apps
    'cms',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'filer',
    'menus',
    'mptt',
    'sekizai',
    'treebeard',

    # local apps

]

MIDDLEWARE = [

    'cms.middleware.utils.ApphookReloadMiddleware', # needs to be before

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # django cms
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

SECRET_KEY = get_secrets('SECRET_KEY')

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'myproject/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # django cms processor
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR.parent + '/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR.parent + '/media')


# django cms settings
CMS_TEMPLATES = [
    ('cms/default.html', 'Default page template'),
]

LANGUAGES = [
    ('en', 'English'),
]

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
