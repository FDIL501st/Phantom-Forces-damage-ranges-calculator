from typing import TypeAlias

from . import DamageCalculator
from ..damage_info import GrenadeDamageInfo
from ..damage_function import GrenadeDamageFunction

GrenDmgInfo: TypeAlias = 'GrenadeDamageInfo.GrenadeDamageInfo'
GrenDmgFunc: TypeAlias = 'GrenadeDamageFunction.GrenadeDamageOverRangeFunction'


class GrenadeDamageCalculator(DamageCalculator.DamageCalculator):
    """Calculator for grenade kill radius.
    Is subclass to abstract class DamageCalculator"""

    def __init__(self, gren_dmg_info: GrenDmgInfo) -> None:
        super().__init__()
        self.__grenade_damage_function: GrenDmgFunc = GrenadeDamageFunction.GrenadeDamageOverRangeFunction(
            gren_dmg_info)

    def graph_hits_to_kill(self) -> None:
        pass

    def calculate_all_hits_to_kill(self) -> None:
        self._hits_to_kill = self.__grenade_damage_function.calculate_killing_radius()

    @property
    def grenade_damage_function(self) -> GrenDmgFunc:
        return self.__grenade_damage_function

    @grenade_damage_function.setter
    def grenade_damage_function(self, gren_dmg_func: GrenDmgFunc) -> None:
        self.__grenade_damage_function = gren_dmg_func
