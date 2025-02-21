# models.py
# pylint: disable=R0903
"""
This module contains the SQLAlchemy models for the application. 
It defines the 'User' model with basic attributes like 'id', 'name', and 'orders'.
"""
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = "Jobs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    type = Column(String, nullable=False)
    postdate = Column(String, nullable=False)
    url = Column(String, nullable=False)
