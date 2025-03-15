#!/usr/bin/python3
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../hbnb')))


from app.models.amenity import Amenity
import unittest

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")

test_amenity_creation()
