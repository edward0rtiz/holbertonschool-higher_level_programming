#!/usr/bin/python3
class Square:
    """Type class square"""
    def __init__(self, size):
        """Init the square class
        Args:
        param1: size is the type int attribute to make it private
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """private attribute to get the size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
