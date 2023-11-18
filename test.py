#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import unittest
from is_even import is_even

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

if __name__ == "__main__":
    unittest.main()
