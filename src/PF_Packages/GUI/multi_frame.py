from typing import TypeAlias
import tkinter
from tkinter import ttk, StringVar

Frame: TypeAlias = ttk.Frame
Label: TypeAlias = ttk.Label
Entry: TypeAlias = ttk.Entry


class MultiFrame(Frame):
    """The frame containing torso and head multi extry/text fields."""

    def __init__(self, master: tkinter.Misc) -> None:
        super().__init__(master)

        self.torso_multi: StringVar = StringVar()  # Stores data from torso_entry
        self.head_multi: StringVar = StringVar()  # stores data from head_entry

        # create the grid to place the widgets in
        self.__createGrid()

        # Add the labels for the multi fields
        self.__createLabel()

        # Add the entry widget for the multi fields
        self.__createEntry()

    def __createGrid(self) -> None:
        """Creates the grid for the frame."""
        # Will make a 2x2 grid, equal spacing    
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

    def __createLabel(self) -> None:
        """Creates the label for multi fields."""
        head_label: Label = Label(master=self, text="Head multiplier")
        head_label.grid(column=0, row=0)

        torso_label: Label = Label(master=self, text="Torso multiplier")
        torso_label.grid(column=0, row=1)

    def __createEntry(self) -> None:
        """Creates the entry widgets for the multi fields"""
        head_entry: Entry = Entry(master=self, textvariable=self.head_multi)
        head_entry.grid(column=1, row=0)

        torso_entry: Entry = Entry(master=self, textvariable=self.torso_multi)
        torso_entry.grid(column=1, row=1)
