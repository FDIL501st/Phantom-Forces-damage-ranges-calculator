from typing import TypeAlias
import tkinter
from tkinter import ttk
from . import result_window

Frame: TypeAlias = ttk.Frame
Label: TypeAlias = ttk.Label
Entry: TypeAlias = ttk.Entry
StringVar: TypeAlias = tkinter.StringVar
ResultWindow: TypeAlias = 'result_window.ResultWindow'


class FileNameFrame(Frame):
    def __init__(self, master: ResultWindow) -> None:
        super().__init__(master=master)

        self.__filename: StringVar = StringVar()  # saves the __filename input by user

        self.__createLabel()
        self.__createEntry()

    def __createLabel(self) -> None:
        """Creates the label for the entry widget, telling user what they will input."""
        label_text: str = "Enter name of text file\n to which results will be saved in"
        # the label text is something to edit it enhance in the future

        self.input_filename_label: Label = Label(master=self, text=label_text)
        self.input_filename_label.pack(side=tkinter.LEFT)

    def __createEntry(self) -> None:
        """Create entry widget for user to write intput into."""
        self.input_filename: Entry = Entry(master=self, textvariable=self.__filename, width=50)
        self.input_filename.pack(side=tkinter.RIGHT)

    @property
    def filename(self) -> str:
        return self.__filename.get()

