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

class JobUpdateRequestSchema(BaseModel):
    """
    Schema for representing a user.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        orders (List[int]): A list of orders associated with the user.
    """

    websit : List[str]
    type: List[str]
    location: str
    time_limited: str

    class Config:
        """
        Configuration for the UserSchema.

        orm_mode = True tells Pydantic to treat the data as ORM models, --
        allowing automatic conversion
        from SQLAlchemy model instances to Pydantic models.
        """

        orm_mode = True
