from ..dataTypes import Hits


class HitsToKillParser:
    """Class to help parse hits to kill data between numbers and strings.
    Help with moving through data through calculation, then convert to string for dict and labels on graph."""

    @staticmethod
    def convert_tuple_to_str(hits: Hits, torso_multi_is_one: bool = False) -> str:
        """Converts hits in Tuple[int, int, int] to string.
        Helpful for adding hits to HitsToKill type which takes in string instead of Tuple."""
        # Read the tuple
        n_head: int = hits[0]
        n_torso: int = hits[1]
        n_limb: int = hits[2]

        # Will use CSV format
        hits_str: str = "{0:d}|{1:d}|{2:d}".format(n_head, n_torso, n_limb)
        return hits_str

    @staticmethod
    def convert_str_to_tuple(hits: str) -> Hits:
        """Converts hits in string to Tuple[int, int, int]."""
        # Need to make sure of checking for "torso/limb"
