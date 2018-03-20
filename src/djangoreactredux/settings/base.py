"""Django settings for djangoreactredux project."""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ajsdgas7&*kosdsa21[]jaksdhlka-;kmcv8l$#diepsm8&ah^'
#SECRET_KEY = '#01f&u4_xy_jk7t7n3#i*v=v)cl%-4sjpmy=5=4eo0h@ki#y!c'

DEBUG = True

ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['localhost']

PAGE_CACHE_SECONDS = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django_mako_plus',
    'rest_framework',
    'knox',
    'django_extensions',
    'homepage',
    'accounts',
    'base',
    'testapp'
)

# MIDDLEWARE_CLASSES = (
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     # 'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.common.CommonMiddleware'
# )


# A logger for DMP
# SECURITY WARNING: never set this True on a live site
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# store static files locally and serve with whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


TEMPLATES = [
    {
        # Note that additional options exist - see the DMP docs
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'APP_DIRS': True,

        'OPTIONS': {
            # these define how page scripts are run by browsers
            # the default app and page to render in Mako when the url is too short
            # if None (no default app), DMP's urls.py will not capture short URLs
            'DEFAULT_APP': 'homepage',
            'DEFAULT_PAGE': 'index',
            # functions to automatically add variables to the params/context before templates are rendered
            'CONTEXT_PROCESSORS': [
                # adds "STATIC_URL" from settings.py
                'django.template.context_processors.static',
                # adds debug and sql_queries
                'django.template.context_processors.debug',
                'django.template.context_processors.request',           # adds "request" object
                # adds "user" and "perms" objects
                'django.contrib.auth.context_processors.auth',
                # adds messages from the messages framework
                'django.contrib.messages.context_processors.messages',
                # adds "settings" dictionary
                'django_mako_plus.context_processors.settings',
            ],

            # additional template dirs to search
            'TEMPLATES_DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],

            # how to discover and register apps
            # 'default': register all apps that are subfolders of BASE_DIR
            # 'all': register all apps, even when pip-installed or django apps (e.g. django.contrib.admin)
            # 'none': no auto-registration; apps must be registered with `django_mako_plus.register_dmp_app()`
            'APP_DISCOVERY': 'default',

            # identifies where the Mako template cache will be stored, relative to each template directory
            'TEMPLATES_CACHE_DIR': '__dmpcache__',

            # static file providers
            'CONTENT_PROVIDERS': [
                # adds JS context - this should normally be listed first
                {'provider': 'django_mako_plus.JsContextProvider'},
                # generates links for app/styles/template.css
                {'provider': 'django_mako_plus.CssLinkProvider'},
                # generates links for app/scripts/template.js
                #{'provider': 'django_mako_plus.JsLinkProvider'},
                {'provider': 'django_mako_plus.WebpackJsLinkProvider',
                    'filename': lambda pr: os.path.join(pr.app_config.path, 'scripts', '__bundle__.js')
                 },
                {'provider': 'django_mako_plus.WebpackJsCallProvider'},
                # { 'provider': 'django_mako_plus.CompileScssProvider' },   # autocompiles Scss files
                # { 'provider': 'django_mako_plus.CompileLessProvider' },   # autocompiles Less files
            ],

            # webpack providers
            'WEBPACK_PROVIDERS': [
                # generates links for app/scripts/template.js
                {'provider': 'django_mako_plus.JsLinkProvider'},
            ],

            # additional template dirs to search
            'TEMPLATES_DIRS': [
                # '/var/somewhere/templates/',
            ],
            # imports for every template
            'DEFAULT_TEMPLATE_IMPORTS': [
                # the next two lines are just examples of including common imports in templates
                'import django_mako_plus',
                # 'import os, os.path, re, json',
            ],
        },
    },
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        #'APP_DIRS': False,
        # Instead, look for template source files in these dirs.
       # 'DIRS': [
       #     STATIC_ROOT,  # required to statically include common Underscore templates
       # ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


ROOT_URLCONF = 'djangoreactredux.urls'

WSGI_APPLICATION = 'djangoreactredux.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_ACTIVATION_DAYS = 70  # days

# ############# REST FRAMEWORK ###################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
}

# ############ REST KNOX ########################
REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'USER_SERIALIZER': 'knox.serializers.UserSerializer'
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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
