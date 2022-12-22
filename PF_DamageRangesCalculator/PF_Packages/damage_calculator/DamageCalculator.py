from abc import ABC

class DamageCalculator(ABC):
    """Parent class for DamageCalculator classes. 
    Is abstract, so not meant to be initialized."""

    def __init__(self) -> None:
        super().__init__()
        print("Constructor DamageCalculator abstract class.")
    pass




    


