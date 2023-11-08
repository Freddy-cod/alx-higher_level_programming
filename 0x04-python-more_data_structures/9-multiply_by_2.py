#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}  # Create a new dictionary

    for key, value in a_dictionary.items():
        new_dict[key] = value * 2  # Multiply each 

    return new_dict
