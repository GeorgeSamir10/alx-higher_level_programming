#!/usr/bin/python3
"""
This module defines the Square class that represents
a square with a specific size and position.
"""


class Square:
    """
    Represents a square with a specific size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The (x, y) coordinates of the
            top-left corner of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#'
        character, considering the position.
        """
        if self.__size == 0:
            print()
        else:
            x, y = self.__position
            for _ in range(y):
                print()
            for _ in range(self.__size):
                print(' ' * x + '#' * self.__size)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If `value` is not a tuple of two integers.
            ValueError: If any element of `value` is negative.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
