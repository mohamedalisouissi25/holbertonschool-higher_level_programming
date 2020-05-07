#!/usr/bin/python3
def print_sorted_dictionary(my_dictionnary):
    for key in sorted(my_dictionnary.keys()):
        print("{:s}: {}".format(key, my_dictionnary[key]))
