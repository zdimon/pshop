import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pshop',                      # Or path to database file if using sqlite3.
        'USER': 'chatuser',
        'PASSWORD': 'pasfas',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


PRESSA_DOMAIN = 'http://pressa.ru'
IMPORT_COVER_DOMAIN = PRESSA_DOMAIN
GET_FILE_URL = PRESSA_DOMAIN +'/get_litres_file'
IMPORT_CATALOG_URL = PRESSA_DOMAIN +'/genres_list'
IMPORT_JOURNAL_URL = PRESSA_DOMAIN+'/journals_list'
IMPORT_JOURNAL_CATALOG_URL = PRESSA_DOMAIN+'/journal_catalog'
IMPORT_COVER_JOURNAL_URL = PRESSA_DOMAIN+'/journal_cover'
IMPORT_JOURNAL_ISSUE = PRESSA_DOMAIN+'/journal_issue'
IMPORT_ISSUE_URL = PRESSA_DOMAIN+'/get_fresh_book'
PURCHASE_REQUEST_URL = PRESSA_DOMAIN+'/purchase'
PARTNER_SECRET_KEY = 'qwerty'
PARTNER_NAME = 'test'
PARTNER_ID = 'test'

DEBUG = True

LIQPAY_PUBLIC_KEY =	'i21835423321'
LIQPAY_PRIVATE_KEY =	'cS25yl03r8nFEiOVzh1aVhcBmhbVtELlwffWTT1a'
LIQPAY_RESULT_URL = 'http://shop.mirbu.com/liqpay/result'
LIQPAY_SERVER_URL = 'http://shop.mirbu.com/liqpay/server'
