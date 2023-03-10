from typing import TypeAlias, Final
from abc import ABC
from .function_calculator import FunctionCalculator

DmgFuncCalc: TypeAlias = 'FunctionCalculator.DamageFunctionCalculator'


class DamageOverRangeFunction(ABC):
    """Class representing all functions for damage vs range."""

    def __init__(self) -> None:
        self.MAX_HP: Final[int] = 100
        self.function_calculator: DmgFuncCalc | None = None  # to be set later by setter

    # Setter and getters (none for MAX_HP as should be constant)

    @property
    def function_calculator(self) -> DmgFuncCalc:
        return self._function_calculator

    @function_calculator.setter
    def function_calculator(self, new_func_calc: DmgFuncCalc) -> None:
        # Before setting, make sure the argument passed is actually a DmgFuncCalc object
        if isinstance(new_func_calc, FunctionCalculator.DamageFunctionCalculator):
            self._function_calculator = new_func_calc
