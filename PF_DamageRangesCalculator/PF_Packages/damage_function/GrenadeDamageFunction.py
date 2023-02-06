from typing import TypeAlias
from . import DamageFunction
from .function_calculator import FunctionCalculator
from ..damage_info import GrenadeDamageInfo
from ..dataTypes import HitsToKill, Hit

GrenDmgInfo: TypeAlias = 'GrenadeDamageInfo.GrenadeDamageInfo'


class GrenadeDamageOverRangeFunction(DamageFunction.DamageOverRangeFunction):
    """Represent damage over range functions for grenades."""

    def __init__(self, gren_dmg_info: GrenDmgInfo) -> None:
        super().__init__()
        self.__grenade_damage_info = gren_dmg_info
        self.function_calculator = FunctionCalculator.DamageFunctionCalculator(gren_dmg_info, 100)

    def calculate_killing_radius(self) -> HitsToKill:
        """Calculates the killing radius of a grenade."""
        radius: float = self.function_calculator.calculate_max_range_hits_kill([0, 0, 1])
        return {"Grenade kill radius": radius}
