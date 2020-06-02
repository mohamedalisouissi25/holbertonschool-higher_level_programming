#!/usr/bin/python3


def is_same_class(obj, a_class):
    """if obj is the exact class a_class
    return true,
    otherwise false"""
    return type(obj) is a_class
