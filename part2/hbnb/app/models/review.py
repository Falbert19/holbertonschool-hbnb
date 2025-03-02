#!/usr/bin/python3
import .base_model import BaseModel
from .place import Place
from .user import User


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        """Initialize a review instance"""
        super().__init__()
        self.id = str(uuid.uuid4())
        self.text = self.__validate_text(text)
        self.rating = self.validate_rating(rating)
        self.user = self.validate_user(user)
        self.created_at = datetime.utcnow()
        self.update_at = self.created_at

    def _validate_text(self, text):
        """Ensures the review text is non-empty"""
        if not text or not isinstance(text, str):
            raise ValueError("Review text cannot be empty.")
        return text.strip()

    def _validate_rating(self, rating):
        """Ensures the rating is between 1 and 5"""
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")
        return rating

    def _validate_place(self, place):
        """Ensures the place exists and is a valid Place instance"""
        if not isinstance(place, Place):
            raise ValueError("Invalid place instance.")
        return place

    def _validate_user(self, user):
        """Ensures the user exists and is a valid User instance"""
        if not isinstance(user, User):
            raise ValueError("Invalid user instance.")
        return user

    def update(self, text=None, rating=None):
        """
        Updates the review text or rating while enforcing constraints
        """
        if text is not None:
            self.text = self._validate_text(text)
        if rating is not None:
            self.rating = self._validate_rating(rating)
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        """Returns a string representation of the Review instance"""
        return (f"Review(id='{self.id}', text='{self.text}', rating={self.rating}, "
                f"place='{self.place.id}', user='{self.user.id}', "
                f"created_at={self.created_at}, updated_at={self.updated_at})")
