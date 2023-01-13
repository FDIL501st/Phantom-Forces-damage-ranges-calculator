from typing import TypeAlias
from math import isinf
from . import DamageFunction
from ..damage_info import GunDamageInfo
from .function_calculator import FunctionCalculator
from ..dataTypes import HitsToKill, Hits
from ..parser.HitsToKillParser import HitsToKillParser

GunDmgInf: TypeAlias = 'GunDamageInfo.GunDamageInfo'

class GunDamageOverRangeFunction(DamageFunction.DamageOverRangeFunction):
    """Represents damage over range function for guns."""
    def __init__(self, gun_dmg_info: GunDmgInf) -> None:
        super().__init__()
        
        self.gun_damage_info = gun_dmg_info
        self.function_calculator = FunctionCalculator.DamageFunctionCalculator(gun_dmg_info, 100)
    
    def calculate_all_combinations_hits_to_kill(self) -> HitsToKill:
        """Calculates all combinations of hits that can kill.""" 
        hits_to_kill: HitsToKill = {}
        if self.__gun_damage_info.torso_multi == 1.0:
            # Torso multi is 1, so can ignore torso hits
            hits_to_kill.update(self.__calculate_head_limb_hits)
            hits_to_kill.update(self.__calculate_only_limb_hits, True)
        else:
            # Include torso hits
            hits_to_kill.update(self.__calculate_head_torso_limb_hits)
            hits_to_kill.update(self.__calculate_torso_limb_hits)
            hits_to_kill.update(self.__calculate_only_limb_hits)

        return hits_to_kill

    def __calculate_only_limb_hits(self, torso_multi_one: bool = False) -> HitsToKill:
        """Calculates combinations of only limb hits that can kill."""
        hits_to_kill: HitsToKill = {}   # stores the hits to kill
        n_limb: int = 1 # Keep track of number of limb hits

        while True:
            hits: Hits = (0, 0, n_limb) # a potential hits to kil
            range: float = self._function_calculator.calculate_max_range_hits_kill(hits)
            # Check if can kill
            if range != -1:
                # Can kill, so add to hits_to_kill
                hits_str: str = HitsToKillParser.convert_tuple_to_str(hits=hits, torso_multi_is_one=torso_multi_one)
                hits_to_kill[hits_str] = range
            
            # Check if can kill all ranges
            if isinf(range):
                # Leave loop, this is our leaving condition
                # Also because after leaving loop, all that needs to be done is return hits_to_kill,
                #   will just replace the break with the return statement to end the loop(as end the function) 
                #   and return at the same time
                return hits_to_kill

            # Add 1 limb hit, our udpate condition
            n_limb += 1


    def __calculate_torso_limb_hits(self) -> HitsToKill:
        """Calculates combinations of only torso and limb hits that can kill."""
        hits_to_kill: HitsToKill = {}   # stores hits to kill
        n_torso: int = 1     # stores number of torso shots
        n_limb: int = 0      # stores number of limb shots

        while True:
            hits: Hits = (0, n_torso, n_limb)
            range: float = self._function_calculator.calculate_max_range_hits_kill(hits)

            #Check if can kill
            if range != -1:
                # can kill, so can add to hits_to_kill
                hits_str: str = HitsToKillParser.convert_tuple_to_str(hits)
                # This function only used when torso multi is not 1, so can assume that
                hits_to_kill[hits_str] = range

            # Check if can kill all range
            if isinf(range):
                # Check if have only torso hits (meaning n_limb == 0)
                if n_limb == 0:
                    # reached limit for hits,
                    # adding more is redundant as already can kill all range with current number of torso hits
                    # so can return hits_to_kill
                    return hits_to_kill
                
                # We need to move to next torso shot and reset limb shot, then continue loop
                n_torso += 1
                n_limb = 0
                continue
            
            # Need to add 1 limb shot for next iteration of loop
            n_limb += 1

    def __calculate_head_limb_hits(self) -> HitsToKill:
        """Calculates combinations of only head and limb this that can kill."""
        hits_to_kill: HitsToKill = {}   # stores hits to kill
        n_head: int = 1  # stores number of headshots
        n_limb: int = 0  # stores number of limb shots

        while True:
            hits: Hits = (n_head, 0, n_limb)    # potential hits to kill
            range: float = self._function_calculator.calculate_max_range_hits_kill(hits) 
            # Check if can kill
            if range != -1:
                # can kill, so add to hits_to kill
                hits_str: str = HitsToKillParser.convert_tuple_to_str(hits=hits, torso_multi_is_one=True)   
                #This function only called when torso multi is 1
                hits_to_kill[hits_str] = range

            # Check if can kill all ranges
            if isinf(range):
                #Check if have only headshots (meaning n_limb == 0)
                if n_limb == 0:
                    # This means we reached our limit with hits, adding more is pointless and less hits will already kill all ranges
                    # return hits_to_kill
                    return hits_to_kill

                # We need to move up 1 headshot and reset limb shots and continue loop
                n_head += 1
                n_limb = 0
                continue
            # Reaching here means need to add 1 limb shot for next iteration of loop
            n_limb += 1

    def __calculate_head_torso_limb_hits(self) -> HitsToKill:
        """Calculates combinations of hits with atleast 1 headshot that can kill."""
        hits_to_kill: HitsToKill = {}       # stores hits to kill
        n_head: int = 1     # stores number of headshots
        n_torso: int = 0    # stores number of torso shots
        n_limb: int = 0     # stores number of limb shots

        while True:
            hits: Hits = (n_head, n_torso, n_limb)      # potential hits to kill
            range: float = self._function_calculator.calculate_max_range_hits_kill(hits)

            #Check if can kill
            if range != -1:
                # can kill, so can add to hits_to kill
                hits_str: str = HitsToKillParser.convert_tuple_to_str(hits)
                # This function only used when torso multi is not 1, so can assume that
                hits_to_kill[hits_str] = range
            
            # Check if can kill all ranges
            if isinf(range):
                pass
            
            #Before next iteration of loop, need to add 1 limb shot
            n_limb += 1
    # Getter and setters
    @property
    def gun_damage_info(self) -> GunDmgInf:
        return self.__gun_damage_info

    @gun_damage_info.setter
    def gun_damage_info(self, gun_dmg_inf: GunDmgInf) -> None:
        # Before setting, make sure to only set GunDamageInfo objects
        if isinstance(gun_dmg_inf, GunDamageInfo.GunDamageInfo):
            self.__gun_damage_info: GunDmgInf = gun_dmg_inf
        else:
            # If set did not occur, check if __gun_damage_info is an attribute(has been set before)
            # If not, then should set to None to make it exist for later getter calls or usage and not get Attribute Error
            try:
                a = self.__gun_damage_info
            except AttributeError:
                # __gun_damage_info has not been set yet, so need to set it to None
                # This won't run if __gun_damage_info already exists
                # Then just won't set to new value
                self.__gun_damage_info = None

