#!/usr/bin/python3
import uuid
from datetime import datetime
from .base_model import BaseModel
from .place import Place
from .user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        """Initialize a review instance"""
        super().__init__()
        self.id = str(uuid.uuid4())
        self.text = self._validate_text(text)
        self.rating = self._validate_rating(rating)
        self.place = self._validate_place(place)
        self.user = self._validate_user(user)

    def _validate_text(self, text):
        """Validates that text is a non-empty string"""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Review text must be a non-empty string")
        return text.strip()

    def _validate_rating(self, rating):
        """Validates that rating is between 1 and 5"""
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        return rating

    def _validate_place(self, place):
        """Validates that place is a valid Place instance"""
        if not isinstance(place, Place):
            raise ValueError("Place must be a valid Place instance")
        return place

    def _validate_user(self, user):
        """Validates that user is a valid User instance"""
        if not isinstance(user, User):
            raise ValueError("User must be a valid User instance")
        return user
