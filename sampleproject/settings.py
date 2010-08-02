# -*- coding: utf-8 -*-

import os, sys
_abs = lambda *a: os.path.abspath(os.path.join(*a))

ROOT = _abs(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'sample.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

SITE_ID = 1

MEDIA_ROOT = ''
MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'wlu_6d@&4og2a4-6k8*35l0_h=%gy(gb9eis8w6d^fktydyby4'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'sampleproject.urls'

TEMPLATE_DIRS = (
    _abs(ROOT, 'templates'),
)

INSTALLED_APPS = (
    'template_inspector',
)