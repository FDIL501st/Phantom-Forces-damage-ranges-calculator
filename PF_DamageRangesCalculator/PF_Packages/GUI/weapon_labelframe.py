from typing import TypeAlias
import tkinter
from tkinter import ttk, IntVar

Labelframe: TypeAlias = ttk.Labelframe
Radiobutton: TypeAlias = ttk.Radiobutton

class WeaponLabelframe(Labelframe):
    """Labelframe containing the radio buttons for choosing weapon type."""
    def __init__(self, master: tkinter.Misc, text: str = "Weapon Type") -> None:
        super().__init__(master, text=text)

        self.weapon: IntVar = IntVar()    # stores the result of which radio button is pressed
        # gun is 0, grenade is 1

        # create the grid
        self.__createGrid()

        # create the radio buttons
        self.__createRadioButton()

    # TODO - add a command that is run whenever a button is pressed
    # it should make multi frame visible or invisible depending on self.weapon

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
            value=0
        )
        self.gun_radiobutton.grid(row=0)

        self.grenade_radiobutton: Radiobutton = Radiobutton(
            master = self,
            text="Grenade",
            variable=self.weapon,
            value=1
        )
        self.grenade_radiobutton.grid(row=1)