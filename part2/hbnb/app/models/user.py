#!/usr/bin/python3
"""User class inherits from BaseModel"""
from .base_model import BaseModel


class User(BaseModel):
    """"Defines a User with atrributes inherited from BaseModel"""
    def __init__(self, first_name, last_name, email, is_admin=False):
        """Initialize a User instance"""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
