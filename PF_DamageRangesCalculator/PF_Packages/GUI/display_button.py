from typing import TypeAlias
import tkinter
from tkinter import ttk

Button: TypeAlias = ttk.Button


class DisplayButton(Button):
    """The button from when pressed should do some calculations and display the results.
    This class is the parent class of the button classes that will be actual buttons placed on the GUI.
    """
    def __init__(self, master: tkinter.Misc) -> None:
        super().__init__(master)


