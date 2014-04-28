DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'atlas',
        'USER': '{{atlas_db_user}}',
        'PASSWORD': '{{atlas_db_password}}',
        'HOST': '{{atlas_db_host}}',
        'PORT': '{{atlas_db_port}}',
    }
}

STATICFILES_DIRS = (
    "{{atlas_prefix}}/media/",
)

LOCALE_PATHS = (
    '{{atlas_prefix}}/django_files/locale',
)

TEMPLATE_DIRS = (
    '{{atlas_prefix}}/html',
)

SECRET_KEY = 'my_pets_name_is_eloise'

REDIS = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    },
}

HTTP_HOST = '/'
DB_PREFIX = 'new_'
STATIC_IMAGE_MODE = 'PNG'
DATA_FILES_PATH = '/tmp/'
INTERNAL_IPS = ('127.0.0.1','192.168.33.1', '10.0.2.2') #For Django debug toolbar

# FOR VERBOSE JS OUTPUT
DEV = False
