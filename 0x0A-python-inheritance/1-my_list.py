#!/usr/bin/python3


"""
subclass class
"""


class MyList(list):
    """inheritance of list base class"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
