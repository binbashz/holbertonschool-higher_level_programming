#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0  # Var to keep track of the number of integers printed
    for i in range(0, x):  # Iterate over the specified range of x values
        try:
            print("{:d}".format(my_list[i]), end="")
            integer_count += 1  # Increment the count of printed integers
        except (ValueError, TypeError):  # Catch ValueErr or TypeError excep
            pass  # Skip non-integer elements silently
    print()  # Print a newline character
    return integer_count  # Return the count of integers printed
