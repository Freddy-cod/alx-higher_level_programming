#!/usr/bin/python3
"""find the max"""


def find_peak(list_of_integers):
    """find_peak"""
    if not len(list_of_integers):
        return None
    else:
        return max(list_of_integers)
