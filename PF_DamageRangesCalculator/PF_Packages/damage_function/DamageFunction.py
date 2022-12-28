from typing import TypeAlias, Final
from abc import ABC, abstractmethod
from .function_calculator import FunctionCalculator

DmgFuncCalc: TypeAlias = 'FunctionCalculator.DamageFunctionCalculator'

class DamageOverRangeFunction(ABC):
    """Class representing all functions for damage vs range."""
    def __init__(self) -> None:
        self.damage_drop: float = 0    # Set by subclasses
        self.MAX_HP: Final[int] = 100
        self.function_calculator: DmgFuncCalc = None # to be set later by setter

    @abstractmethod
    def calculate_damage_drop(self) -> None:
        """Calculates and set damage_drop.
        Should be called within constructor of concrete subclasses as 
        they have they data needed to calculate it."""
        pass

    # Setter and getters (none for MAX_HP as should be constant)
    @property
    def damage_drop(self) -> float:
        return self._damage_drop
    
    @damage_drop.setter
    def damage_drop(self, damageDrop: float) -> None:
        self._damage_drop = damageDrop

    @property
    def function_calculator(self) -> DmgFuncCalc:
        return self._function_calculator

    @function_calculator.setter
    def function_calculator(self, new_func_calc: DmgFuncCalc) -> None:
        # Before setting, make sure the argument passed is actually a DmgFuncCalc object
        if issubclass(type(new_func_calc), type(DmgFuncCalc)):
            self._function_calculator = new_func_calc




