#!/bin/usr/python3
"""Unittest for Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testrec_instances(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def test_isrec(self):
        self.assertIsInstance(Rectangle(10, 7), Base)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_w_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__width)

    def test_h_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__height)

    def test_y_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__y)

    def test_single_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_arg(self):
        rec = Rectangle(10, 7)
        rec2 = Rectangle(4, 8)
        self.assertNotEqual(rec.id, rec2.id)

    def test_three_arg(self):
        rec = Rectangle(10, 7, 2)
        rec2 = Rectangle(4, 8, 1)
        self.assertNotEqual(rec.id, rec2.id)

    def test_four_arg(self):
        rec = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(4, 2, 1, 3)
        self.assertNotEqual(rec.id, rec2.id)

    def test_five_arg(self):
        rec = Rectangle(10, 7, 2, 8, 4)
        rec2 = Rectangle(4, 2, 1, 3, 7)
        self.assertNotEqual(rec.id, rec2.id)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 7, 2, 8, 4, 1)

if __name__ == '__main__':
    unittest.main()
