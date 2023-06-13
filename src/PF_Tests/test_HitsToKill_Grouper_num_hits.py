from unittest import TestCase
from PF_Packages.dataTypes import Hits
from PF_Packages.dict_sorter.HitsToKill_Grouper import num_hits


class TestNumHits(TestCase):
    def test_num_hits(self):
        hits1: Hits = (0, 0, 4)
        hits2: Hits = (1, 2, 2)
        hits3: Hits = (0, 1, 6)

        self.assertEqual(4, num_hits(hits1),
                         msg="Incorrect sum of hits1")

        self.assertEqual(5, num_hits(hits2),
                         msg="Incorrect sum of hits2")

        self.assertEqual(7, num_hits(hits3),
                         msg="Incorrect sum of hits3")
