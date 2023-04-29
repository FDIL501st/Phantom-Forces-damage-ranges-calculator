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
    The files are saved in a local directly called Results
    """
    # issue, recent_dir gets reset whenever new SaveButton created
    # which occurs for every new result window
    __recent_dir = './'
    # keeps track of the most recent directory used to save results
    # this is used as the initialdir of the save as file dialog

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
        filetypes: list[tuple[str, str]] = [("Text Files (.txt)", "*.txt"), ("All Files", "*.*")]
        result_file = filedialog.asksaveasfile(mode='w',
                                               initialdir=self.__recent_dir,
                                               defaultextension='*.txt',
                                               filetypes=filetypes)
        # if file was created
        if result_file is not None:
            # write into file
            result_file.write(self.__results)
            # update recent_dir
            self.__recent_dir = os.path.dirname(result_file.name)
            # close file
            result_file.close()
            # unsure if wanna close the results window as well or not
            # self.result_window.close()

        # might want to add an else in case failed to save as was unable to create the file
