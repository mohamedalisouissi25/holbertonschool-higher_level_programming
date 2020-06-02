#!/usr/bin/python3
"""
the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """If obj is an instance or inherited from a_class
    return true,
    else False"""
    return isinstance(obj, a_class)
