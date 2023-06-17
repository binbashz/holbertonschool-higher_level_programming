#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespace from the text
    text = text.strip()

    # Define the punctuation characters that will trigger new lines
    punctuation = [".", "?", ":"]

    # Iterate over each character in the text
    for char in text:
        # Print the character without a newline
        print(char, end="")

        # Check if the character is a punctuation mark
        if char in punctuation:
            # Print two new lines after the punctuation mark
            print("\n\n", end="")

    # Print a final newline character
    print()
