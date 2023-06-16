#!/usr/bin/python3

""" Printing a square """


class Square:
    """
    Square class that defines a square.
    """

    def __init__(self, size=0):
        """
        Constructor to initialize the Square instance.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Method to calculate the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method to print the square.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
