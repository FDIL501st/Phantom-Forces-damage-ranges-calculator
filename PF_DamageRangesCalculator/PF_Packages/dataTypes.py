# Module with datatypes used by packages and some aliases
import enum
from typing import TypeAlias, Tuple


# Special enum for a single hit
class Hit(enum.Enum):
    HEAD = "head"
    TORSO = "torso"
    Base = "base"


# General type for all number of hits
Hits: TypeAlias = Tuple[int, int, int]
# Tuple formatted as such: (# of headshots, # of torso shots, # of limb/base shots)
# Grenade damage counts as base damage in Hit, and for Hits would be (0, 0, 1)

HitsToKill: TypeAlias = dict[str, float]
# How hits to kill are stored, with the description of number of shots, and range it can kill up to
