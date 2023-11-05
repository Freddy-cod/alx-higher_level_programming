#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through the rows of the matrix
    for row in matrix:
        # Iterate through the elements in each row
        for element in row:
            # Print each element with formatting
            print("{:d}".format(element), end=" ")
        print()  # Move to the next line after each row
