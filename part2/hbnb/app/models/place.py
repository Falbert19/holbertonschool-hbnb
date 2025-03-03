#!/usr/bin/python3
"""Defines the place class that represents rental properties.
A place object stores details such as title, description, price, location,
and associated reviews and amenities"""
from .base_model import BaseModel
from .user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self._validate_string(title, "Title")
        self.description = self._validate_string(description, "Description")
        self.price = self._validate_price(price)
        self.latitude = self._validate_coordinate(latitude, "Latitude")
        self.longitude = self._validate_coordinate(longitude, "Longitude")
        self.owner = self._validate_owner(owner)
        self.reviews = []  # list to store related reviews
        self.amenities = []  # list to store related amenities

    def _validate_string(self, value, field_name):
        """Validates that a value is a non-empty string"""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")
        return value.strip()

    def _validate_price(self, value):
        """Validates that price is a positive float."""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a positive number")
        return float(value)

    def _validate_coordinate(self, value, field_name):
        """Validates latitude/longitude as a valid float."""
        if not isinstance(value, (int, float)) or not (-180 <= value <= 180):
            raise ValueError(f"{field_name} must be a valid coordinate")
        return float(value)

    def _validate_owner(self, owner):
        """Validates that the owner is a valid User"""
        if not isinstance(owner, User):
            raise ValueError("Owner must be a User")
        return owner

    def add_review(self, review):
        """add a review to the place"""
        from .review import Review

        if not isinstance(review, Review):
            raise ValueError("Invalid review")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """add amenity to the place"""
        from .amenity import Amenity  # Avoid circular import

        if not isinstance(amenity, Amenity):
            raise ValueError("Invalid amenity")
        self.amenities.append(amenity)

    def __repr__(self):
        """Returns a string representation of the Place object"""
        return (f"Place(title='{self.title}', price={self.price}, "
                f"latitude={self.latitude}, longitude={self.longitude}, "
                f"owner='{self.owner}', reviews={len(self.reviews)}, "
                f"amenities={len(self.amenities)})")
