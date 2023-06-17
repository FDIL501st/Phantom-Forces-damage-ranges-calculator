from __future__ import annotations

from typing import TypeAlias, Tuple
from sortedcontainers import SortedList

from ..dataTypes import HitsToKill

# an element of the sorted list
element: TypeAlias = Tuple[str, float]


class HitsToKillSorter:
    """
    Sorts HitsToKill by descending value of range.
    The (key, value) pairs are stored in a list.
    """

    # Can use sortedList instead and pass key to sort by range
    def __init__(self, hits_to_kill: HitsToKill = None) -> None:
        self.__sorted_HitsToKill: SortedList[element] = SortedList(key=lambda x: x[1])
        # make SortedList with the ranges being used to sort the tuples
        if hits_to_kill is not None:
            # insert initial hits to kills if they are given
            self.__sorted_HitsToKill.update(hits_to_kill.items())

    @property
    def sorted_HitsToKill(self) -> SortedList[element]:
        return self.__sorted_HitsToKill

    def insert(self, hits: str, kill_range: float) -> None:
        """
        Takes in a hits to kill, (key, value) pair and inserts into
        sorted_HitsToKill as a tuple.
        """
        # just call add of SortedList
        self.__sorted_HitsToKill.add(value=(hits, kill_range))

    def __iter__(self):
        # just return iter of SortedList
        return iter(self.__sorted_HitsToKill)
