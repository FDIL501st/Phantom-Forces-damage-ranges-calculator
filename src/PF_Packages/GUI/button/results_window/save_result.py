from typing import TypeAlias
from tkinter import ttk, filedialog
import os.path

from . import result_window, result_tables

Button: TypeAlias = ttk.Button
ResultWindow: TypeAlias = 'result_window.ResultWindow'
ResultTable: TypeAlias = 'result_tables.ResultTable'


class SaveButton(Button):
    """
    A button to save the results displayed into a .txt file.
    """

    __recent_dir: str = './'
    # keeps track of the most recent directory used to save results
    # this is used as the initial directory of the save as file dialog
    # helpful feature of repeated use when trying to save into the same place

    def __init__(self, master: ResultWindow) -> None:
        super().__init__(master=master)
        self.result_window: ResultWindow = master
        self.config(text="Save Results")
        self.config(command=self.__save)
        self.__results: str = master.result_table.get_text()

    def __save(self) -> None:
        """
        Creates a file and puts results in it.
        """
        filetypes: list[tuple[str, str]] = [("Text Files (.txt)", "*.txt")]
        result_file = filedialog.asksaveasfile(mode='w',
                                               initialdir=self.__recent_dir,
                                               defaultextension='*.txt',
                                               filetypes=filetypes)
        # if file was created
        if result_file is not None:
            # write into file
            result_file.write(self.__results)
            # update recent_dir
            SaveButton.__recent_dir = os.path.dirname(result_file.name)
            # close file
            result_file.close()
            # close the result window as to reduce opened windows by the app
            self.result_window.close()

        # might want to add an else in case failed to save as was unable to create the file
