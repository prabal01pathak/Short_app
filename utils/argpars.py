#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: get the arguments from the terminal when running 
    manage.py
Author: Prabal Pathak
"""

from typing import Optional
import typer
import uvicorn

from short_app.app import app
from .directory import create_folder, print

cmd_app = typer.Typer()
PORT = 8000
HOST = "127.0.0.1"



@cmd_app.command()
def runserver(host: str = HOST, port: int = PORT):
    """
    Run the uvicorn server
    """
    uvicorn.run(app, host=host, port= port)


@cmd_app.command()
def makemigrations():
    """
    Make migrations
    """
    typer.echo(" making the migrations", color="green")

@cmd_app.command()
def migrate():
    """
    migrate the database
    """
    typer.echo(" Migrating the migrations")


@cmd_app.command()
def startapp(name: str = typer.Argument(...)):
    create_folder(name)
    print("Done createing the folders and files")


if __name__=="__main__":
    cmd_app()
