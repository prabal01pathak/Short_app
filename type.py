#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from typing import Optional

import typer
from typer import Typer

app = Typer()

@app.command()
def makemigrations():
    typer.echo("create migrations")

@app.command()
def runserver(host: Optional[str] = "localhost", port: Optional[int] = 8000):
    print(f"starting the server at https://{host}/{port}")
    while True:
        time.sleep(1)



if __name__ == "__main__":
    app()


