import unittest
import PF_Packages.parser.PF_regex
from typing import TypeAlias, List

PF_Regex: TypeAlias = PF_Packages.parser.PF_regex.PF_Regex

class Test_test_PF_regex_find_all_nums(unittest.TestCase):
    """Class testing PF_Regex.find_all_nums()."""

    def test_find_damage_normal(self):
        """Tests regex if can find the 2 damage numbers given normal/expected input from user."""
        e: List[float] = [29, 19]
        data = "29 - 19"
        a: List[float] = PF_Regex.find_all_nums(data=data)
        self.assertListEqual(e, a)

if __name__ == '__main__':
    unittest.main()
