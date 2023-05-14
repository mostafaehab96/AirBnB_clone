#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
