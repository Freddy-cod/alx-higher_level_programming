#!/usr/bin/python3
# This code adds two numbers together and prints the result.

from add_0 import add

if __name__ == "__main__":
    # Declare two variables, a and b, and assign them the values 1 and 2.
    a = 1
    b = 2

    # Add the two numbers together and store the result in the variable result.
    result = add(a, b)

    # Print the result of the addition to the console.
    print("{} + {} = {}".format(a, b, result))