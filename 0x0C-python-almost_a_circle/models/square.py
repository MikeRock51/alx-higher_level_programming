#!/usr/bin/python3
"""A module containing a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides default __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Validates and sets the size of a square"""
        self.width = value

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""

        index = 0
        if args and len(args) > 0:
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Square"""
        square_dict = {'id': self.id, 'size': self.width,
                       'x': self.x, 'y': self.y}
        return square_dict
