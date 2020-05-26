#!/usr/bin/python3
   """
   A Locked class
   """
class LockedClass:
    """
    A class that prevents the user from dynamically creating
    new instance attributes
    """
    __slots__ = ['first_name']
