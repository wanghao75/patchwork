"""
Sample production-ready settings for patchwork project.

Most of these are commented out as they will be installation dependent.

Design based on:
    http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/
"""

from .base import *  # noqa

#
# Core settings
# https://docs.djangoproject.com/en/2.2/ref/settings/#core-settings
#

# Security
#
# You'll need to replace this to a random string. The following python code can
# be used to generate a secret key:
#
#      import string
#      import secrets
#
#      chars = string.ascii_letters + string.digits + string.punctuation
#      print("".join([secrets.choice(chars) for i in range(50)]))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', "")

# Email
#
# Replace this with your own details

EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = os.getenv('EMAIL_PORT', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
SERVER_EMAIL = DEFAULT_FROM_EMAIL
NOTIFICATION_FROM_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = (
    # Add administrator contact details in the form:
    # ('Jeremy Kerr', 'jk@ozlabs.org'),
)

#
# Static files settings
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-files
# https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
#

STATIC_ROOT = os.environ.get('STATIC_ROOT', 'static')

STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)

CSRF_TRUSTED_ORIGINS = ['https://patchwork.osinfra.cn']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DATABASE_NAME", ""),
        'USER': os.environ.get("DATABASE_USER", ""),
        'PASSWORD': os.environ.get("DATABASE_PASSWORD", ""),
        'HOST': os.environ.get("DATABASE_HOST", ""),
        'PORT': os.environ.get("DATABASE_PORT", ""),
    }
}

DATA_DIR = '/var/lib/patchcheck'
ALLOWED_HOSTS = ['*']
DEBUG = False
