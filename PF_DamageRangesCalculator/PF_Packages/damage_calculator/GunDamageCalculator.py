from typing import TypeAlias
from . import DamageCalculator
from ..damage_info import GunDamageInfo


GunDmgInfo: TypeAlias = 'GunDamageInfo.GunDamageInfo'

#Some odd reason, when try to use alias for base parent name, get error about argument being tuple, not str somehow
class GunDamageCalculator(DamageCalculator.DamageCalculator):
    """Calculator for hits to kill of a gun.
    Is subclass to abstract class DamageCalculator."""

    def __init__(self, gun_dmg_info: GunDmgInfo) -> None:
        super().__init__()
        print("Constructor GunDamageCalculator object.")
        self.gun_damage_info: GunDmgInfo = gun_dmg_info
        #self.gun_damage_function: GunDmgFunc = GunDmgFunc()
    
    def graph_hits_to_kill() -> None:
        pass
    
    def calculate_all_hits_to_kill(self) -> None:
        pass

    # Getters and setters
    @property
    def gun_damage_info(self) -> GunDmgInfo:
        return self.__gun_dmg_info

    @gun_damage_info.setter
    def gun_damage_info(self, newGunDmgInfo: GunDmgInfo) -> None:
        self.__gun_dmg_info = newGunDmgInfo

    # Still need setter and getter for gun_damage_function


