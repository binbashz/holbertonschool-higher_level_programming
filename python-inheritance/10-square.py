#!/usr/bin/env python3
"""Defines a Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the square description"""
        return "[Square] {}/{}".format(self.__width, self.__height)
