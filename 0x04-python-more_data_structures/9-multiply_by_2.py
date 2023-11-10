#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary
    new_dict = {}

    for key, value in a_dictionary.items():
        # Multiply each
        new_dict[key] = value * 2

    return new_dict
