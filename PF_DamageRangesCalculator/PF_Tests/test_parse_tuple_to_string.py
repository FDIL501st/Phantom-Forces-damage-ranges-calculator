import unittest
from typing import TypeAlias
from PF_Packages.parser.HitsToKillParser import HitsToKillParser
from PF_Packages.dataTypes import Hits


class Test_test_parse_tuple_to_string(unittest.TestCase):
    def test_parse_one_limb_shot(self) -> None:
        """Tests if correctly converts (0, 0, 1) to string."""
        expected: str = "1 limb shot"
        hits: Hits = (0, 0, 1)
        actual: str = HitsToKillParser.convert_tuple_to_str(hits=hits)
        self.assertEqual(expected, actual, msg=f"Did not parse {hits} correctly with torso multi != 1.")

        expected = "1 torso/limb shot"
        actual = HitsToKillParser.convert_tuple_to_str(hits=hits, torso_multi_is_one=True)
        self.assertEqual(expected, actual, msg=f"Did not parse {hits} correctly with torso multi == 1.")
        

    def test_parse_more_than_one_limb_shot(self) -> None:
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

    def test_parse_one_torso_shot(self) -> None:
        """Tests if correctly converts (0, 1, 0)."""
        hits: Hits = (0, 1, 0)

        e1: str = "1 torso shot"
        a1: str = HitsToKillParser.convert_tuple_to_str(hits=hits)
        self.assertEqual(e1, a1, msg=f"Did not parse {hits} correctly with torso multi != 1.")

        e2: str = ""
        a2: str = HitsToKillParser.convert_tuple_to_str(hits=hits, torso_multi_is_one=True)
        self.assertEqual(e2, a2, msg=f"Did not parse {hits} correctly with torso multi == 1.")
    
    def test_parse_more_than_one_torso_shots(self) -> None:
        """Tests if correctly converts when have more than 1 torso shots."""
        hits2: Hits = (0, 2, 0)
        hits4: Hits = (0, 4, 0)

        e: str = "2 torso shots"
        a: str = HitsToKillParser.convert_tuple_to_str(hits=hits2)
        self.assertEqual(e, a, msg=f"Did not parse {hits2} correctly with torso multi != 1.")

        e = ""
        a = HitsToKillParser.convert_tuple_to_str(hits2, True)
        self.assertEqual(e, a, msg=f"Did not parse {hits2} correctly with torso multi == 1.")

        e = "4 torso shots"
        a = HitsToKillParser.convert_tuple_to_str(hits=hits4)
        self.assertEqual(e, a, msg=f"Did not parse {hits4} correctly with torso multi != 1.")

        e = ""
        a = HitsToKillParser.convert_tuple_to_str(hits4, True)
        self.assertEqual(e, a, msg=f"Did not parse {hits4} correctly with torso multi == 1.")

    def test_parse_torso_limb_combination_shots(self) -> None:
        """Tests hits that are combinations of torso and limb shots."""
        pass
if __name__ == '__main__':
    unittest.main()
