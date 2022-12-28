# Module with datatypes used by packages and some aliases
import enum
from typing import TypeAlias, Tuple

class Hit(enum.Enum):
    HEAD = "head"
    TORSO = "torso"
    Base = "base"

class Range(enum.Enum):
    BEFORE_MIN_RANGE = -1
    DAMAGE_DROP = 0
    AFTER_MAX_RANGE = 1


HitsToKill: TypeAlias = Tuple[int, int, int]
# Tuple formatted as such: (# of headshots, # of torso shots, # of limb/base shots)
# Grenade damage counts as base damage in Hit, and for HitsToKill would be (0, 0, 1)