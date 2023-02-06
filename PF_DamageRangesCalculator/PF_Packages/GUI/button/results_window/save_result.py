from typing import TypeAlias
from tkinter import ttk
from . import result_window, result_tables

Button: TypeAlias = ttk.Button
ResultWindow: TypeAlias = 'result_window.ResultWindow'
ResultTable: TypeAlias = 'result_tables.ResultTable'


class SaveButton(Button):
    """
    A button to save the results displayed into a .txt file.
    The files are saved in a local directly called Results
    """

    def __init__(self, master: ResultWindow) -> None:
        super().__init__(master=master)
        self.config(text="Save Results")
        self.config(command=self.__save)
        self.__results: str = master.result_table.get_text()

    def __save(self) -> None:
        """Creates a file and puts results in it.
        Files are saved in a directly called Results.
        Will not be replacing any previously created files.
        Nor will they be deleted.
        """

        # Need to figure out a way figure out if files exists or not
        # Currently thinking having a list, which gets filled up during constructor
        # with all file names in Results directory
        with open("./Results/result.txt", 'w') as f:
            f.write(self.__results)
