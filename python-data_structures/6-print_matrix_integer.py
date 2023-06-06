#!/usr/bin/python3
def print_updated_matrix(updated_matrix=[[]]):
    for row in updated_matrix:
        for element in row:
            print("{:d} ".format(element), end='')
        print()
