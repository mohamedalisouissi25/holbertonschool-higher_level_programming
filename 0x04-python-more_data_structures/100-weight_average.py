#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        n = 0
        m = 0
        for k in my_list:
            n += (k[0] * k[1])
            m += k[1]
        return (n / m)
    return 0
