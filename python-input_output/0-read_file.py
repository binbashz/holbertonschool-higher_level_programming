#!/usr/bin/python3
"""
   task o read file
"""


def read_file(filename=""):
    """
    read the text file and use witg
    """
    with open(filename, encoding="utf-8") as my_file_to_open:
        print(my_file_to_open.read(), end='')
