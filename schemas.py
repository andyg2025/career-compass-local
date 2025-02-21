# schemas.py
# pylint: disable=R0903
"""
This module contains the Pydantic schemas for validating and --
serializing the request and response data.
It defines two schemas: UserCreateSchema for creating users and --
UserSchema for representing user data.
"""
from typing import List
from pydantic import BaseModel

class QuerySchema(BaseModel):

    local: str
    q: str
    time: str

    class Config:
        orm_mode = True