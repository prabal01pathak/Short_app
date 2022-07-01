#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: Main application file
Author: Prabal Pathak
"""

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    """root route"""
    return {"message": "Hello World!"}
