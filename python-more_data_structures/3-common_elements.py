#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_set = set()

    # Iterate over each element in the first set
    for item in set_1:
        # Check if the element is present in the second set
        if item in set_2:
            # If the element is common, add it to the common set
            common_set.add(item)

    # Return the set of common elements
    return common_set
