#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maximum = my_list[0]
        for n in my_list:
            if n > maximum:
                maximum = n
        return maximum
    return None
