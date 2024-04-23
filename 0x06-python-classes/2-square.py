#!/usr/bin/python3
''' class for Square object '''


class Square:
    ''' This is a class that defines a square '''

    def __init__(self, size=0):
        ''' The object is initialized with 1 attr
        size which default value is 0
        and supposed to work even when the programmer
        forgets to initialize with a value'''
        self.__size = size

        ''' the size must be an integer otherwise TypeError is
        raised'''
        if (type(self.__size) is not int):
            raise TypeError('size must be an integer')
        elif (self.__size < 0):
            raise ValueError('size must be >= 0')
