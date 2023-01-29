from typing import TypeAlias
from .result_button import ResultButton
from . import button_frame

ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'


class GrenadeResultButton(ResultButton):
    """Class for the button when pressed
    should calculate killing radius of a grenade
    and display the results.
    """

    def __init__(self, master: ButtonFrame) -> None:
        super().__init__(master=master)
        grenade_label: str = "Calculate killing radius"
        self.label.set(grenade_label)
