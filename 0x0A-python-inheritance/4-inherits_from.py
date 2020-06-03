#!/usr/bin/python3
"""
The inherits_from function
"""


def inherits_from(obj, a_class):
    """If obj is a subclass of a_class,
    retur true,
    otherwise false"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
