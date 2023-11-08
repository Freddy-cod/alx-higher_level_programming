#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_diff_set = set()

    # Find elements in set_1 but not in set_2
    for element in set_1:
        if element not in set_2:
            only_diff_set.add(element)

    # Find elements in set_2 but not in set_1
    for element in set_2:
        if element not in set_1:
            only_diff_set.add(element)

    return only_diff_set
