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

        # String starters that will be used
        head_msg: str = "{0:d} headshots"
        torso_msg: str = "{0:d} torso shots"
        limb_msg1: str = "{0:d} limb shots"
        limb_msg2: str = "{0:d} torso/limb shots"

        hits_str: str = ""  # What we will build and return

        def parse_headshots(s: str) -> str:
            # Deal with headshots
            if n_head == 0:
                # Don't add head_msg, got no headshots
                pass
            elif n_head == 1:
                s += head_msg[:-1].format(n_head)
                # Remove the s before adding
            else:
                # more than 1 headshot
                s += head_msg.format(n_head)
            return s

        def parse_torsoshots(s: str) -> str:
            # Deal with torso shots
            if n_torso == 0:
                # Don't add torso_msg, got no torso shots
                pass
            elif n_torso == 1:
                s += torso_msg[:-1].format(n_torso)
                # Remove the s before adding
            else:
                # more than 1 torso shot
                s += torso_msg.format(n_torso)
            return s

        def parse_limbshots1(s: str) -> str:
            # Deal with torso shots
            if n_limb == 0:
                # Don't add torso_msg, got no torso shots
                pass
            elif n_limb == 1:
                s += limb_msg1[:-1].format(n_limb)
                # Remove the s before adding
            else:
                # more than 1 torso shot
                s += limb_msg1.format(n_limb)
            return s

        def parse_limbshots2(s: str) -> str:
            # Deal with torso shots
            if n_limb == 0:
                # Don't add torso_msg, got no torso shots
                pass
            elif n_limb == 1:
                s += limb_msg2[:-1].format(n_limb)
                # Remove the s before adding
            else:
                # more than 1 torso shot
                s += limb_msg2.format(n_limb)
            return s

        def add_space(s: str) -> str:
            if len(s) == 0:
                # s is empty
                # Do nothing
                pass
            elif not s[-1].isspace():
                # s doesn't have a space, need to add it
                s += ", "
            return s

        if not torso_multi_is_one:
            # Consider all 3 type of shots
            hits_str = parse_headshots(hits_str)
            hits_str = add_space(hits_str)
            hits_str = parse_torsoshots(hits_str)
            hits_str = add_space(hits_str)
            hits_str = parse_limbshots1(hits_str)
        else:
            # Due to torso multi is 1, we use limb_msg2
            # Also only considering head and limb shots
            hits_str = parse_headshots(hits_str)
            hits_str = add_space(hits_str)
            hits_str = parse_limbshots2(hits_str)
        
        # Before returning, need to remove extra space if added at end
        # This also only works if hits_str is not an empty string, for example (0, 0, 0) or
        #   or for some odd reason have only torso hits when torso multi is 1, as then those hits are ignored
        # Our program shouldn't be doing this, but in case it does, we deal with it to not run into an error
        if len(hits_str) != 0:
            if hits_str[-1].isspace():
                hits_str = hits_str[:-2]
                # Make itself equal to itself without last 2 char, ", "
        return hits_str

    @staticmethod
    def convert_str_to_tuple(hits: str) -> Hits:
        """Converts hits in string to Tuple[int, int, int]."""
        # Need to make sure of checking for "torso/limb"