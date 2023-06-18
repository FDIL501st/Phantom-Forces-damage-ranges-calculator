import unittest
from PF_Packages.parser.HitsToKillParser import HitsToKillParser
from PF_Packages.dataTypes import Hits


class Test_test_parse_tuple_to_string(unittest.TestCase):
    def test_parse_one_limb_shot(self) -> None:
        """Tests if correctly converts (0, 0, 1) to string."""
        expected: str = "0 | 0 | 1"
        hits: Hits = (0, 0, 1)
        actual: str = HitsToKillParser.convert_tuple_to_str(hits_tup=hits)
        self.assertEqual(expected, actual, msg=f"Did not parse {hits} correctly.")

    def test_parse_more_than_one_limb_shot(self) -> None:
        """Tests if correctly converts more than 1 limb shot to string."""
        expect1: str = "0 | 0 | 2"

        expect3: str = "0 | 0 | 7"

        hits1: Hits = (0, 0, 2)
        hits7: Hits = (0, 0, 7)

        actual1: str = HitsToKillParser.convert_tuple_to_str(hits1)

        actual3: str = HitsToKillParser.convert_tuple_to_str(hits7)

        self.assertEqual(expect1, actual1, msg=f"Did not parse {hits1} correctly.")

        self.assertEqual(expect3, actual3, msg=f"Did not parse {hits7} correctly.")

    def test_parse_one_torso_shot(self) -> None:
        """Tests if correctly converts (0, 1, 0)."""
        hits: Hits = (0, 1, 0)

        e1: str = "0 | 1 | 0"
        a1: str = HitsToKillParser.convert_tuple_to_str(hits_tup=hits)
        self.assertEqual(e1, a1, msg=f"Did not parse {hits} correctly.")

    def test_parse_more_than_one_torso_shots(self) -> None:
        """Tests if correctly converts when have more than 1 torso shots."""
        hits2: Hits = (0, 2, 0)
        hits4: Hits = (0, 4, 0)

        e: str = "0 | 2 | 0"
        a: str = HitsToKillParser.convert_tuple_to_str(hits_tup=hits2)
        self.assertEqual(e, a, msg=f"Did not parse {hits2} correctly.")

        e = "0 | 4 | 0"
        a = HitsToKillParser.convert_tuple_to_str(hits4)
        self.assertEqual(e, a, msg=f"Did not parse {hits4} correctly.")

    def test_parse_torso_limb_combination_shots(self) -> None:
        """Tests hits that are combinations of torso and limb shots."""
        hits_1_3: Hits = (0, 1, 3)
        hits_2_2: Hits = (0, 2, 2)
        hits_3_2: Hits = (0, 3, 2)

        e: str = "0 | 1 | 3"
        a: str = HitsToKillParser.convert_tuple_to_str(hits_1_3)
        self.assertEqual(e, a, msg=f"Did not parse {hits_1_3} correctly.")

        e = "0 | 2 | 2"
        a = HitsToKillParser.convert_tuple_to_str(hits_2_2)
        self.assertEqual(e, a, msg=f"Did not parse {hits_2_2} correctly.")

        e = "0 | 3 | 2"
        a = HitsToKillParser.convert_tuple_to_str(hits_3_2)
        self.assertEqual(e, a, msg=f"Did not parse {hits_3_2} correctly.")

    def test_parse_headshots_only(self) -> None:
        """Tests hits that are headshots only. This include 1 headshot, and many headshots."""
        hits1: Hits = (1, 0, 0)
        hits3: Hits = (3, 0, 0)

        e: str = "1 | 0 | 0"
        a: str = HitsToKillParser.convert_tuple_to_str(hits1)
        self.assertEqual(e, a, msg=f"Did not parse {hits1} correctly.")

        e = "3 | 0 | 0"
        a = HitsToKillParser.convert_tuple_to_str(hits3)
        self.assertEqual(e, a, msg=f"Did not parse {hits3} correctly.")

    def test_parse_head_limb_combination_shots(self) -> None:
        """Tests hits that are combinations of head and limb shots."""
        hits_1_2: Hits = (1, 0, 2)
        hits_2_1: Hits = (2, 0, 1)
        hits_3_2: Hits = (3, 0, 2)

        e: str = "1 | 0 | 2"
        a: str = HitsToKillParser.convert_tuple_to_str(hits_1_2)
        self.assertEqual(e, a, msg=f"Did not parse {hits_1_2} correctly.")

        e = "2 | 0 | 1"
        a = HitsToKillParser.convert_tuple_to_str(hits_2_1)
        self.assertEqual(e, a, msg=f"Did not parse {hits_2_1} correctly.")

        e = "3 | 0 | 2"
        a = HitsToKillParser.convert_tuple_to_str(hits_3_2)
        self.assertEqual(e, a, msg=f"Did not parse {hits_3_2} correctly where torso multi != 1")

    def test_parse_head_torso_combination_shots(self) -> None:
        """Tests hits that are combinations of head and torso shots."""
        hits_1_4: Hits = (1, 4, 0)
        hits_2_3: Hits = (2, 3, 0)
        hits_3_1: Hits = (3, 1, 0)

        # Whenever torso multi is 1, expect to ignore torso shots

        e: str = "1 | 4 | 0"
        a: str = HitsToKillParser.convert_tuple_to_str(hits_1_4)
        self.assertEqual(e, a, msg=f"Did not parse {hits_1_4} correctly.")

        e = "2 | 3 | 0"
        a = HitsToKillParser.convert_tuple_to_str(hits_2_3)
        self.assertEqual(e, a, msg=f"Did not parse {hits_2_3} correctly.")

        e = "3 | 1 | 0"
        a = HitsToKillParser.convert_tuple_to_str(hits_3_1)
        self.assertEqual(e, a, msg=f"Did not parse {hits_3_1} correctly.")

    def test_parse_head_torso_limb_combination_shots(self) -> None:
        """Tests hits that are combinations of head, torso and limb shots."""
        hits_1_1_3: Hits = (1, 1, 3)
        hits_1_3_2: Hits = (1, 3, 2)
        hits_2_2_1: Hits = (2, 2, 1)
        hits_2_1_1: Hits = (2, 1, 1)
        hits_3_1_1: Hits = (3, 1, 1)
        hits_3_1_2: Hits = (3, 1, 2)

        e: str = "1 | 1 | 3"
        a: str = HitsToKillParser.convert_tuple_to_str(hits_1_1_3)
        self.assertEqual(e, a, msg=f"Did not parse {hits_1_1_3} correctly.")

        e = "1 | 3 | 2"
        a = HitsToKillParser.convert_tuple_to_str(hits_1_3_2)
        self.assertEqual(e, a, msg=f"Did not parse {hits_1_3_2} correctly.")

        e = "2 | 2 | 1"
        a = HitsToKillParser.convert_tuple_to_str(hits_2_2_1)
        self.assertEqual(e, a, msg=f"Did not parse {hits_2_2_1} correctly.")

        e = "2 | 1 | 1"
        a = HitsToKillParser.convert_tuple_to_str(hits_2_1_1)
        self.assertEqual(e, a, msg=f"Did not parse {hits_2_1_1} correctly.")

        e = "3 | 1 | 1"
        a = HitsToKillParser.convert_tuple_to_str(hits_3_1_1)
        self.assertEqual(e, a, msg=f"Did not parse {hits_3_1_1} correctly.")

        e = "3 | 1 | 2"
        a = HitsToKillParser.convert_tuple_to_str(hits_3_1_2)
        self.assertEqual(e, a, msg=f"Did not parse {hits_3_1_2} correctly.")


if __name__ == '__main__':
    unittest.main()
