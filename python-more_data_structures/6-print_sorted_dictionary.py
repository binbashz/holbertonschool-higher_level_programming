#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Retrieve the keys of the dictionary and sort them alphabetically
    sorted_keys = sorted(a_dictionary.keys())
    # Iterate over the sorted keys
    for key in sorted_keys:
        # Print each key-value pair
        print(key, ":", a_dictionary[key])
