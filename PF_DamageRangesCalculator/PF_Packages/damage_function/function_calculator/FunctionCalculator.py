from typing import TypeAlias, Any
from .. import DamageFunction
from ...dataTypes import Hit, HitsToKill, Range

DmgFunc: TypeAlias = DamageFunction.DamageOverRangeFunction

class DamageFunctionCalculator:
    """Class that handles all base calculations related to damage functions."""
    
    def __init__(self, dmg_func: Any) -> None:
        # Before assigning to damage_function, need to make sure actually is of proper type
        # Proper type is any subclass of DmgFunc
        # Luckily, the setter will do this for us
        self.damage_function: Any = dmg_func
    
    def calculate_damage_one_hit(self, hit_type: str|Hit, range: float) -> float:
        """Calculates the damage of 1 shot at a given range."""
        # TODO - proper calls to getters
        min_range: float = 0
        max_range: float = 0
        pass

    def calculate_max_range_hits_kill(hits_to_kill: HitsToKill) -> float:
        """Calculates the max range the hits to kill provided can kill up to.
        Ignores any previous range that less hits can kill up to.
        For reverse damage drop, nothing special occurs. 
        Any less ranges that more hits to kill are required are ignored."""
        # TODO - proper calls to getters
        min_range: float = 0
        max_range: float = 0
        # Know will end up calling this function a lot, might save time if get this info during constructor instead here
        # As only really need to call all the getters once as this info stays constant during all the calls to this
        pass

    # Need a function for figuring if range is before min damage range, between damage ranges, or above max damage range
    # And should return some type of code (aka an int) that represents these three states, or returns an enum

    # Might be worthless method as still need to do if-else statements later when need to do calcualtions
    # End up not doing anything to cut down on code but rather increases code
    def calculate_range_type(range: float) -> Range:
        """Figures out the type of range the given range is.
        Types of range are being before min range, damage drop range, or after max range."""
        # first need to get the min and max range so got ranges to compare to
        
        # TODO - proper calls to getters
        min_range: float = 0
        max_range: float = 0

        if range < min_range:
            return Range.BEFORE_MIN_RANGE
        elif range > max_range:
            return Range.AFTER_MAX_RANGE
        # Only other case left is being between min_range and max_range
        else:
            return Range.DAMAGE_DROP

    # getter and setter
    @property
    def damage_function(self) -> Any:
        return self._damage_function

    @damage_function.getter
    def damage_function(self, dmg_func: Any) -> None:
        # Before assigning, need to check if of correct type
        if issubclass(type(dmg_func), type(DmgFunc)):
            self._damage_function = dmg_func

        else:
            # All other cases, set to None
            self._damage_function = None



