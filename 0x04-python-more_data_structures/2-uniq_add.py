#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()

    for number in my_list:
        unique_set.add(number)

    total = sum(unique_set)

    return total
