#!/usr/bin/python3
def best_score(my_dictionary):
    if not my_dictionary:
        return None
    maximum = max(my_dictionary.values())
    for key in my_dictionary.keys():
        if my_dictionary[key] == maximum:
            return key
