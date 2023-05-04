import tkinter
from typing import TypeAlias, Literal
from tkinter import scrolledtext
from . import result_window
from ....dataTypes import HitsToKill
from ....dict_sorter.HitsToKill_Sorter import HitsToKillSorter
from ....damage_info import GunDamageInfo, GrenadeDamageInfo, DamageInfo

ResultWindow: TypeAlias = 'result_window.ResultWindow'
ScrolledText: TypeAlias = scrolledtext.ScrolledText
END: Literal["end"] = tkinter.END
GunDmgInfo: TypeAlias = 'GunDamageInfo.GunDamageInfo'
GrenDmgInfo: TypeAlias = 'GrenadeDamageInfo.GrenadeDamageInfo'
DmgInfo: TypeAlias = 'DamageInfo.DamageInfo'


class ResultTable(ScrolledText):
    """Class representing the table used to show the results in.
    Table will be made in a Text widget.
    """

    def __init__(self, master: ResultWindow, dmg_info: DmgInfo) -> None:
        """Common constructor for all child classes."""
        super().__init__(master=master)

        # calculate results
        dmg_info.calculate_killing_ranges()
        self._results: HitsToKill = dmg_info.calculator.hits_to_kill
        # self._num_results = len(self._results)  # number of results to display
        self._dmg_info: DmgInfo = dmg_info

        # current line number to write in
        # should be +1 everytime a '\n' is added
        self._line_num: int = 1

    def _create_header(self, header1_top: str, header1_bot: str, header2: str) -> None:
        """Creates the headers for the 2 columns.
        Will be placed as the top row of the table.
        """
        self.insert(float(self._line_num), header1_top)
        self._end_column1(line_num=self._line_num)
        self.insert(END, header2)
        self.insert(END, '\n')
        self._line_num += 1
        self.insert(float(self._line_num), header1_bot)
        self._end_column1(self._line_num)
        self.insert(END, '\n')
        self._line_num += 1

        # Create seperator
        SEPERATOR_LENGTH: int = 65
        seperator: str = ""
        for i in range(SEPERATOR_LENGTH):
            seperator += '-'
        # made line, so insert it
        self.insert(float(self._line_num), seperator)
        self.insert(END, '\n')
        self._line_num += 1

    def _end_column1(self, line_num: int) -> None:
        """Inserts spaces and | to end the first column.
        Should be used before inserting second column.
        """

        col1_text: str = self.get(float(line_num), END)

        # Now can calculate how much spaced needs to be added
        # give col1_text max 50 characters, fill spaced up to that
        # and then add a | and a space
        COL1_MAX: int = 45

        num_spaces: int = COL1_MAX - len(col1_text)
        # insert that many spaces using a loop
        for i in range(num_spaces):
            self.insert(END, " ")

        # finally insert the column separator
        self.insert(END, "| ")

    def get_text(self) -> str:
        """Gets the entire table displayed as string.
        """
        return self.get(1.0, END)


class GunResultTable(ResultTable):
    """Class representing the table used to show gun results in."""

    def __init__(self, master: ResultWindow, gun_dmg_info: GunDmgInfo) -> None:
        """Will create the table with all the results placed within the frame.
        To see the results, just need to place the frame on the master widget.
        """
        super().__init__(master=master, dmg_info=gun_dmg_info)
        hits_to_kill_header_top: str = "Hits to Kill"
        hits_to_kill_header_bot: str = "(Headshots | Torso shots | Limb shots)"
        kill_range_header: str = "Range can kill to"
        self._create_header(hits_to_kill_header_top, hits_to_kill_header_bot, kill_range_header)
        self.__populate_table(results=self._results)

    def __populate_table(self, results: HitsToKill) -> None:
        """Populates the table with data from results
        and places it on the frame.
        """
        # Where we implement the data structure to sort results
        results_sorted: HitsToKillSorter = HitsToKillSorter(hits_to_kill=results)

        for hits_to_kill in results_sorted:
            # read off the tuple
            kill_hits: str = hits_to_kill[0]
            kill_range: float = hits_to_kill[1]

            # insert kill_hits
            self.insert(float(self._line_num), kill_hits)
            # add in column seperator
            self._end_column1(line_num=self._line_num)
            # insert kill_range, will round to 1 decimal place
            self.insert(END, str(round(kill_range, 1)))
            # move to next line
            self.insert(END, '\n')
            self._line_num += 1

            # Now we can loop to display next line

    def _create_header(self, header1_top: str, header1_bot: str, header2: str) -> None:
        # first display stats of the damage
        self.insert(float(self._line_num), str(self._dmg_info))
        self.insert(END, '\n')
        self._line_num += 2
        # add 2 as the gun damage stats takes 2 lines

        # blank line to separate from actual table
        self.insert(float(self._line_num), '\n')
        self._line_num += 1

        # now put rest of header from parent
        super()._create_header(header1_top=header1_top, header1_bot=header1_bot, header2=header2)


class GrenadeResultTable(ResultTable):
    """Class represents the result table for grenade results."""

    def __init__(self, master: ResultWindow, gren_dmg_info: GrenDmgInfo) -> None:
        """Will create the table with all the results placed within the frame.
        To see the results, just need to place the frame on the master widget.
        """
        super().__init__(master=master, dmg_info=gren_dmg_info)
        self._create_header(header1_top="Grenade", header1_bot='', header2="Grenade kill radius")
        self.__display_results(results=self._results)

    def __display_results(self, results: HitsToKill) -> None:
        """Inserts the grenade results to the text widget, so it can be displayed."""
        self._end_column1(self._line_num)
        # round kill radius to 1 decimal place
        self.insert(END, str(round(results.get("Grenade kill radius"), 1)))
        self.insert(END, '\n')
        self._line_num += 1

    def _create_header(self, header1_top: str, header1_bot: str, header2: str) -> None:
        # first display stats of the damage
        self.insert(float(self._line_num), str(self._dmg_info))
        self.insert(END, '\n')
        self._line_num += 1
        # add 1 as the grenade damage stats takes 1 line

        # blank line to separate from actual table
        self.insert(float(self._line_num), '\n')
        self._line_num += 1

        # now rest of header from parent
        super()._create_header(header1_top=header1_top, header1_bot=header1_bot, header2=header2)
