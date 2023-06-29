#!/usr/bin/python3

"""Task 0. Base class
"""


class Base:
    """ Private class attribute to track the number of objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """ If an id is provided, assign it to the
        public instance attribute 'id' """
        if id is not None:
            self.id = id
        else:
            """ If no id is provided, increment the counter and
            assign the new value to 'id' """

            Base.__nb_objects += 1
            self.id = Base.__nb_objects
