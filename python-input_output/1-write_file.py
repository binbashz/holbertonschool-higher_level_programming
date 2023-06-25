#!/usr/bin/python3
""" 1. Write to a file
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and returns the # of chars written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file_content = file.write(text)
        return len(text)
