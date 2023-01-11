from typing import TypeAlias
from . import DamageFunction
from ..damage_info import GunDamageInfo
from .function_calculator import FunctionCalculator
from ..dataTypes import HitsToKill

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
        else:
            # Include torso hits
            hits_to_kill.update(self.__calculate_head_torso_limb_hits)
            hits_to_kill.update(self.__calculate_torso_limb_hits)

        hits_to_kill.update(self.__calculate_only_limb_hits)
        return hits_to_kill

    def __calculate_only_limb_hits(self) -> HitsToKill:
        """Calculates combinations of only limb hits that can kill."""

    def __calculate_torso_limb_hits(self) -> HitsToKill:
        """Calculates combinations of only torso and limb hits that can kill."""
    
    def __calculate_head_limb_hits(self) -> HitsToKill:
        """Calculates combinations of only head and limb this that can kill."""
    
    def __calculate_head_torso_limb_hits(self) -> HitsToKill:
        """Calculates combinations of hits with atleast 1 headshot that can kill."""

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

