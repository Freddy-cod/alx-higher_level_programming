#!/usr/bin/python3

"""My functions for adding two numbers."""


def add_integer(a, b=98):
    """Outputs the addition of a and b.
       Raises an error if a and b aint numbers.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
