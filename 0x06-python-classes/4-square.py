#!/usr/bin/python3
"""
Module defines A class of Name Square which defines a square.
"""


class Square:
    """
    Empty class named Square defines a square.
    """
    def __init__(self, size=0):
        """
        Method initiates an object instance of class Square.
        Args:
            size (int): size of the square to be initiated.
        """
        self.size = size

    def area(self):
        """
        Method calculates & returns the area of a square
        Returns:
            int value of the area of the square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter method for the private attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method sets the value of private attribute size after
        checking its value and type.

        Args:
            value (int): the value to be tested before assigning it to the
            prive attribute size.
        """
        if value:
            if type(value) is int:
                if (value > 0):
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        else:
            self.__size = 0
