from typing import TypeAlias, Dict
from tkinter import ttk
from .button import Button
from .result_button import ResultButton
from .gun_result_button import GunResultButton
from .grenade_result_button import GrenadeResultButton
from ..main_window import GUI

Frame: TypeAlias = ttk.Frame


class ButtonFrame(Frame):
    """Frame storing the buttons of the GUI."""
    def __init__(self, master: GUI, *buttons: ResultButton) -> None:
        super().__init__(master=master)
        self.top_master: GUI = master

        self.buttons: Dict[int, ResultButton] = {}
        # Initialize values of buttons
        for button in buttons:
            num: int = self.__find_button_type(button)
            self.buttons[num] = button

    @staticmethod
    def __find_button_type(button: ResultButton) -> int:
        """Finds the button type according to enum Button, and return that enum type."""
        # This code will be hard coded to search for all types of ResultButton classes,
        # and enum literals Button has

        if isinstance(button, GunResultButton):
            return Button.GUN.value
        elif isinstance(button, GrenadeResultButton):
            return Button.GRENADE.value
        else:
            raise TypeError("Did not pass a ResultButton object.")

    def display_button(self, button_type: int | Button) -> None:
        """Displays the button matching the button_type.
        """

        # First need to convert button_type to an integer, if it is an Enum
        if isinstance(button_type, Button):
            button_num: int = button_type.value
        else:
            button_num = button_type

        # Now having int, we can find it in the dictionary
        button_display: ResultButton = self.buttons[button_num]
        