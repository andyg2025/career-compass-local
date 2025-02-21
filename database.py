# database.py
"""
This module contains the database configuration and session management for the application.
It defines the connection to the PostgreSQL database -
and provides a sessionmaker for interacting with the database.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

User_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():

    db = User_Session()
    try:
        yield db
    finally:
        db.close()
