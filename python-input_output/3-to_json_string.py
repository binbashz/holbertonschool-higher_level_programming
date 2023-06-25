#!/usr/bin/python3
""" To JSON string
"""

import json


def to_json_string(my_obj):
    """
        Use the 'json.dumps()' function to
        serialize the object into a JSON-formatted string
    """
    return json.dumps(my_obj)
