"""
Django settings for shop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import abspath, dirname, basename, join, split
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.utils.translation import ugettext_lazy as _

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
    )

from local import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7^hy-ys*3nt@3dx67i$h&jwc4b2!e0wxjmt57+h+o=-io85tt4'

# SECURITY WARNING: don't run with debug turned on in production!

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
ACCOUNT_ACTIVATION_DAYS = 2



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.pressinfo.am'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@pressinfo.am'
EMAIL_HOST_PASSWORD = 'amaretto.c67'
DEFAULT_FROM_EMAIL = 'pressinfo.am@gmail.com'



EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/home/zdimon/tmp' # change this to a proper location


#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 465
#EMAIL_HOST_USER = 'noreply.pressinfo@gmail.com'
#EMAIL_HOST_PASSWORD = 'amaretto.c67'
#DEFAULT_FROM_EMAIL = 'noreply.pressinfo@gmail.com'
#SERVER_EMAIL = 'noreply.pressinfo@gmail.com'



# Application definition

INSTALLED_APPS = (
    'flatblocks',
    'registration',
    'site',
    'page',
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'banner_rotator',
    
    'django.contrib.sites',
    'main',
    'south',
    'catalog',
    'mptt',
    
    'dbbackup',
    'djsupervisor',
    'djcelery',
    'backup',
    'liqpay',
    'flatblocks',
    
    'modeltranslation',
    'redactor',
    'rosetta',
    'paymaster',
    'captcha',
    
    
)

RECAPTCHA_PUBLIC_KEY = '6LdVS_8SAAAAAD64_-IWB41qYEbBW9Qh3XjdaLGQ'
RECAPTCHA_PRIVATE_KEY = '6LdVS_8SAAAAANiQzpQVCY2wTQfQTjn4P1e0cXxl'

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',

)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.i18n',
        'django.contrib.messages.context_processors.messages'

)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGES = (
    ('hy', _('Armenian')),
    ('ru', _('Russian')),
    ('en', _('English')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
REDACTOR_OPTIONS = {'lang': 'hy'}
REDACTOR_UPLOAD = 'uploads/'
    
SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
        join(BASE_DIR, 'locale'),
    )
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
YANDEX_TRANSLATE_KEY = 'trnsl.1.1.20140521T130035Z.1014ae2799c685e3.97b1345108ab3a8520d96f730016a9dac947049b'
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'en'
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'English'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
LOGIN_REDIRECT_URL = '/'

import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/0'

from celery.schedules import crontab
from datetime import timedelta
'''
CELERYBEAT_SCHEDULE = {

        'backup': {'task': 'backup.tasks.backup','schedule': crontab(minute=0, hour=0)},
        'loadnewissue': {'task': 'catalog.tasks.import_new','schedule': crontab(minute=0, hour="*/1")},
        #'backup': {'task': 'backup.tasks.backup','schedule': crontab()},

}'''
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_FILESYSTEM_DIRECTORY = BASE_DIR+'/backup/data'

SECRET = 'secret'
MIRROR_ID = 1



