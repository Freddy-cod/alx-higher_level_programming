#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())  # Sort the keys alphabetically
    
    for key in sorted_keys:
        value = a_dictionary[key]
        
        if isinstance(value, dict):
            # If the value is another dictionary, print its keys without sorting
            print(key, ": {")
            for subkey, subvalue in value.items():
                print(f"    {subkey}: {subvalue}")
            print("}")
        else:
            # Print the key and its value
            print(key, ":", value)
