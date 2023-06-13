from __future__ import annotations
from typing import TypeAlias, List, Tuple

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
        self.__sorted_HitsToKill: List[element] = []

        if hits_to_kill is not None:
            # Loop through for insertion into list as there are hits to kill provided
            for hit, kill_range in hits_to_kill.items():
                # have to insert the (key, value) pair into the list
                self.insert(hit, kill_range)

    @property
    def sorted_HitsToKill(self) -> List[element]:
        return self.__sorted_HitsToKill

    def insert(self, hits: str, kill_range: float) -> None:
        """
        Takes in a hits to kill, (key, value) pair and inserts into
        sorted_HitsToKill as a tuple.

        Insertion index is the position such that list keeps ascending order by range.
        If there is a duplicate range already existing, place to the right most position
        (right before the range value).
        """

        # implement a binary search-esque algorithm to find index to insert into
        # when find kill_range, move to right half
        # this ensures we insert duplicates right before next kill_range

        # special case: insert into empty list
        if len(self.__sorted_HitsToKill) == 0:
            # can just add to list
            self.__sorted_HitsToKill.append((hits, kill_range))
            # done insertion, so can stop
            return

        # all other cases, do binary search-esque algorithm to find index to insert into

        # set up loop

        # index of lower end of array
        lo: int = 0

        # index of higher end of array
        hi: int = len(self.__sorted_HitsToKill) - 1

        # keep looping until have 1 element left in array being analyzed
        while lo != hi:
            # index of middle of array
            mid: int = lo + (hi - lo) // 2

            # compare to middle element
            # don't care if kill_range is equal as then we go to right(same thing as greater than)

            if kill_range < self.__sorted_HitsToKill[mid][1]:
                # have to insert to left-side of array
                # move hi to mid, lo kept the same
                hi = mid

            else:
                # have to insert to right-right of array
                # move lo to 1 more than mid, hi kept the same
                lo = mid + 1

        # leaving loop means there is only 1 element left to analyze
        # similar deal with which side to place as with loop, except this time actually insert

        # doesn't matter if you use lo or hi, as at this point they should be equal
        if kill_range < self.__sorted_HitsToKill[lo][1]:
            # move everything at lo and above to the right,
            # everything at lo and above is greater than
            self.__sorted_HitsToKill.insert(lo, (hits, kill_range))
        else:
            # place it right after lo, as lo and below are less than or equal to
            self.__sorted_HitsToKill.insert(lo + 1, (hits, kill_range))

    def __iter__(self) -> HitsToKillSorter:
        # start index at 0 for iteration
        self.index: int = 0
        # return the self as the iterator object
        return self

    def __next__(self) -> element:
        try:
            # try to use the index to access an element
            elem: element = self.__sorted_HitsToKill[self.index]
        except IndexError:
            # stop iteration if left the list
            raise StopIteration

        # update the index by 1 to move to next element
        self.index += 1
        # return element we tried to access above
        return elem
