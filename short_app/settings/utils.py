#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: Utilitize for application settings
Author: Prabal Pathak
"""

import os
from typing import Any


def get_env(key: str, args: Any) -> str:
    """Get environment variables
    Args:
        key(str): environment key
    Return:
        str: environment variable value
    """
    return os.getenv(key, args)
