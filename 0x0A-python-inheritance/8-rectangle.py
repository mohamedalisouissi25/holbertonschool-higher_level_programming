#!/usr/bin/python3
"""
The subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ empty class of rectangle """
    def __init__(self, width, height):
        """ the rectangle instantiation """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
