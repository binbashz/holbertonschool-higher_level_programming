#!/usr/bin/python3
""" Class to JSON"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    for JSON serialization of a object
    """
    return obj.__dict__
