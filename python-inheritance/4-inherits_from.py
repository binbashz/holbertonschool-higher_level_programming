#!/usr/bin/python3
""" task 04 """


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to check against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from a_class; False otherwise.
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
