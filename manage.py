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
        raise ImportError(f"Make sure you have {_e} installed if you are using virtual environment please activate it")


if __name__ == "__main__":
    main()
