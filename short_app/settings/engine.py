#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Sql engine settings like session and base class
Author: Prabal Pathak
"""

from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()
ENGINE = {}


def memoize(func):
    """Store the session"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        engine = func(*args, **kwargs)
        ENGINE["engine"] = engine
        return engine

    return wrapper


@memoize
def create_connection(url: str) -> create_engine:
    """Create engine for sql and reurn it"""
    if url.startswith("sqlite"):
        engine = create_engine(url, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(url)
    return engine


def make_session(url: str) -> sessionmaker:
    """Create local session for database access"""
    engine = create_connection(url)
    local_session = sessionmaker(autocommit=True, autflush=True, bind=engine)
    return local_session


if __name__ == "__main__":
    DATABASE_URL = "sqlite:///sql.db"
    session = make_session(DATABASE_URL)
    print(ENGINE, session)
