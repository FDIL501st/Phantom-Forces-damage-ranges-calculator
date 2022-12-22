from . import DamageCalculator


DmgCalc = DamageCalculator.DamageCalculator

class GunDamageCalculator(DmgCalc):
    """Calculator for hits to kill of a gun.
    Is subclass to abstract class DamageCalculator."""

    def __init__(self) -> None:
        super().__init__()
        print("Constructor GunDamageCalculator object.")
        # TODO - finish constructor

    
    def calculate_all_hits_to_kill(self) -> None:
        pass


# A GunDamageCalculator object to import in other modules if needed
gun_dmg_calc: GunDamageCalculator = GunDamageCalculator()
