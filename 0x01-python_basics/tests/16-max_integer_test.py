#!/usr/bin/python3
""" 16-max_integer_test.py - test file for 16-max_integer.py
Test function
   def max_integer(list=[]):
Test with
   $ python3 -m unittest tests.16-max_integer_test
"""

import unittest


max_integer = __import__('16-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """"""
    def testFindMaxPosNum(self):
        """"""
        self.assertEqual(max_integer([1, 100, 0]), 100)

    def testFindMaxMixNum(self):
        """"""
        self.assertEqual(max_integer([-999, -100, 0, 5]), 5)

    def testFindMaxMixNumAtBeginning(self):
        """"""
        self.assertEqual(max_integer([800, -100, 0, 5]), 800)

    def testFindMaxMixNumAtEnd(self):
        """"""
        self.assertEqual(max_integer([800, -100, 0, 99999]), 99999)

    def testFindMaxSameInput(self):
        """"""
        self.assertEqual(max_integer([-7, -7, -7]), -7)

    def testFindMaxNoInput(self):
        """"""
        self.assertEqual(max_integer([]), None)

    def testFindMaxAllZeros(self):
        """"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()
