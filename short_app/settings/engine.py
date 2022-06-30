#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()
ENGINE = {}

def memoize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        engine = func(*args, **kwargs)
        ENGINE['engine'] = engine
        return engine
    return wrapper


@memoize
def create_connection(url: str) -> create_engine:
    if url.startswith("sqlite"):
        engine = create_engine(url, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(url)
    return engine


def make_session(url: str) -> sessionmaker:
    engine = create_connection(url)
    local_session = sessionmaker(autocommit=True, autflush=True, bind=engine)
    return local_session


if __name__ == "__main__":
    url = "sqlite:///sql.db"
    session = make_session(url)
    print(ENGINE, session)
