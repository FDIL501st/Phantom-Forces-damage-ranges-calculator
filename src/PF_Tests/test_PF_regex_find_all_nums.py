import unittest
from typing import TypeAlias, List

from PF_Packages.parser import PF_regex

PF_Regex: TypeAlias = PF_regex.PF_Regex

class Test_test_PF_regex_find_all_nums(unittest.TestCase):
    """Class testing PF_Regex.find_all_nums()."""

    def test_find_damage_normal(self):
        """Tests regex if can find the 2 damage numbers given normal/expected input from user."""
        e: List[float] = [29, 19]
        data = "29 - 19"
        a: List[float] = PF_Regex.find_all_nums(data=data)
        self.assertListEqual(e, a)

    def test_find_reverse_damage_normal(self):
        """Tests regex if can find 2 damage numbers if given reverse damage in normal/expected format from user.
        This test is more about the order of numbers being found to be correct, which is should be considering that 
        lies on the regex library than code within this function."""
        e = [34, 45]
        data = "34 - 45"
        a = PF_Regex.find_all_nums(data=data)
        self.assertListEqual(e, a)
    
    def test_ignore_words(self):
        """Tests regex if can ignore words and only finds the numbers.
        Can represent user input with extra uneeded information typed in."""

        e = [33.3, 24]
        data = "33.3 - 24 damage"
        a = PF_Regex.find_all_nums(data=data)
        self.assertListEqual(e, a)

    def test_ignore_neg_nums(self):
        """Tests regex if ignores any negative numbers and only finds the absolute values."""
        e = [34, 24]
        data = "-34-24"
        a = PF_Regex.find_all_nums(data=data)
        self.assertListEqual(e, a)
        
if __name__ == '__main__':
    unittest.main()
