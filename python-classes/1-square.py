#!/usr/bin/python3

""" Write a class Square that defines a square by: ( 0-square.py) """


class Square:

    """
    This is the Square class that defines a square.

    Private instance attribute:
        - __size: represents the size of the square
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
