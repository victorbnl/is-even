#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import unittest
from is_even import isEven

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(isEven(0))
        self.assertFalse(isEven(1))
        self.assertTrue(isEven(2))
        self.assertFalse(isEven(3))

if __name__ == "__main__":
    unittest.main()
