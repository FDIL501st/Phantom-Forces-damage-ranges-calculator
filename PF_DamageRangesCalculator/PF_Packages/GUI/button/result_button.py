from typing import TypeAlias
from tkinter import ttk, StringVar
from . import button_frame
from .. import main_window
from ...parser.damage_info_control import DamageInfoControl
from ...damage_info import DamageInfo

Button: TypeAlias = ttk.Button
ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'
GUI: TypeAlias = 'main_window.GUI'
DamageInfo: TypeAlias = 'DamageInfo.DamageInfo'


# noinspection SpellCheckingInspection
class ResultButton(Button):
    """The button from when pressed should do some calculations and display the results.
    This class is the parent class of the button classes
    that will be actual buttons placed on the GUI.
    """

    def __init__(self, master: ButtonFrame) -> None:
        super().__init__(master)
        self.gui: GUI = master.gui
        self.label: StringVar = StringVar()
        # Variable to be set by children classes

        self.config(textvariable=self.label)
        # Set displayed text to label that will be set

        # Using a StringVar and textvariable, so when children classes later sets the value of label,
        # the value gets set automatically, and doesn't need to be specifically updated in children constructor

        # Also set the command here, as the command is common between the 2 buttons
        # only difference betwee buttons should be the label they have

        self.config(command=self.calculate_hits_to_kill)

    def calculate_hits_to_kill(self) -> None:
        """Reads gun damage info(damage, damage ranges and multis) from GUI fields,
        calculates all hits to kills and displays the result.
        """

        damage_info_control: DamageInfoControl = DamageInfoControl(damage_frame=self.gui.damage_frame,
                                                                   multi_frame=self.gui.multi_frame)
        if damage_info_control.verify_all_fields():
            gun_dmg_info: DamageInfo = damage_info_control.createDamageInfo()
