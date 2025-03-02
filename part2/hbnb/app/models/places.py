#!/usr/bin/python3
"""Defines the place class that represents rental properties.
A place object stores details such as title, description, price, location,
and associated reviews and amenities"""
from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.owner = owner
        self.reviews = []  # list to store relatd reviews
        self.amenities = []  # lisr to store related amenities

    def add_review(self, review):
        """add a review to the place"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """add amenity to the place"""
        self.amenities.append(amenity)
