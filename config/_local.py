import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

IMPORT_CATALOG_URL = 'http://localhost:8000/genres_list'
IMPORT_JOURNAL_URL = 'http://localhost:8000/journals_list'
IMPORT_COVER_JOURNAL_URL = 'http://localhost:8000/journal_cover'
IMPORT_ISSUE_URL = 'http://localhost:8000/get_fresh_book'