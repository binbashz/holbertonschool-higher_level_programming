#!/usr/bin/python3

"""

Class Rectangle

"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """initialized  instance of class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter  width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter  width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
