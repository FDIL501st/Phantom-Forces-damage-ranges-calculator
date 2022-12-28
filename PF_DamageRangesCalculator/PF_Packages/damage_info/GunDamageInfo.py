from typing import TypeAlias
#from typing_extensions import Self
from . import DamageInfo
from ..damage_calculator import GunDamageCalculator 


# Some odd reason gets error if try to use alias for base class name 
GunDmgCalc: TypeAlias = 'GunDamageCalculator.GunDamageCalculator'


class GunDamageInfo(DamageInfo.DamageInfo):
    """Class representing the damage information of a gun in Phantom Forces.
    This is a subclass of the abstract DamageInfo class."""

    def __init__(self, d1: float, d2: float, r1: float, r2: float, torsoMulti: float, headMulti: float) -> None:
        # first check for reverse damage drop
        self.reverse_damage_drop: bool = False
        if d1 < d2:
            # Case where gun has reverse damage drop
            self.reverse_damage_drop = True
            # This information is needed for labelling and figuring out the hits to kill combiantions

        super().__init__(d1, d2, r1, r2)
        self.torso_multi: float = torsoMulti
        self.head_multi: float = headMulti


    # Overriding abstract method
    def calculate_killing_ranges(self) -> None:
        # Only try to use the calculator if the calculator is set to some object and is not None
        # This check is to avoid any errors of using None to call methods
        if self._calculator is not None:
            self._calculator.calculate_all_hits_to_kill()
        