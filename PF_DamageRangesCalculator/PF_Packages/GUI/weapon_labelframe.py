from typing import TypeAlias
import tkinter
from tkinter import ttk, IntVar
from . import main_window
from .button.button import Button

Labelframe: TypeAlias = ttk.Labelframe
Radiobutton: TypeAlias = ttk.Radiobutton
Frame: TypeAlias = ttk.Frame
GUI: TypeAlias = 'main_window.GUI'


class WeaponLabelframe(Labelframe):
    """Labelframe containing the radio buttons for choosing weapon type."""

    def __init__(self, master: GUI, frame: Frame, text: str = "Weapon Type") -> None:
        super().__init__(master, text=text)
        self.gui = master   # stores the GUI so can access other frames on the GUI
        self.frame = frame  # stores the frame which this button unmaps or maps
        self.weapon: IntVar = IntVar()  # stores the result of which radio button is pressed
        # gun is 0, grenade is 1

        # create the grid
        self.__createGrid()

        # create the radio buttons
        self.__createRadioButton()

    def __createGrid(self) -> None:
        """Creates the grid of the labelframe."""
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

    def __createRadioButton(self) -> None:
        """Creates the radio buttons."""
        self.gun_radiobutton: Radiobutton = Radiobutton(
            master=self,
            text="Gun",
            variable=self.weapon,
            value=0,
            command=self.set_frames
        )
        self.gun_radiobutton.grid(row=0)

        self.grenade_radiobutton: Radiobutton = Radiobutton(
            master=self,
            text="Grenade",
            variable=self.weapon,
            value=1,
            command=self.set_frames,
        )
        self.grenade_radiobutton.grid(row=1)

    def set_frames(self) -> None:
        """Disables or enables frame depending on if select gun or grenade.
        Also changes the Button that is pressed, again depending on selecting gun or grenade.
        """
        if self.weapon.get() == 0:
            for w in self.frame.winfo_children():
                # for each widget in frame, enable them.
                w['state'] = 'normal'
            # set button for calculating gun damage
            self.gui.button_frame.display_button(button_type=Button.GUN)

        elif self.weapon.get() == 1:
            for w in self.frame.winfo_children():
                # for each widget in frame, disable them.
                w['state'] = 'disabled'
                # set button for calculating grenade damage
                self.gui.button_frame.display_button(button_type=Button.GRENADE)
