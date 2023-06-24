#!/usr/bin/env python3
"""Defines a Square class that inherits from Rectangle"""


class BaseGeometry:
    """Defines the base geometry class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Defines a rectangle class"""

    def __init__(self, width, height):
        """Initializes a rectangle instance"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Returns the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size):
        """Initializes a square instance"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)
