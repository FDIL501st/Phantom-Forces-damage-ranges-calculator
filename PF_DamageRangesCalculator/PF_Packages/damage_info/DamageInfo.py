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
        # Can't set negative damage, so do nothing if that occurs
        if d1 > 0:
            self._max_damage = d1
    
    @property
    def min_damage(self) -> float:
        return self._min_damage

    @min_damage.setter
    def min_damage(self, d2: float) -> None:
        # Can't set negative damage, so do nothing if that occurs
        if d2 > 0:
            self._min_damage = d2

    @property
    def max_range(self) -> float:
        return self._max_range

    @max_range.setter
    def max_damage_range(self, r1: float) -> None:
        # Can't set negative range, so do nothing if that occurs
        if r1 > 0:
            self._max_range = r1

    @property
    def min_range(self) -> float:
        return self._min_range

    @min_range.setter
    def min_range(self, r2: float) -> None:
        # Can't set negative range, so do nothing if that occurs
        if r2 > 0:
            self._min_range = r2

