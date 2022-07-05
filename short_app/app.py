#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: Main application file
Author: Prabal Pathak
"""

from fastapi import FastAPI

from .video.routes import router


app = FastAPI(
    title="Short App",
    # prefix="api",
    # openapi_url="/api/openapi.json",
    # redoc_url="/api/redoc",
    # docs_url="/api/docs",
    # prefix="/api/",
    # swagger_ui_oauth2_redirect_url = "/api/docs/oauth2-redirect"
)
app.include_router(router)


@app.get("/")
async def root():
    """root route"""
    return {"message": "Hello World!"}
