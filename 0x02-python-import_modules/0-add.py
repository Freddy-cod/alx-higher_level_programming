#!/usr/bin/python3
# This code adds two numbers together and prints the result.
from add_0 import add
if __name__ == "__main__":
    # Declare two variables, a and b, and assign them the values 1 and 2.
    a = 1
    b = 2
    # Print the result of the addition to the console.
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
