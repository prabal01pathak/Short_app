#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typer.testing import CliRunner

from utils.argpars import cmd_app
from utils.directory import clear_app

runner = CliRunner()

def test_cmd_app():
    result = runner.invoke(cmd_app, ['startapp', 'testing_cmd_app'])
    assert result.exit_code == 0
    assert "Done" in result.stdout
    clear_app("testing_cmd_app")
