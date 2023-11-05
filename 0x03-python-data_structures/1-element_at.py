#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None  # Return None for invalid indices
    else:
        return my_list[idx]  # Retrieve and return the element atindex
