#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the characters in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char != 'c' and char != 'C':
            # If not, add it to the result string
            result += char

    # Return the result string without 'c' and 'C'
    return result
