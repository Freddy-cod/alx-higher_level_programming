#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Iterate through the elements in the input list
    for num in my_list:
        # Print each integer using str.format()
        print("{:d}".format(num))
