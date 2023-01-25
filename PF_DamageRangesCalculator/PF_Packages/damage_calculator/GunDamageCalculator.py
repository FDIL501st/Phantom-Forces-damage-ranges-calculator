from typing import TypeAlias
from . import DamageCalculator
from ..damage_info import GunDamageInfo
from ..damage_function import GunDamageFunction

GunDmgInfo: TypeAlias = 'GunDamageInfo.GunDamageInfo'
GunDmgFunc: TypeAlias = 'GunDamageFunction.GunDamageOverRangeFunction'

class GunDamageCalculator(DamageCalculator.DamageCalculator):
    """Calculator for hits to kill of a gun.
    Is subclass to abstract class DamageCalculator."""

    def __init__(self, gun_dmg_info: GunDmgInfo) -> None:
        super().__init__()
        print("Constructor GunDamageCalculator object.")
        self.gun_damage_info: GunDmgInfo = gun_dmg_info
        self.gun_damage_function: GunDmgFunc = GunDamageFunction.GunDamageOverRangeFunction(gun_dmg_info)
    
    def graph_hits_to_kill(self) -> None:
        pass
    
    def calculate_all_hits_to_kill(self) -> None:
        pass

    # Getters and setters
    @property
    def gun_damage_info(self) -> GunDmgInfo:
        return self.__gun_dmg_info

    @gun_damage_info.setter
    def gun_damage_info(self, newGunDmgInfo: GunDmgInfo) -> None:
        self.__gun_dmg_info: GunDmgInfo = newGunDmgInfo

    @property
    def gun_damage_function(self) -> GunDmgFunc:
        return self.__gun_dmg_func
    
    @gun_damage_function.setter
    def gun_damage_function(self, newGunDmgFunc: GunDmgFunc) -> None:
        self.__gun_dmg_func: GunDmgFunc = newGunDmgFunc

    # TODO - isinstance checks for setters?