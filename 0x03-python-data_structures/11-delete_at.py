#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list for invalid indices

    # Create a new list with elements before and after the specified index
    new_list = my_list[:idx] + my_list[idx+1:]

    return new_list
