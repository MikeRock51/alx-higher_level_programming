#!/usr/bin/python3
"""
A python script that contains the class definition of
a State and an instance
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A state class

    Attributes:
        * id(Integer): The id of the state
        * name(String): The name of the state
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
