from typing import TypeAlias, Final
from .. import DamageFunction
from ...damage_info import GunDamageInfo
from ...dataTypes import Hit, HitsToKill

DmgFunc: TypeAlias = 'DamageFunction.DamageOverRangeFunction'

GunDmgInfo: TypeAlias = 'GunDamageInfo.GunDamageInfo'
DmgInfoSub: TypeAlias = GunDmgInfo    # use | for all subclasses, need to add grenade damage info

class DamageFunctionCalculator:
    """Class that handles all base calculations related to damage functions."""
    
    def __init__(self, damage_info: DmgInfoSub, max_hp: int) -> None:
        self.__MAX_HP: Final[int] = max_hp
        self.d1: float = damage_info.max_damage # base damage at min range
        self.d2: float = damage_info.min_damage # base damage at max range
        # Damages named as d1 and d2 as names like max and min damage get confusing for reverse damage drop
        # even though the calculation is the exact same
        self.min_range: float = damage_info.min_range
        self.max_range: float = damage_info.max_range
        self.__damage_drop: float = damage_info.damage_drop
        # Info below is dependant if gun_damage_info or not
        if isinstance(damage_info, GunDmgInfo):
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
            
        
    def calculate_max_range_hits_kill(self, hits_to_kill: HitsToKill) -> float:
        """Calculates the max range the hits to kill provided can kill up to.
        Ignores any previous range that less hits can kill up to.
        For reverse damage drop, nothing special occurs. 
        Any less ranges that more hits to kill are required are ignored.
        Range provided assumes a single linear equation with damage_drop as the slope.
        Meaning any ranges returned that are outside the damage ranges is possible and 
        should be appropriately handled outside this function."""
        # Formula used to calculate range will be discussed in comments at the end, after the return statment

        y_int: float = self.__d1 - (self.__damage_drop*self.__min_range)
        h: float = (hits_to_kill[0]*self.__head_multi) + (hits_to_kill[1]*self.__torso_multi) + hits_to_kill[2]
        range: float = ( (self.__MAX_HP/h) - y_int )/self.__damage_drop
        return range

        # Formula discussed:
        # Function for damage at range r is:
        # D(r) = n_headshots*head_multi*f(r) + n_torsoshots*torso_multi*f(r) + n_limbshots*f(r)
        # n is number of shots to that part of the body
        # f(r) is base damage at range r, assuming damage is always dropping (ignoring how damage is constant before and after min and max range)
        # f(r) = damage_drop*r + y_int, the linear equation, y_int = d1 - damage_drop*min_range
        # To find range at which hits to kills can kill up to, set D(r) to MAX_HP and isolate for r
        # MAX_HP = f(r)[n_headshots*head_multi + n_torsoshots*torso_multi + n_limbshots]
        # Let [n_headshots*head_multi + n_torsoshots*torso_multi + n_limbshots] = h
        # Then we get MAX_HP = f(r)h
        # MAX_HP/h = f(r)
        # Expand f(r) to isolate for r
        # MAX_HP/h = damage_drop*r + y_int
        # MAX_HP/h - y_int = damage_drop*r
        # (MAX_HP/h - y_int )/damage_drop = r
    
    # getters and setters

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
    # Should not be able to set damage_drop
    
    @property
    def MAX_HP(self) -> float:
        return self.__MAX_HP
    # Should not be able to set MAX_HP