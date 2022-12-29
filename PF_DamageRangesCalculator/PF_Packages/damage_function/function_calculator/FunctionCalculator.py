from typing import TypeAlias
from .. import DamageFunction
from ...damage_info import GunDamageInfo, DamageInfo
from ...dataTypes import Hit, HitsToKill

DmgFunc: TypeAlias = 'DamageFunction.DamageOverRangeFunction'
DmgFuncSub: TypeAlias = DmgFunc # use | operator for all subclasses

GunDmgInfo: TypeAlias = 'GunDamageInfo.GunDamageInfo'
DmgInfo: TypeAlias = 'DamageInfo.DamageInfo'
DmgInfoSub: TypeAlias = GunDmgInfo|DmgInfo    # use | for all subclasses

class DamageFunctionCalculator:
    """Class that handles all base calculations related to damage functions."""
    
    def __init__(self, dmg_func: DmgFuncSub) -> None:
        # Before assigning to damage_function, need to make sure actually is of proper type
        # Proper type is any subclass of DmgFunc
        # Luckily, the setter will do this for us
        self.damage_function: DmgFuncSub = dmg_func

        # Call getters for all damage info here so as to call them only once
        # SO no need to call them each time need to do a calculation
        # As will be using these same values more than once
        # TODO - proper calls to getters
        # Might be good idea to first get the damage_info class to no need to repeat that call
        damage_info: DmgInfoSub = None
        self.d1: float = damage_info.max_damage # base damage at min range
        self.d2: float = damage_info.min_damage # base damage at max range
        # Damages named as d1 and d2 as names like max and min damage get confusing for reverse damage drop
        # even though the calculation is the exact same
        self.min_range: float = damage_info.min_range
        self.max_range: float = damage_info.max_range
        self.damage_drop: float = 0
        # Info below is dependant if gun_damage_info or not
        if isinstance(damage_info, DmgInfo):
            self.torso_multi: float = 1
            self.head_multi: float = 1.4
        else:
            # Default values if not dealing with a gun, same as base damage then
            self.torso_multi = 1
            self.head_multi = 1
        
    
    def calculate_damage_one_hit(self, hit_type: str|Hit, range: float) -> float:
        """Calculates the damage of 1 shot at a given range."""
        # First convert hit_type to a string
        if type(hit_type) is Hit:
            hit_type = hit_type.value
        
        multiplier: float = 1
        # Figures out the multi to use
        if hit_type == Hit.TORSO.value:
            multiplier = self.__torso_multi
        # Case when headshot
        elif hit_type == Hit.HEAD.value:
            multiplier = self.__head_multi
        # Other cases are base damage or improrper str, both cases use default multi of 1
        # So doing nothing

        # Now need if-else statement for range
        # Case where range before min_range, so use min_damage
        if range < self.min_range:
            # Calculation is simple, as it does multi*d1
            return multiplier*self.__d1

        # Case ranger after max_Range, so use max_damage
        elif range > self.max_range:
            # Calculation is simple, does multi*d2
            return multiplier*self.__d2

        # Case between the min and max ranges, so must use damage_drop and calculate the damage
        else:
            # Need to calculate damage using the drop
            # Luckily it is a linear equation to solve
            # Linear equation for base damage is f(r) = m*r - m*r1 + d1
            # m is the slope/damage_drop, r is the range, r1 is min_range, d1 is d1

            # the multi done at the end as that linear equation caluclates base damage

            function_result: float = self.__damage_drop*range
            function_result -= self.__damage_drop*self.__min_range
            function_result += self.__d1
            # function_result is done, now mulitply the multi
            return multiplier*function_result
            
        
    def calculate_max_range_hits_kill(hits_to_kill: HitsToKill) -> float:
        """Calculates the max range the hits to kill provided can kill up to.
        Ignores any previous range that less hits can kill up to.
        For reverse damage drop, nothing special occurs. 
        Any less ranges that more hits to kill are required are ignored."""
        
        pass

    # getter and setter
    @property
    def damage_function(self) -> DmgFuncSub:
        return self._damage_function

    @damage_function.getter
    def damage_function(self, dmg_func: DmgFuncSub) -> None:
        # Before assigning, need to check if of correct type
        # Any subclass of DmgFunc
        if isinstance(dmg_func, DmgFunc):
            self._damage_function = dmg_func

        else:
            # All other cases, set to None
            self._damage_function = None

    @property
    def torso_multi(self) -> float:
        return self.__torso_multi

    @torso_multi.setter
    def torso_multi(self, torsoMulti: float) -> None:
        # Only set torso multi if greater than 0
        if torsoMulti > 0:
            self.__torso_multi: float = torsoMulti
        else:
            # Set to default multi of 1
            self.__torso_multi: float = 1

    @property
    def head_multi(self) -> float:
        return self.__head_multi

    @head_multi.setter
    def head_multi(self, headMulti: float) -> None:
        # Only set head multi if greater than 0
        if headMulti > 0:
            self.__head_multi: float = headMulti
        else:
            # Set to default multi of 1
            self.__head_multi: float = 1

    @property
    def d1(self) -> float:
        return self.__d1

    @d1.setter
    def d1(self, damage: float) -> None:
        # Only set damage if not negative
        if not damage < 0:
            self.__d1: float = damage
        else:
            # Set to default damage of 1
            self.__d1: float = 1

    @property
    def d2(self) -> float:
        return self.__d2

    @d1.setter
    def d2(self, damage: float) -> None:
        # Only set damage if not negative
        if not damage < 0:
            self.__d2: float = damage
        else:
            # Set to default damage of 1
            self.__d2: float = 1

    @property
    def max_range(self) -> float:
        return self.__max_range

    @max_range.setter
    def max_range(self, r1: float) -> None:
        # range must not be negative
        if not r1 < 0:
            self.__max_range: float = r1
        # Do nothing if not given proper value
        
    @property
    def min_range(self) -> float:
        return self.__min_range

    @min_range.setter
    def min_range(self, r2: float) -> None:
        # range must not be negative
        if not r2 < 0:
            self.__min_range: float = r2
        # Do nothing if not given proper value

    @property
    def damage_drop(self) -> float:
        return self.__damage_drop

    @damage_drop.setter
    def damage_drop(self, drop: float) -> None:
        self.__damage_drop: float = drop
    