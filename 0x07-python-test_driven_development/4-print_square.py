#!/usr/bin/python
"""
This module prints square from given value
"""


def print_square(size):
    """
    the `print_square` function
    takes size arg and checks if
    it is an integer and if not throw
    error else prints square of X
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(0, size):
            print('X' * size)
