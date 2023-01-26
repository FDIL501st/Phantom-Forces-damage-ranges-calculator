from abc import ABC, abstractmethod


class DamageCalculator(ABC):
    """Parent class for DamageCalculator classes. 
    Is abstract, so not meant to be initialized."""

    def __init__(self) -> None:
        super().__init__()
        print("Constructor DamageCalculator abstract class.")
        self.hits_to_kill: dict[str, float] = dict()    # Make a new empty dict to store hits to kill in
    
    @abstractmethod
    def graph_hits_to_kill(self) -> None:
        pass

    # Setter and getter for hits_to_kill
    @property
    def hits_to_kill(self) -> dict[str, float]:
        return self._hits_to_kill
    
    @hits_to_kill.setter
    def hits_to_kill(self, new_hits_to_kill) -> None:
        self._hits_to_kill = new_hits_to_kill
