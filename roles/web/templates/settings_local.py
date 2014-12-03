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

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '{{atlas_redis_connection_string}}',
        'OPTIONS': {
            "PARSER_CLASS": "redis.connection.HiredisParser"
        }
    },
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

HTTP_HOST = '/'
DB_PREFIX = 'new_'
DATA_FILES_PATH = '{{atlas_prefix}}/media/data'
INTERNAL_IPS = ('127.0.0.1',
                '192.168.33.1',
                '10.0.2.2') #For Django debug toolbar

# FOR VERBOSE JS OUTPUT
DEBUG = {{atlas_environment == 'dev'}}
DEV = not DEBUG

STATIC_IMAGE_PATH = "{{atlas_static_image_path}}"
STATIC_IMAGE_PHANTOMJS_URL = "{{atlas_static_image_phantomjs_url}}"

# These are old - safe to remove?
STATIC_IMAGE_MODE = 'PNG'
EXPORT_IMAGE_WIDTH = 748
EXPORT_IMAGE_HEIGHT = 520
PHANTOM_JS_EXECUTABLE = '/usr/bin/phantomjs'
PHANTOM_JS_SCRIPT = '{{atlas_prefix}}/media/js/explore/generate.svg.js'
PHANTOM_JS_TEMP = '{{atlas_phantomjs_temp}}'
BACKGROUND_CACHE_URL_HOST = 'localhost:8000'

ALLOWED_HOSTS = ["*"]

COMPRESS_ROOT = '{{atlas_prefix}}/media/'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_OFFLINE = not DEBUG
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': '/media/',
    'VERSION': '1.0.7',  # TODO: We don't need this anymore maybe?
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
