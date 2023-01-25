from . import DamageInfo

class GrenadeDamageInfo(DamageInfo.DamageInfo):
    """Class representing damage information of a grenade in Phantom Forces.
    This is a concrete subclass of abstract class DamageInfo."""

    def __init__(self, d1: float, d2: float, r1: float, r2: float) -> None:
        super().__init__(d1, d2, r1, r2)

    #Override abstract method
    def calculate_killing_ranges(self) -> None:
        # Will killing_radius function to calculate killing radius.
        pass