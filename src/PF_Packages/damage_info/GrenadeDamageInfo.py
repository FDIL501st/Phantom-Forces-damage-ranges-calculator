from . import DamageInfo
from ..damage_calculator import GrenadeDamageCalculator
from ..dataTypes import HitsToKill


class GrenadeDamageInfo(DamageInfo.DamageInfo):
    """Class representing damage information of a grenade in Phantom Forces.
    This is a concrete subclass of abstract class DamageInfo."""

    def __init__(self, d1: float, d2: float, r1: float, r2: float) -> None:
        super().__init__(d1, d2, r1, r2)
        self._calculator = GrenadeDamageCalculator.GrenadeDamageCalculator(self)

    # Override abstract method
    def calculate_killing_ranges(self) -> HitsToKill:
        return self._calculator.calculate_all_hits_to_kill()

    def __str__(self) -> str:
        stats: str = super().__str__()
        # Just the same as DamageInfo as no extra damage info in grenades
        return stats
