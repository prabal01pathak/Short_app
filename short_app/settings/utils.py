#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def get_env(key: str, args):
    return os.getenv(key, 0)
