from typing import TypeAlias, List, Set
from tkinter import ttk
import os
import regex

from . import result_window, result_tables

Button: TypeAlias = ttk.Button
ResultWindow: TypeAlias = 'result_window.ResultWindow'
ResultTable: TypeAlias = 'result_tables.ResultTable'


class SaveButton(Button):
    """
    A button to save the results displayed into a .txt file.
    The files are saved in a local directly called Results
    """

    results_directory_path: str = "./Results"  # static variable for path to Results directory
    file_nums: Set[int] = set()      # static variable holding the number for result files used

    def __init__(self, master: ResultWindow) -> None:
        super().__init__(master=master)
        self.config(text="Save Results")
        self.config(command=self.__save)
        self.__results: str = master.result_table.get_text()
        SaveButton.__initialize_file_nums()

    def __save(self) -> None:
        """Creates a file and puts results in it.
        Files are saved in a directly called Results.
        Will not be replacing any previously created files,
        unless user provided a name for a .txt file that already exist in the GUI.
        """
        # keep adding 1 to i until find a number that isn't in file_nums
        i: int = 1
        while i in self.file_nums:
            i += 1

        filename: str = "result" + str(i) + ".txt"
        # at this point, have a filename that doesn't exist right now
        pathname: str = os.path.join(SaveButton.results_directory_path, filename)

        with open(pathname, 'w') as f:
            f.write(self.__results)

        # add the i to the set as now used it
        self.file_nums.add(i)

    @classmethod
    def __initialize_file_nums(cls) -> None:
        """
        Checks Results directory for all current file Result<number>.txt files saved in it and
        stores the numbers.\n
        Will create Results directory if it doesn't exist.
        """
        # First check if Results directory exists
        if not os.path.isdir(cls.results_directory_path):
            # if it doesn't, create the directory
            os.mkdir(cls.results_directory_path)
        # At this point, Results directory exists

        # find all files that already exist within directory
        filenames: List[str] = os.listdir(cls.results_directory_path)

        # now figure out which ones start with result and store the number
        # expected format of files saved by this program is result[numbers].txt

        # regex doesn't match properly
        result_filename_pattern: regex.Pattern = regex.compile(
            r"""result(\d+).txt"""
        )

        for filename in filenames:
            # match filename with pattern
            result_filename_match: regex.Match = result_filename_pattern.fullmatch(filename)
            # check if found match
            if result_filename_match is not None:
                # store the number
                cls.file_nums.add(int(result_filename_match.group(1)))
