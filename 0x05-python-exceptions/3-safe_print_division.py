#!/usr/bin/python3

def safe_print_division(a, b):
    # Handle 0-division, value, and type error.
    try:
        div = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
