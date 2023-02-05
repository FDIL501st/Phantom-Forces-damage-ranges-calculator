import tkinter
from typing import TypeAlias, Literal, final
from tkinter import scrolledtext
from . import result_window
from ....dataTypes import HitsToKill

ResultWindow: TypeAlias = 'result_window.ResultWindow'
ScrolledText: TypeAlias = scrolledtext.ScrolledText
END: Literal["end"] = tkinter.END


class ResultTable(ScrolledText):
    """Class representing the table used to show the results in.
    Table will be made in a Text widget.
    """

    def __init__(self, master: ResultWindow, results: HitsToKill) -> None:
        """Common constructor for all child classes."""
        super().__init__(master=master)

        self._num_results = len(results)  # number of results to display

    def _create_header(self, header1: str, header2: str) -> None:
        """Creates the headers for the 2 columns.
        Will be placed as the top row of the table.
        """
        self.insert(1.0, header1)
        self._end_column1(1)
        self.insert(END, header2)
        self.insert(END, '\n')

        # Create seperator
        SEPERATOR_LENGTH: final[int] = 65
        seperator: str = ""
        for i in range(SEPERATOR_LENGTH):
            seperator += '-'
        # made line, so insert it
        self.insert(2.0, seperator)
        self.insert(END, '\n')

    def _end_column1(self, line_num: int) -> None:
        """Inserts spaces and | to end the first column.
        Should be used before inserting second column.
        """

        col1_text: str = self.get(float(line_num), END)

        # Now can calculate how much spaced needs to be added
        # give col1_text max 50 characters, fill spaced up to that
        # and then add a | and a space
        COL1_MAX: final[int] = 45

        num_spaces: int = COL1_MAX - len(col1_text)
        # insert that many spaces using a loop
        for i in range(num_spaces):
            self.insert(END, " ")

        # finally insert the column separator
        self.insert(END, "| ")

    def get_text(self) -> str:
        """Gets the table displayed as string.
        """
        return self.get(1.0, END)


class GunResultTable(ResultTable):
    """Class representing the table used to show gun results in."""

    def __init__(self, master: ResultWindow, results: HitsToKill) -> None:
        """Will create the table with all the results placed within the frame.
        To see the results, just need to place the frame on the master widget.
        """
        super().__init__(master=master, results=results)
        self._create_header("Hits to Kill", "Range can kill to")
        self.__populate_table(results=results)

    def __populate_table(self, results: HitsToKill) -> None:
        """Populates the table with data from results
        and places it on the frame.
        """

        line_num: int = 2
        # keeps track which line we insert into
        # skip first 2 lines because they are for header
        for kill_hits, kill_range in results.items():
            # add 1 to line_num as inserting to next line
            line_num += 1

            # insert kill_hits
            self.insert(float(line_num), kill_hits)
            # add in column seperator
            self._end_column1(line_num=line_num)
            # insert kill_range
            self.insert(END, kill_range)
            # move to next line
            self.insert(END, '\n')
            # Now we can loop
