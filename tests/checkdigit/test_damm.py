# Copyright (c) 2025 Luis A. Ochoa. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <LICENSE>.

import unittest

from parameterized import parameterized
from checkdigit.damm import DammAlgorithm as damm

class DammTestCase(unittest.TestCase):

    @parameterized.expand([
        ("0", "00"),
        ("1", "13"),
        ("231", "2312"),
        ("739964", "7399641"),
        ("28041986", "280419866"),
        ("519664633801", "5196646338010"),
        ("22653775129265104212", "226537751292651042123")
    ])
    def test_generate(self, case, expected):
        self.assertEqual(expected, damm.generate(case))

    @parameterized.expand([
        (True, "00"),
        (True, "13"),
        (True, "2312"),
        (True, "7399641"),
        (True, "280419866"),
        (True, "5196646338010"),
        (True, "226537751292651042123"),
        (False, "5"),
        (False, "01"),
        (False, "16"),
        (False, "2310"),
        (False, "7399642"),
        (False, "280419869"),
        (False, "5196646338013"),
        (False, "226537751292651042127")
    ])
    def test_is_valid(self, expected, case):
        self.assertEqual(expected, damm.is_valid(case))

if __name__ == '__main__':
    unittest.main()
