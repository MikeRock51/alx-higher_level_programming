#!/usr/bin/python3
"""
A script that contains the class definition of a City
"""


from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    A class definition of a City

    Attributes:
        * id (Integer): The id of the city
        * name (String): The name of the city
        * state_id (Integer): Foreign key that links to states.id
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
