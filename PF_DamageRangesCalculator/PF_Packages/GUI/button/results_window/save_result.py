from typing import TypeAlias, List
from tkinter import ttk
import os

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

        # Issue with checking results here is if open multiple results windows,
        # then press save on all of them, only 1 file gets saved, not all of them
        # as the files in the directory at the creation of the windows don't have those save files

        # This only work if open a new window after saving results from another window
        self.__results_directory_path: str = "./Results"
        # First check if Results directory exists
        if not os.path.isdir(self.__results_directory_path):
            # if it doesn't, create the directory
            os.mkdir(self.__results_directory_path)
        # At this point, Results directory exists

        # find all files that already exist within directory
        self.files: List[str] = os.listdir(self.__results_directory_path)

    def __save(self) -> None:
        """Creates a file and puts results in it.
        Files are saved in a directly called Results.
        Will not be replacing any previously created files.
        Nor will they be deleted.
        """

        # do a loop to find a file name that doesn't exist
        i: int = 1
        filename: str = "result"
        while True:
            potential_name: str = filename+str(i)+".txt"
            if potential_name not in self.files:
                # found the name to use
                filename = potential_name
                break

            # need to loop to next potential name
            i += 1

        # at this point, have a filename that doesn't exist right now
        pathname: str = os.path.join(self.__results_directory_path, filename)

        with open(pathname, 'w') as f:
            f.write(self.__results)
