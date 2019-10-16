#!/usr/bin/python3


class MyInt(int):
    """Type class of MyInt inherit int type"""

    def __eq__(self, other):

        return self.real != other

    def __ne__(self, other):

        return self.real == other
