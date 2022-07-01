#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: create application, runserver, makemigration, and migrate
Author: Prabal Pathak
"""

import uvicorn

from utils.argpars import cmd_app
from utils.directory import create_folder


if __name__ == "__main__":
    cmd_app()
