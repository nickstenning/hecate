# Django settings for hecate project.

from os import environ as env
import os.path

import dj_database_url

# Silence warnings from ipython/sqlite
import warnings
import exceptions
warnings.filterwarnings("ignore",
                        category=exceptions.RuntimeWarning,
                        module='django.db.backends.sqlite3.base',
                        lineno=53)

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DEBUG = env.get('DJANGO_DEBUG', 'true') == 'true'
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

# Allows setting Django admins from an environment variable of the form:
#
#   export DJANGO_ADMINS="John Doe <john@doe.com>, Bob Tables <bob@sqli.com>"
#
if env.get('DJANGO_ADMINS'):
    import email.utils
    ADMINS = tuple(email.utils.getaddresses([env.get('DJANGO_ADMINS')]))

MANAGERS = ADMINS

if env.get('DJANGO_EMAIL_DEBUG') == 'true':
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
elif env.get('MANDRILL_USERNAME'):
    EMAIL_HOST = 'smtp.mandrillapp.com'
    EMAIL_PORT = '587'
    EMAIL_HOST_USER = env.get('MANDRILL_USERNAME')
    EMAIL_HOST_PASSWORD = env.get('MANDRILL_APIKEY')
    EMAIL_USE_TLS = 'true'
else:
    EMAIL_HOST = env.get('EMAIL_HOST', 'localhost')
    EMAIL_PORT = env.get('EMAIL_PORT', '25')
    EMAIL_HOST_USER = env.get('EMAIL_USER', 'mail')
    EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', 'mail')
    EMAIL_USE_TLS = env.get('EMAIL_USE_TLS', 'true') == 'true'

EMAIL_DOMAIN = env.get('EMAIL_DOMAIN', 'hecate.example.com')
DEFAULT_FROM_EMAIL = env.get('DEFAULT_FROM_EMAIL', 'noreply@%s' % EMAIL_DOMAIN)
SERVER_EMAIL = env.get('SERVER_EMAIL', 'robots@%s' % EMAIL_DOMAIN)
if env.get('DEFAULT_TO_EMAIL'):
    DEFAULT_TO_EMAIL = (env.get('DEFAULT_TO_EMAIL'),)

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///development.sqlite3')
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
if DEBUG:
    SECRET_KEY = 'f8pqx#@_x-nv+$m7q7lt^lrmby4ixjms#x*2_sskn9)%t36(!q'
else:
    SECRET_KEY = env.get('DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hecate.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'hecate.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'djangosecure',
    'apps.accounts',
)

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'homepage'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Redirect from plain HTTP to HTTPS if not in dev mode
if env.get('DJANGO_SECURE') == 'true':
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 7 * 86400
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
else:
    SECURE_SSL_REDIRECT = False

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
