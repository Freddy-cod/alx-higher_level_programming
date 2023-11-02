#!/usr/bin/python3
# This code adds two numbers together and prints the result.

from add_0 import add

if __name__ == "__main__":
    # Declare two variables, num1 and num2, and assign them the values 1 and 2.
    num1 = 1
    num2 = 2

    # Add the two numbers together and store the result in the variable result.
    result = add(num1, num2)

    # Print the result of the addition to the console.
    print("{} + {} = {}".format(num1, num2, result))

