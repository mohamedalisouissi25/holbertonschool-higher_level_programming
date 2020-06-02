#!/usr/bin/python3
"""
A module that contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """if obj is the exact class a_class
    return true,
    otherwise false"""
    return type(obj) is a_class
