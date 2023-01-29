from typing import TypeAlias
from .result_button import ResultButton
from . import button_frame

ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'


class GunResultButton(ResultButton):
    """Class for the button when pressed should
    calculate hits to kill of a gun and
    display the results.
    """

    def __init__(self, master: ButtonFrame) -> None:
        super().__init__(master=master)
        gun_label: str = "Calculate hits to kill"
        self.label.set(gun_label)
