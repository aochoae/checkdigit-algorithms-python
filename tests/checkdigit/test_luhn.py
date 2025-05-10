# Copyright (c) 2025 Luis A. Ochoa. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <LICENSE>.

import unittest

from parameterized import parameterized
from checkdigit.luhn import LuhnAlgorithm as luhn

class LuhnTestCase(unittest.TestCase):

    @parameterized.expand([
        ("0", "00"),
        ("1", "18"),
        ("231", "2311"),
        ("739964", "7399645"),
        ("28041986", "280419862"),
        ("37185048010235", "371850480102358"),
        ("22653775129265104212", "226537751292651042122")
    ])
    def test_generate(self, case, expected):
        self.assertEqual(expected, luhn.generate(case))

    @parameterized.expand([
        (True, "00"),
        (True, "18"),
        (True, "2311"),
        (True, "7399645"),
        (True, "280419862"),
        (True, "371850480102358"),
        (True, "226537751292651042122"),
        (False, "5"),
        (False, "09"),
        (False, "12"),
        (False, "2319"),
        (False, "7399642"),
        (False, "280419860"),
        (False, "371850480102352"),
        (False, "226537751292651042124")
    ])
    def test_is_valid(self, expected, case):
        self.assertEqual(expected, luhn.is_valid(case))

if __name__ == '__main__':
    unittest.main()
