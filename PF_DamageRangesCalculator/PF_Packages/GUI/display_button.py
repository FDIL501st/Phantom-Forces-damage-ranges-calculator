from typing import TypeAlias
import tkinter
from tkinter import ttk, StringVar

Button: TypeAlias = ttk.Button


# noinspection SpellCheckingInspection
class DisplayButton(Button):
    """The button from when pressed should do some calculations and display the results.
    This class is the parent class of the button classes
    that will be actual buttons placed on the GUI.
    """
    def __init__(self, master: tkinter.Misc) -> None:
        super().__init__(master)

        self.label: StringVar = StringVar()
        # Variable to be set by children classes

        self.config(textvariable=self.label)
        # Set displayed text to label that will be set

        # Using a StringVar and textvariable, so when children classes later sets the value of label,
        # the value gets set automatically, and doesn't need to be specifically updated in children constructor


