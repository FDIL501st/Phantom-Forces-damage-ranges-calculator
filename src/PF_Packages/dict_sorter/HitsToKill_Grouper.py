from __future__ import annotations
from typing import TypeAlias, Dict

from .HitsToKill_Sorter import HitsToKillSorter
from ..dataTypes import Hits


class HitsToKill_Grouper:
    """
    Groups HitsToKill by number of hits.
    Each number of hits has a HitsToKill_Sorter.
    Grouping done using a dict,
    where the key is number of hits and
    value is the HitsToKill_Sorter with all this hits to kill with that number of hits.
    """
    def __int__(self) -> None:
        self.hit_groups: Dict[int, HitsToKillSorter] = {}


def num_hits(hits_to_kill: Hits) -> int:
    """
    Sums up the number of hits in hits to kill provided.

    :param hits_to_kill: Hits to kill as 3 numbers
    :type hits_to_kill: tuple[int, int, int]
    :return: The total number of hits in hits to kill
    :rtype: int
    """
    # expect hits_to_kill to be a tuple of 3 ints
    # we just sum up those 3 numbers
    return sum(hits_to_kill)
