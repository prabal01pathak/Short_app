#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: To create the folder and files from the app argparse
Author: Prabal Pathak
"""

from functools import wraps
from pathlib import Path
import os
import shutil

import typer

colors = {
    "green": typer.colors.GREEN,
    "blue": typer.colors.BLUE,
    "red": typer.colors.RED,
    "magenta": typer.colors.MAGENTA,
    "white": typer.colors.WHITE
}

def print(message:str , color: str="magenta", bold: bool=False):
    message = typer.style(message, fg=colors[color], bold=bold)
    typer.echo(message)
    


def create(func):
    """decorator to create app
       use the app path and create files
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Createing the application")
        path = func(*args, **kwargs)
        print("Done creating folder")
        files = create_files(path)
        print("Done", bold=True)
        return files
    return wrapper


@create
def create_folder(app_name: str) -> bool:
    """
    Create the folder for application and 
    create all the boilerplate required to start the project
    Args:
        app_name(str): Folder name to create
    Return:
        acknwoledgment(bool)
    """
    path = Path(f"./{app_name}")
    if path.exists():
        raise ValueError(f"Application already exists {path}")
    if not path.exists():
        path.mkdir()
    return path


def create_files(path: Path) -> list:
    """Create all the filed for the newely create app
    Args:
        path(Path): path for the application
    Return:
        files(list): list of files created
    Files:
        1. models.py
        2. views.py
        3. utils.py
        4. __init__.py
    """
    # create models.py
    models = path / "models.py"
    views = path / "views.py"
    utils = path / "utils.py"
    init = path / "__init__.py"
    files = [models, views, utils, init]
    for file in files:
        if not file.exists():
            file.touch()
    return files


def clear_app(app_name: str):
    path = Path(f"./{app_name}")
    if path.exists():
        shutil.rmtree(path)
    else:
        raise ValueError("Directory dosen't exist")



if __name__ == "__main__":
    f = create_folder("Hello")
    print(f)
