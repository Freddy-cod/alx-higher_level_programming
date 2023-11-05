#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Iterate through the elements in the reversed list
    for num in reversed(my_list):
        print("{:d}".format(num))
