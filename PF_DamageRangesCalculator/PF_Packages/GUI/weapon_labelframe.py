from typing import TypeAlias
import tkinter
from tkinter import ttk, IntVar

Labelframe: TypeAlias = ttk.Labelframe
Radiobutton: TypeAlias = ttk.Radiobutton
Frame: TypeAlias = ttk.Frame

class WeaponLabelframe(Labelframe):
    """Labelframe containing the radio buttons for choosing weapon type."""
    def __init__(self, master: tkinter.Misc, frame: Frame ,text: str = "Weapon Type") -> None:
        super().__init__(master, text=text)

        self.frame = frame              # stores the frame which this button unmaps or maps
        self.weapon: IntVar = IntVar()    # stores the result of which radio button is pressed
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
            command=self.set_frame
        )
        self.gun_radiobutton.grid(row=0)

        self.grenade_radiobutton: Radiobutton = Radiobutton(
            master = self,
            text="Grenade",
            variable=self.weapon,
            value=1,
            command=self.set_frame
        )
        self.grenade_radiobutton.grid(row=1)

    def set_frame(self) -> None:
        """Disables or enables multi_frame depending on value of self.weapon."""
        if self.weapon.get() == 0:
            self.frame.grid(column=0, row=2)

        elif self.weapon.get() == 1:
            self.frame.grid_forget()
