#!/usr/bin/python3
""" Create an  Rectangle object """


class Rectangle():
    """
    create an Rectangleo object
    with width and height
    """
    def __init__(self, width=0, height=0):
        """ initialize the Rectangle obj"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the wisth value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of the triangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string representation of the rectangle """
        string = ""

        if self.perimeter == 0:
            return string
        else:
            for i in range(0, self.height):
                for j in range(0, self.width):
                    string += "#"
                if i <= self.height - 1:
                    string += "\n"
        return string
