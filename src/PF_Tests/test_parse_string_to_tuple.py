from unittest import TestCase

from PF_Packages.parser.HitsToKillParser import HitsToKillParser
from PF_Packages.dataTypes import Hits


class TestParseStringToTuple(TestCase):
    def test_convert_str_to_tuple_correct_format(self):
        # Tests correct format of argument passed
        hits1_str: str = "0 | 3 | 1"
        hits1_tup: Hits = (0, 3, 1)

        hits2_str: str = "1 | 0 | 4"
        hits2_tup: Hits = (1, 0, 4)

        hits3_str: str = "0 | 0 | 5"
        hits3_tup: Hits = (0, 0, 5)

        hits4_str: str = "1 | 2 | 2"
        hits4_tup: Hits = (1, 2, 2)

        self.assertEqual(hits1_tup, HitsToKillParser.convert_str_to_tuple(hits1_str),
                         msg="hits1 failed to convert")

        self.assertEqual(hits2_tup, HitsToKillParser.convert_str_to_tuple(hits2_str),
                         msg="hits2 failed to convert")

        self.assertEqual(hits3_tup, HitsToKillParser.convert_str_to_tuple(hits3_str),
                         msg="hits3 failed to convert")

        self.assertEqual(hits4_tup, HitsToKillParser.convert_str_to_tuple(hits4_str),
                         msg="hits4 failed to convert")

    def test_convert_str_to_tuple_incorrect_format(self):
        # Tests incorrect format for argument passed
        # Expect an Exception to be raised

        hits_incorrect: str = "1 headshot, 2 limb shots"
        with self.assertRaises(ValueError):
            HitsToKillParser.convert_str_to_tuple(hits_incorrect)

