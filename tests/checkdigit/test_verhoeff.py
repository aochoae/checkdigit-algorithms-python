# Copyright (c) 2025 Luis A. Ochoa. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <LICENSE>.

import unittest

from parameterized import parameterized
from checkdigit.verhoeff import VerhoeffAlgorithm as verhoeff

class VerhoeffTestCase(unittest.TestCase):

    @parameterized.expand([
        ("0", "04"),
        ("1", "15"),
        ("231", "2316"),
        ("739964", "7399648"),
        ("28041986", "280419865"),
        ("519664633801", "5196646338015"),
        ("22653775129265104212", "226537751292651042125")
    ])
    def test_generate(self, case, expected):
        self.assertEqual(expected, verhoeff.generate(case))

    @parameterized.expand([
        (True, "04"),
        (True, "15"),
        (True, "2316"),
        (True, "7399648"),
        (True, "280419865"),
        (True, "5196646338015"),
        (True, "226537751292651042125"),
        (False, "5"),
        (False, "01"),
        (False, "16"),
        (False, "2313"),
        (False, "7399649"),
        (False, "280419864"),
        (False, "5196646338017"),
        (False, "226537751292651042122")
    ])
    def test_is_valid(self, expected, case):
        self.assertEqual(expected, verhoeff.is_valid(case))

if __name__ == '__main__':
    unittest.main()
