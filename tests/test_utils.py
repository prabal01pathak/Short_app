#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Discription: Test command line utlitize
Author: Prabal Pathak
"""

from typer.testing import CliRunner

from short_app.utils.argpars import cmd_app
from short_app.utils.directory import clear_app

runner = CliRunner()


def test_startapp():
    """Test the argparse.py commands : Create App"""
    result = runner.invoke(cmd_app, ["startapp", "testing_cmd_app"])
    assert result.exit_code == 0
    assert "Done" in result.stdout
    clear_app("testing_cmd_app")


def test_makemigrations():
    """Test makemigrations command of utils.argparse.py"""
    result = runner.invoke(cmd_app, ["makemigrations"])
    assert result.exit_code == 0
    assert "migrations" in result.stdout


def test_migrate():
    """Test migrate command of utils.argparse.py"""
    result = runner.invoke(cmd_app, ["migrate"])
    assert result.exit_code == 0
    assert "Migrating" in result.stdout
