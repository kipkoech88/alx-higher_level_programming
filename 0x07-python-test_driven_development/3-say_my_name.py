#!/usr/bin/python3
"""
Module that prints name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the first and last
    name. It takes two arguments
    first and last name that must
    be strings"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print('My name is {} {}'.format(first_name, last_name))
