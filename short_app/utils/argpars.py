#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: get the arguments from the terminal when running
    manage.py
Author: Prabal Pathak
"""

import os
import typer

from .directory import create_folder, print_message

cmd_app = typer.Typer()
PORT = 8000
HOST = "127.0.0.1"


@cmd_app.command()
def runserver(host: str = HOST, port: int = PORT, reload: bool = False):
    """
    Run the uvicorn server
    """
    # root_path = "/api/v1"
    command = f"uvicorn short_app.app:app --host {host} --port {port}"

    if not reload:
        os.system(command)
    else:
        os.system(command + " --reload")


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
    """create the add with all modules"""
    create_folder(name)
    print_message("Done createing the folders and files")


if __name__ == "__main__":
    cmd_app()
