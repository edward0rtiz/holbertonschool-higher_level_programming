#!/bin/usr/python3
"""Unittest for Rectangle"""

import unittest
from models.base import Base
from models.square import Square

class Testsqr_instance(unittest.TestCase):
    """Type class unittest instance for sqr"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

if __name__ == '__main__':
    unittest.main()
