#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        print(' '.join("{:d}".format(digit) for digit in nums))
