import re
from typing import Optional

from ..dataTypes import Hits


class HitsToKillParser:
    """Class to help parse hits to kill data between numbers and strings.
    Help with moving through data through calculation, then convert to string for dict and labels on graph."""

    @staticmethod
    def convert_tuple_to_str(hits_tup: Hits) -> str:
        """Converts hits in Tuple[int, int, int] to string.
        Helpful for adding hits to HitsToKill type which takes in string instead of Tuple."""
        # Read the tuple
        n_head: int = hits_tup[0]
        n_torso: int = hits_tup[1]
        n_limb: int = hits_tup[2]

        # Will use CSV format
        hits_str: str = "{0:d} | {1:d} | {2:d}".format(n_head, n_torso, n_limb)
        return hits_str

    @staticmethod
    def convert_str_to_tuple(hits_str: str) -> Hits:
        """Converts hits in string to Tuple[int, int, int].
        Does the reverse of convert_tuple_to_str().

        :param hits_str: hits as a string, expected format is what convert_tuple_to_str() returns.
        :type hits_str: str
        :return: hits as a tuple of 3 ints, (# of headshots, # of torso shots, # of limb shots)
        :rtype: Tuple[int, int, int]
        """

        # use a re to confirm expected format

        # pattern for the format of what hits should be
        # format is what convert_tuple_str() returns

        hits_str_format: re.Pattern = re.compile(
            "(?P<num_head>\d+) \| (?P<num_torso>\d+) \| (?P<num_limb>\d+)"
        )

        result: Optional[re.Match] = re.fullmatch(hits_str_format, hits_str)
        if not result:
            # result is None, meaning failed to match
            # raise ValueError as incorrect argument passed in
            raise ValueError("hits provided is not expected format")

        # having confirmed format of hits, can read the 3 ints from it
        hits_tuple: Hits = (
            int(result.group('num_head')),
            int(result.group('num_torso')),
            int(result.group('num_limb'))
        )
        return hits_tuple
