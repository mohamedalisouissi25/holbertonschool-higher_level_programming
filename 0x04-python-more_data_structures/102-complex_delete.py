#!/usr/bin/python3
def complex_delete(my_dictionary, value):
    keys_to_del = []
    for key in my_dictionary:
        if my_dictionary[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del my_dictionary[key]
    return my_dictionary
