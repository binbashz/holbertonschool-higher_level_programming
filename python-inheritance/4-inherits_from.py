#!/usr/bin/python3
""" task 04 """


def inherits_from(obj, a_class):

    """ Check if obj is an instance of a_class """
    if isinstance(obj, a_class):
        return True
    return issubclass(type(obj), a_class)
