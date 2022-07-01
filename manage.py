#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: create application, runserver, makemigration, and migrate
Author: Prabal Pathak
"""

import uvicorn

from short_app.utils.argpars import cmd_app
from short_app.utils.directory import create_folder


if __name__ == "__main__":
    cmd_app()
