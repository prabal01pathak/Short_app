#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: Application settings like app name, database settings, installed apps
Author: Prabal Pathak
"""

import os
from collections import namedtuple
from .utils import get_env


APP_NAME = "short_app"
SECRET_KEY = os.getenv("SECRET_KEY", None)
INSTALLED_APPS = [
    "short_app",
]

DATABASES = {
    "sqlite3": "sqlite3",
    "postgresql": {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': get_env('POSTGRE_USER', 'postgres'),
        'PASSWORD': get_env('POSTGRE_PASSWORD', 'postgres'),
        'NAME': get_env('POSTGRE_NAME', 'postgres'),
        'HOST': get_env('POSTGRE_HOST', 'localhost'),
        'PORT': int(get_env('POSTGRE_PORT', '5432')),
    },
    "mysql": {
        'ENGINE': 'django.db.backends.mysql',
        'USER': get_env('MYSQL_USER', 'root'),
        'PASSWORD': get_env('MYSQL_PASSWORD', ''),
        'NAME': get_env('MYSQL_NAME', 'labelstudio'),
        'HOST': get_env('MYSQL_HOST', 'localhost'),
        'PORT': int(get_env('MYSQL_PORT', '3306')),
    }
}

DATABASE_DEFAULT = DATABASES['sqlite3'] if not os.getenv("DB", None) else DATABASES[os.getenv("DB")]
