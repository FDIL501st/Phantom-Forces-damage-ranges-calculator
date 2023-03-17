import tkinter
from typing import TypeAlias, Literal, final
from tkinter import scrolledtext
from . import result_window
from ....dataTypes import HitsToKill
from ....dict_sorter.HitsToKill_Sorter import HitsToKillSorter

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

    def _create_header(self, header1_top: str, header1_bot: str, header2: str) -> None:
        """Creates the headers for the 2 columns.
        Will be placed as the top row of the table.
        """
        self.insert(1.0, header1_top)
        self._end_column1(1)
        self.insert(END, header2)
        self.insert(END, '\n')
        self.insert(2.0, header1_bot)
        self._end_column1(2)
        self.insert(END, '\n')

        # Create seperator
        SEPERATOR_LENGTH: final[int] = 65
        seperator: str = ""
        for i in range(SEPERATOR_LENGTH):
            seperator += '-'
        # made line, so insert it
        self.insert(3.0, seperator)
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
        hits_to_kill_header_top: str = "Hits to Kill"
        hits_to_kill_header_bot: str = "(Headshots | Torso shots | Limb shots)"
        kill_range_header: str = "Range can kill to"
        self._create_header(hits_to_kill_header_top, hits_to_kill_header_bot, kill_range_header)
        self.__populate_table(results=results)

    def __populate_table(self, results: HitsToKill) -> None:
        """Populates the table with data from results
        and places it on the frame.
        """
        # Where we implement the data structure to sort results
        results_sorted: HitsToKillSorter = HitsToKillSorter(hits_to_kill=results)

        line_num: int = 3
        # keeps track which line we insert into
        # skip first 3 lines because they are for header
        for hits_to_kill in results_sorted:
            # read off the tuple
            kill_hits: str = hits_to_kill[0]
            kill_range: float = hits_to_kill[1]

            # add 1 to line_num as inserting to next line
            line_num += 1

            # insert kill_hits
            self.insert(float(line_num), kill_hits)
            # add in column seperator
            self._end_column1(line_num=line_num)
            # insert kill_range, will round to 1 decimal place
            self.insert(END, round(kill_range, 1))
            # move to next line
            self.insert(END, '\n')
            # Now we can loop


class GrenadeResultTable(ResultTable):
    """Class represents the result table for grenade results."""

    def __init__(self, master: ResultWindow, results: HitsToKill) -> None:
        """Will create the table with all the results placed within the frame.
        To see the results, just need to place the frame on the master widget.
        """
        super().__init__(master=master, results=results)
        self._create_header(header1_top="Grenade", header1_bot='', header2="Grenade kill radius")
        self.__display_results(results=results)

    def __display_results(self, results: HitsToKill) -> None:
        """Inserts the grenade results to the text widget, so it can be displayed."""
        self._end_column1(line_num=4)
        # round kill radius to 1 decimal place
        self.insert(END, round(results.get("Grenade kill radius"), 1))
