from typing import TypeAlias, Any
from .. import DamageFunction
from ...dataTypes import Hit, HitsToKill

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
        pass

    def calculate_max_range_hits_kill(hits_to_kill: HitsToKill) -> float:
        """Calculates the max range the hits to kill provided can kill up to.
        Ignores any previous range that less hits can kill up to.
        For reverse damage drop, nothing special occurs. 
        Any less ranges that more hits to kill are required are ignored."""
        pass

    # Need a function for figuring if range is before min damage range, between damage ranges, or above max damage range
    # And should return some type of code (aka an int) that represents these three states, or returns an enum
    
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



