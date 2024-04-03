#!/usr/bin/python3

def safe_print_integer(value):
    # Handle Value and Type Errors
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
