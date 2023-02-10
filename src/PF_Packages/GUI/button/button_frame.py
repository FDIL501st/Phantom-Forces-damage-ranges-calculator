from typing import TypeAlias, Dict, List
from tkinter import ttk
from .button import Button
from . import result_button, gun_result_button, grenade_result_button
from .. import main_window

Frame: TypeAlias = ttk.Frame
ResultButton: TypeAlias = result_button.ResultButton
GUI: TypeAlias = 'main_window.GUI'


class ButtonFrame(Frame):
    """Frame storing the buttons of the GUI."""
    def __init__(self, master: GUI) -> None:
        super().__init__(master=master)
        self.gui: GUI = master

        self.buttons: Dict[int, ResultButton] = {}
        buttons: List[ResultButton] = self.__create_buttons()
        # Initialize values of buttons
        for button in buttons:
            num: int = self.__find_button_type(button)
            self.buttons[num] = button

        self.current_button: ResultButton = self.buttons[Button.GUN.value]
        # Tracks the current button being displayed
        # Initially set to the GunResultButton as the radio buttons also start with gun selected
        # also will display it
        self.current_button.pack()

    def __create_buttons(self) -> List[ResultButton]:
        """Makes 1 button of each ResultButton type, then returns them all as a list.
        """
        buttons: List[ResultButton] = []
        for sub_cls in ResultButton.__subclasses__():
            # Create an object of each subclass and append to list
            buttons.append(sub_cls(master=self))
        return buttons

    @staticmethod
    def __find_button_type(button: ResultButton) -> int:
        """Finds the button type according to enum Button, and return that enum type."""
        # This code will be hard coded to search for all types of ResultButton classes,
        # and enum literals Button has

        if isinstance(button, gun_result_button.GunResultButton):
            return Button.GUN.value
        elif isinstance(button, grenade_result_button.GrenadeResultButton):
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

        # At this point, have the button that needs to be displayed
        # so need to remove whatever is on the frame right now,
        # then display the button that needs to be displayed
        self.current_button.pack_forget()
        button_display.pack()

        # finally update current_button with the button we are now displaying
        self.current_button = button_display
