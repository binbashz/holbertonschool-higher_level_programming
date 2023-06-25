#!/usr/bin/python3
"""  Save Object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as file_json:
        """ The json.dump() function is used to serialize the
            object my_obj and write the JSON representation to the file
            The json.dump() function converts the object into a JSON string
            representation and writes it to the file.
        """
        json.dump(my_obj, file_json)
