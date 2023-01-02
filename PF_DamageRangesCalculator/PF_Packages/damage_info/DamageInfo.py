from typing import TypeAlias
from abc import ABC, abstractmethod
from ..damage_calculator import DamageCalculator


DmgCalc: TypeAlias = 'DamageCalculator.DamageCalculator'

class DamageInfo(ABC):
    """Parent class for all DamageInfo classes.
    Is an abstract class, so not meant to be initialized."""

    def __init__(self, d1: float, d2: float, r1: float, r2: float) -> None:
        super().__init__()
        self.max_damage: float = d1
        self.min_damage: float = d2
        self.max_range: float = r1
        self.min_range: float = r2
        self.calculator: DmgCalc = None   
        # calculator is to be set later by subclasses to the one they need

        
    @abstractmethod
    def calculate_killing_ranges(self) -> None:
        pass

    def __calculate_damage_drop(self)  -> None:
        """Calculates and set damage_drop."""
        try:
            # Simple slope calculation, change in damage/change in range
            self._damage_drop: float = (self._max_damage - self._min_damage)/(self._min_range - self._max_range)
        except AttributeError:
            # This can occur during constructor as other attributes yet to exist
            # So just catch and do nothing with the exception
            # Later at some point will be able to calculate
            # For now, don't want program to stop
            pass

    # Setter and getters for all instance variables

    @property
    def calculator(self) -> DmgCalc:
        return self._calculator

    @calculator.setter
    def calculator(self, calculator: DmgCalc) -> None:
        # Before setting calculator, must check if calculator passed is a subclass of DamageCalculator
        # Don't want to set objects that aren't actually a DamageCalculator
        if issubclass(type(calculator), type(DmgCalc)):
            self._calculator = calculator

    @property
    def max_damage(self) -> float:
        return self._max_damage

    @max_damage.setter
    def max_damage(self, d1: float) -> None:
        # Damage must be greater than 0
        if d1 > 0:
            self._max_damage: float = d1
            self.__calculate_damage_drop()
        # do not set if not given proper damage to set

    @property
    def min_damage(self) -> float:
        return self._min_damage

    @min_damage.setter
    def min_damage(self, d2: float) -> None:
        # Damage must be greater than 0
        if d2 > 0:
            self._min_damage: float = d2
            self.__calculate_damage_drop()
        # do not set if not given proper damage to set

    @property
    def max_range(self) -> float:
        return self._max_range

    @max_range.setter
    def max_range(self, r1: float) -> None:
        # range must not be negative
        if not r1 < 0:
            self._max_range: float = r1
            self.__calculate_damage_drop()
        # Do nothing if not given proper value
        
    @property
    def min_range(self) -> float:
        return self._min_range

    @min_range.setter
    def min_range(self, r2: float) -> None:
        # range must not be negative
        if not r2 < 0:
            self._min_range: float = r2
            self.__calculate_damage_drop()
        # Do nothing if not given proper value

    @property
    def damage_drop(self) -> float:
        return self._damage_drop
    
    # No setter for damage_drop as it should not be set directly
    