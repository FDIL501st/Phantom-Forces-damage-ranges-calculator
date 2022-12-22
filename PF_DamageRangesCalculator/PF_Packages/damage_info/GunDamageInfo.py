from .DamageInfo import DamageInfo as Dmg_Info
from ..damage_calculator.GunDamageCalculator import gun_dmg_calc


class GunDamageInfo(Dmg_Info):
    """Class representing the damage information of a gun in Phantom Forces.
    This is a subclass of the abstract DamageInfo class."""

    def __init__(self, d1: float, d2: float, r1: float, r2: float, torsoMulti: float, headMulti: float) -> None:
        # first check for reverse damage drop
        self.reverse_damage_drop = False
        if d1 < d2:
            # Case where gun has reverse damage drop
            self.reverse_damage_drop = True
            # Need to switch values of d1 and d2 for correct storing of variables
            # Damage calculations will consider for reverse_damage_drop
            temp: float = d1
            d1 = d2
            d2 = temp

        super().__init__(d1, d2, r1, r2)
        self.torso_multi: float = torsoMulti
        self.head_multi: float = headMulti

        # Set calculator to a GunDamageCalculator object
        self.calculator = gun_dmg_calc

    