#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: create application, runserver, makemigration, and migrate
Author: Prabal Pathak
"""




def main():
    """command line utility"""
    try:
        from short_app.utils.argpars import cmd_app
        cmd_app()
    except ImportError as _e:
        print("Please make sure you have \
activated the virtual environmentError: ", _e)


if __name__ == "__main__":
    main()
