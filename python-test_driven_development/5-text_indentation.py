#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """
    Prints the given text with two new lines after each '.', '?', and ':'

    Args:
        text (str): Input text to be processed

    Raises:
        TypeError: If text is not a string

    Note:
        No space at the beginning or end of each printed line
    """

    if not isinstance(text, str):  # Check if text is a string
        raise TypeError('text must be a string')

    delimiters = {'.', '?', ':'}  # Set of delimiters
    index = 0  # Initialize index variable

    while index < len(text):
        if text[index] in delimiters:  # Check if character is a delimiter
            print(text[index] + "\n\n", end="")  # Print delim with 2 new lines
            index += 1
            while index < len(text) and text[index] == " ":  # Skip consec spac
                index += 1
        else:
            print(text[index], end="")  # Print character
            index += 1
