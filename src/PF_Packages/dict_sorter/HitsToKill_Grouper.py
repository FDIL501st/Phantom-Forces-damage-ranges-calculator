from __future__ import annotations
from typing import TypeAlias, Dict

from .HitsToKill_Sorter import HitsToKillSorter


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


def num_hits(hits_to_kill: str) -> int:
    """Returns the number of hits a HitsToKill has."""
