#!/usr/bin/python3
""" `add_integer` module
Adds two integers and return an integer value
This modules checks for the inputs to make sure that
integers are passed and raise errors when it fails
"""


def add_integer(a, b=98):
    """ Adds two integers a and b
    all args passed shoud be integers
    it can take one argument and that will be a and
    auto assign be to 98
    """
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    else:
        n = int(a)
        m = int(b)

    return (n + m)
