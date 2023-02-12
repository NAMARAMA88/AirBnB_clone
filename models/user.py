#!/usr/bin/python3
"""
This is User class to represent new users
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User subclass that inherits from BaseModel """
    email = "coulrama2@gmail.com"
    password = "1788Rama"
    first_name = "NAMARAMA"
    last_name = "COULIBALY"
