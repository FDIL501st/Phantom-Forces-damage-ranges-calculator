import unittest
from typing import TypeAlias

import src.PF_Packages

PF_Regex: TypeAlias = src.PF_Packages.parser.PF_regex.PF_Regex


class Test_test_PF_regex_match_two_nums(unittest.TestCase):
    """Class testing PF_Regex.match_two_non_neg_nums()."""

    def test_two_pos_nums_reg(self):
        """Tests regex it correctly matches 2 positive numbers.
        Data used is what is expected to be the norm."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data: str = "23 - 45"
        a: bool = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_right_space(self):
        """Tests regex it correctly matches 2 positive numbers.
        Data is when someone forgets to add a space to left side of '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data: str = "23 -120"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_left_space(self):
        """Tests regex it correctly matches 2 positive numbers.
        Data is when someone forgets to add a space to right side of '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data: str = "23 -120"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_two_hypens(self):
        """Tests regex it correctly matches 2 positive numbers.
        Data is when someone accidently double types '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data: str = "12.394 --54.33"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_whole_no_hyphen(self):
        """Tests regex it correctly matches 2 positive numbers, no decimals.
        Data is when someone forgets the '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data: str = "124 22"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_decimals_no_hyphen(self):
        """Tests regex it correctly matches 2 positive numbers, decimals.
        Data is when someone forgets the '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data = "12.55 22.90"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_whole_no_space(self):
        """Tests regex it correctly matches 2 positive numbers without decimals.
        Data is when someone puts no space with '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data = "12-54"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_decimals_no_space(self):
        """Tests regex it correctly matches 2 positive numbers with decimals.
        Data is when someone puts no space with '-'."""
        e: bool = True
        msg = "Did not correctly match 2 positive numbers."
        data = "12-54.33"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_non_nums_many_decimals(self):
        """Tests regex if corrently unable to match data that has more than 1 decimal.
        Data represents when someone accidently puts in more than 1 decimals."""
        e: bool = False
        msg = "Did not correctly not match having incorrect numbers."
        data = "12 - 54.33.44"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

        data = "12..45 - 54"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_non_nums_alphabets(self):
        """Tests regex if correctly unable to match data that has alphabets.
        Data represents when someone types in garbage."""
        e: bool = False
        msg = "Did not correctly not match having not numbers."
        data = "ahdf - 123.34"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

        data = "fifty - sixty"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_zero(self):
        """Tests regex if correctly able to match data that has a 0.
        Depleted uranium makes damage range 0-150 for example.
        """
        e: bool = True
        msg = "Did not correctly match 0 as a number."
        data = "0 - 150"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_two_pos_nums_with_words(self):
        """Tests regex if correctly able to match data that has the 2 numbers, with words.
        Data could represent rare cases where user decides to use words(like unit) as well with their two numbers.
        Regex should still be able to match the numbers."""

        e: bool = True
        msg = "Did not correctly match the 2 positive numbers."
        data = "30 studs - 45 studs"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

        data = "110.5 - 100 damage"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_more_than_two_pos_nums(self):
        """Tests regex if correctly fails to match data that has more than 2 positive numbers.
        Data could represent user typing in more than 2 numbers accidently."""
        e: bool = False
        msg = "Did not correctly fail match the 3 numbers provided."
        data = "10 - 80 - 134"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)

    def test_one_pos_num_for_two_pos_nums(self):
        """Tests regex if correctly fails to match data that has only 1 positive number, when 2 was expected.
        Data could represent user putting multis in wrong field, or forgetting to put in second number."""
        e: bool = False
        msg = "Did not correctly fail match of provided 1 number, when 2 was expected."
        data = "40 studs"
        a = PF_Regex.match_two_nums(data=data)
        self.assertEqual(e, a, msg=msg)


if __name__ == '__main__':
    unittest.main()
