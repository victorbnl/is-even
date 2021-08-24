#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import unittest
from is_even import isEven

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(isEven(0))
        self.assertTrue(isEven(1))
        self.assertFalse(isEven(2))
        self.assertTrue(isEven(4))

if __name__ == "__main__":
    unittest.main()
