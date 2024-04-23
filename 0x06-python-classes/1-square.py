#!/usr/bin/python3
''' creates square and initiate size variable and
private size instance attribute '''


class Square:
    ''' private attribute size and initialize with size'''

    def __init__(self, size):
        ''' Args: size is the size of square '''
        self.__size = size
