#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Write an Object to a text file, using a JSON representation"""
    with open(filename, 'r') as file_json:
        return json.load(file_json)
