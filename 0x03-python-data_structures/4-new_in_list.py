#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Returncopy of original list 4 invalid indices
    else:
        new_list = my_list.copy()  # Create a copy of the original list
        new_list[idx] = element  # Replace the element at the specified index
        return new_list  # Return the modified copy
