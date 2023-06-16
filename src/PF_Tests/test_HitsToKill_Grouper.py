from unittest import TestCase
from sortedcontainers import SortedDict
from PF_Packages.dict_sorter.HitsToKill_Grouper import HitsToKill_Grouper
from PF_Packages.dict_sorter.HitsToKill_Sorter import HitsToKillSorter


class TestHitsToKill_Grouper(TestCase):

    def setUp(self) -> None:
        # make an empty HitsToKill_Grouper object
        # this will be what will be tested on
        # tests need to insert data themselves
        self.hits_to_kill_grouped: HitsToKill_Grouper = HitsToKill_Grouper()

    def test_hit_groups(self):
        # this tests the getter

        # expect for the dict to be empty
        empty_SortedDict: SortedDict = SortedDict()
        self.assertEqual(empty_SortedDict, self.hits_to_kill_grouped.hit_groups,
                         msg="Getter didn't return an empty SortedDict object")

    # tests below are dependent on the test above to pass
    def test_insert_new_key(self):
        # tests the insert with a new key
        self.hits_to_kill_grouped.insert("3 | 0 | 0", 200)

        self.assertIn(3, self.hits_to_kill_grouped.hit_groups,
                      msg="Did not add new key, 3")

        # need to test being able to get the HitsToKill_Sorter as well
        self.assertIsNotNone(self.hits_to_kill_grouped.hit_groups[3],
                             msg="Did not create HitsToKill_Sorter object.")

        hits_to_kill_sorted: HitsToKillSorter = HitsToKillSorter()
        hits_to_kill_sorted.insert("3 | 0 | 0", 200)

        self.assertEqual(self.hits_to_kill_grouped.hit_groups[3].sorted_HitsToKill,
                         hits_to_kill_sorted.sorted_HitsToKill,
                         msg="Did not make the same list.")

    # test below is dependent on test above to pass
    def test_insert_existing_key(self):
        # tests the insert into a existing key

        hits1: tuple[str, float] = "3 | 0 | 0", 200
        hits2: tuple[str, float] = "1 | 0 | 2", 90.5
        hits3: tuple[str, float] = "2 | 1 | 0", 120.4

        # insert the 3 hits
        self.hits_to_kill_grouped.insert(*hits1)
        self.hits_to_kill_grouped.insert(*hits2)
        self.hits_to_kill_grouped.insert(*hits3)

        # make a HitsToKill_Sorter
        hits_to_kill_sorter: HitsToKillSorter = HitsToKillSorter()
        hits_to_kill_sorter.insert(*hits1)
        hits_to_kill_sorter.insert(*hits2)
        hits_to_kill_sorter.insert(*hits3)

        # check if both lists are the same
        self.assertEqual(self.hits_to_kill_grouped.hit_groups[3].sorted_HitsToKill,
                         hits_to_kill_sorter.sorted_HitsToKill,
                         msg="Did not make the same list.")

        # check other hits are not contained
        self.assertNotIn(4, self.hits_to_kill_grouped.hit_groups,
                         msg="Found a 4 hits list even though there shouldn't be one")
