#!/usr/bin/python3
""" class base geometry module """


class BaseGeometry(object):
    """ empty base geometry class """
    def area(self):
        """ exception whith a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' cheks for value '''
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
