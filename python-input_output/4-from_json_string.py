#!/usr/bin/python3
"""  From JSON string to Object
"""


import json


def from_json_string(my_str):
    """  json.loads() function parses the JSON string
        and converts it into the corresponding Python data structure
    """
    return json.loads(my_str)
