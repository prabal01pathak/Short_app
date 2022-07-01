"""
Discription: Test short_app routes
Author: Prabal Pathak
"""
from short_app import __version__


def test_version():
    """test the application version"""
    assert __version__ == "0.1.0"
