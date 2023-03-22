#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """ The amenity class """

     __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""
