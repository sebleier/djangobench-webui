import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 'kd()b(6e(zd@(wfxffk4wy^ixby4=s@!n+rkwz-vvb+_ja$$79'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = ()
TEMPLATE_DIRS = ()

# Important Settings
INSTALLED_APPS = (
    'djangobench_webui.webui',
)
MEDIA_URL = 'site_media/'
ROOT_URLCONF = 'djangobench_webui.urls'
BENCHMARK_REPO_PATH = os.path.join(os.environ.get('VIRTUAL_ENV'), 'django')
RESULTS_DIR = os.path.join(os.environ.get('VIRTUAL_ENV'), 'results')

try:
    from local_settings import *
except ImportError:
    pass