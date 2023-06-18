from __future__ import annotations

from typing import TypeAlias, Dict
from sortedcontainers import SortedDict

from .HitsToKill_Sorter import HitsToKillSorter
from ..parser.HitsToKillParser import HitsToKillParser
from ..dataTypes import Hits

hit_group: TypeAlias = SortedDict[int, HitsToKillSorter]


class HitsToKill_Grouper:
    """
    Groups HitsToKill by number of hits.
    Each number of hits has a HitsToKill_Sorter.
    Grouping done using a dict,
    where the key is number of hits and
    value is the HitsToKill_Sorter with all this hits to kill with that number of hits.
    """

    def __init__(self) -> None:
        self.__hit_groups: hit_group = SortedDict()
        # Help with ordering by key

    @property
    def hit_groups(self) -> hit_group:
        return self.__hit_groups

    def insert(self, hits: str, kill_range: float) -> None:
        """
        Adds a hit to hit_groups.

        :param hits: hits to add
        :type hits: str
        :param kill_range: range the hits can kill to
        :type kill_range: float
        """

        # get number of hits
        n_hits: int = num_hits(HitsToKillParser.convert_str_to_tuple(hits))
        # before adding, check if n_hits exist
        if n_hits in self.__hit_groups:
            # this means there is a HitsToKillSorter that can be added to
            sorted_hits_to_kill: HitsToKillSorter = self.__hit_groups[n_hits]
            sorted_hits_to_kill.insert(hits, kill_range)
            return

        # n_hit doesn't exist, so need to make a new HitsToKillSorter list
        new_sorted_list: HitsToKillSorter = HitsToKillSorter()
        new_sorted_list.insert(hits, kill_range)

        self.__hit_groups[n_hits] = new_sorted_list

    def insert_all(self, hits_to_kills: Dict[str, float]) -> None:
        """
        A method to bulk insert lots of hits to kills. Just calls insert for each hits to kill.

        :param hits_to_kills: a dict of all hits to kills to insert
        """
        for hits, kill_range in hits_to_kills.items():
            self.insert(hits, kill_range)

    def __iter__(self):
        # just return to call iter of the dict

        # this means I don't need to define __next__ for this class
        # as the iter of the SortedDict has that already defined
        return iter(self.__hit_groups)


def num_hits(hits: Hits) -> int:
    """
    Sums up the number of hits in hits to kill provided.

    :param hits: Hits to kill as 3 numbers
    :type hits: tuple[int, int, int]
    :return: The total number of hits in hits to kill
    :rtype: int
    """
    # expect hits_to_kill to be a tuple of 3 ints
    # we just sum up those 3 numbers
    return sum(hits)
