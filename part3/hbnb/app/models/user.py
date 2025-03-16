#!/usr/bin/python3
"""User class inherits from BaseModel"""
from .base_model import BaseModel


class User(BaseModel):
    """"Defines a User with atrributes inherited from BaseModel"""
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """Initialize a User instance"""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.hash_password(password)

    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
