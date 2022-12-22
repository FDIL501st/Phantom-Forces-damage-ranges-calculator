from . import DamageCalculator

DmgCalc = DamageCalculator.DamageCalculator

class GrenadeDamageCalculator(DmgCalc):
    """Calculator for grenade kill radius.
    Is subclass to abstract class DamageCalcultor"""
    pass


# A GrenadeDamageCalculator object to reference in other modules
gren_dmg_calc: GrenadeDamageCalculator = GrenadeDamageCalculator()