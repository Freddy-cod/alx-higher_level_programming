#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize a new list to store True or False values
    result = []

    # Iterate through the elements in the original list
    for num in my_list:
        if num % 2 == 0:  # Check if the element is a multiple of 2
            result.append(True)  # Add True to the new list if it's a multiple2
        else:
            result.append(False)  # Add False to the new list if it's not a

    return result
