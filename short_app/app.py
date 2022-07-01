#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}
