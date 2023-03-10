import unittest
from typing import TypeAlias

import PF_DamageRangesCalculator

PF_Regex: TypeAlias = PF_DamageRangesCalculator.PF_Packages.parser.PF_regex.PF_Regex

class Test_test_PF_regex_match_one_non_zero_num(unittest.TestCase):   
    """Class testing PF_Regex.match_one_pos_num()."""

    def test_one_pos_num(self):
        """Tests regex if correctly able to match data that has only 1 positive number.
        Data could represent typing in multis."""

        e = True
        msg = "Did not correctly match the 1 positive number provided."
        data = "1.0"
        a = PF_Regex.match_one_non_zero_num(data=data)
        self.assertEqual(e, a, msg=msg)

        data = "1.4"
        a = PF_Regex.match_one_non_zero_num(data=data)
        self.assertEqual(e, a, msg=msg)
    
    def test_zero(self):
        """Tests regex if correctly fails to match providing only a 0.
        Data could represent an accident on user end in typing invalid multi of 0."""

        e = False
        msg = "Did not correctly fail match of 0."
        data = "0"
        a = PF_Regex.match_one_non_zero_num(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_ignore_neg_num(self):
        """Tests regex if ignores the '-' and still matches the number."""
        e = True
        msg = "Did not correctly match the number."
        data = "-23"
        a = PF_Regex.match_one_non_zero_num(data=data)
        self.assertEqual(e, a, msg=msg) 

if __name__ == '__main__':
    unittest.main()
