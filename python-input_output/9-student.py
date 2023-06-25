#!/usr/bin/python3
""" Student to JSON
"""


class Student:
    """Define a  class student
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the Student instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
        """
        return self.__dict__
