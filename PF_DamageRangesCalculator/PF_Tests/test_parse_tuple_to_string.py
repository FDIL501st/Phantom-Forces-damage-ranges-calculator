import unittest
from typing import TypeAlias
from PF_Packages.parser.HitsToKillParser import HitsToKillParser
from PF_Packages.dataTypes import Hits


class Test_test_parse_tuple_to_string(unittest.TestCase):
    def test_parse_one_limb_shot(self):
        """Tests if correctly converts (0, 0, 1) to string."""
        expected: str = "1 limb shot"
        hits: Hits = (0, 0, 1)
        actual: str = HitsToKillParser.convert_tuple_to_str(hits=hits)
        self.assertEqual(expected, actual, msg=f"Did not parse {hits} correctly with torso multi != 1.")

        expected = "1 torso/limb shot"
        actual = HitsToKillParser.convert_tuple_to_str(hits=hits, torso_multi_is_one=True)
        self.assertEqual(expected, actual, msg=f"Did not parse {hits} correctly with torso multi == 1.")
        

    def test_parse_more_than_one_limb_shot(self):
        """Tests if correctly converts more than 1 limb shot to string."""
        expect1: str = "2 limb shots"
        expect2: str = "2 torso/limb shots"

        expect3: str = "7 limb shots"
        expect4: str = "7 torso/limb shots"

        hits1: Hits = (0,0,2)
        hits7: Hits = (0,0,7)

        actual1: str = HitsToKillParser.convert_tuple_to_str(hits1)
        actual2: str = HitsToKillParser.convert_tuple_to_str(hits1, True)

        actual3: str = HitsToKillParser.convert_tuple_to_str(hits7)
        actual4: str = HitsToKillParser.convert_tuple_to_str(hits7, True)

        self.assertEqual(expect1, actual1, msg=f"Did not parse {hits1} correctly with torso multi != 1.")
        self.assertEqual(expect2, actual2, msg=f"Did not parse {hits1} correctly with torso multi == 1.")

        self.assertEqual(expect3, actual3, msg=f"Did not parse {hits7} correctly with torso multi != 1.")
        self.assertEqual(expect4, actual4, msg=f"Did not parse {hits7} correctly with torso multi == 1.")

if __name__ == '__main__':
    unittest.main()
