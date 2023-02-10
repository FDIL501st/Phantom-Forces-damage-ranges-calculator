from typing import TypeAlias
import tkinter
from tkinter import ttk, StringVar

Frame: TypeAlias = ttk.Frame
Label: TypeAlias = ttk.Label
Entry: TypeAlias = ttk.Entry


class DamageFrame(Frame):
    """The frame containing damage and damage ranges entry/text fields."""

    def __init__(self, master: tkinter.Misc) -> None:
        super().__init__(master)

        self.damage: StringVar = StringVar()  # Stores data from dmg_entry
        self.damage_range: StringVar = StringVar()  # stores data from dmg_range_entry

        # create the grid to place the widgets in
        self.__createGrid()

        # Add the labels for the damage fields
        self.__createLabel()

        # Add the entry widget for the damage fields
        self.__createEntry()

    def __createGrid(self) -> None:
        """Creates the grid for the frame."""
        # Will make a 2x2 grid, equal spacing    
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

    def __createLabel(self) -> None:
        """Creates the label for damage fields."""
        dmg_label: Label = Label(master=self, text="Damage")
        dmg_label.grid(column=0, row=0)

        dmg_range_label: Label = Label(master=self, text="Damage Ranges")
        dmg_range_label.grid(column=0, row=1)

    def __createEntry(self) -> None:
        """Creates the entry widgets for the damage fields"""
        dmg_entry: Entry = Entry(master=self, textvariable=self.damage)
        dmg_entry.grid(column=1, row=0)

        dmg_range_entry: Entry = Entry(master=self, textvariable=self.damage_range)
        dmg_range_entry.grid(column=1, row=1)
