#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: Utilitize for application settings
Author: Prabal Pathak
"""

import os

def get_env(key: str, args: str) -> str:
    """Get environment variables
    Args:
        key(str): environment key
    Return:
        str: environment variable value
    """
    return os.getenv(key, 0)
