from typing import TypeAlias
from tkinter import ttk, Scrollbar
from . import result_window
from ....dataTypes import HitsToKill

ResultWindow: TypeAlias = 'result_window.ResultWindow'
Frame: TypeAlias = ttk.Frame
Label: TypeAlias = ttk.Label
Style: TypeAlias = ttk.Style


class ResultTable(Frame):
    """Class representing the table used to show the results in."""

    def __init__(self, master: ResultWindow, results: HitsToKill) -> None:
        """Common constructor for all child classes."""
        super().__init__(master=master)

        self.create_scrollbar(num_row=len(results))
        self.style = Style(master=self)
        # thus the style exists as a child of the frame

        # Create a custom style for all labels

        # Note to self: styles have a hierarchy, with TLabel on top
        # all styles under TLabel will inherit TLabel if doesn't override it
        # Left.TLabel is under TLabel
        # Heading.Left.TLabel is under Left, which is under TLabel

        self.style.configure('Table.TLabel', height=2, relief='groove', borderwidth=1)
        # potential relief: groove, solid, ridge
        # all labels will have height of 2,
        # with border of groove and border width of 1

        self.style.configure('Left.Table.TLabel', width=40)
        self.style.configure('Right.Table.TLabel', width=20)
        # left column will have width of 40, right one 20

        self.style.configure('H1.Left.Table.TLabel', relief='solid', borderwidth=10)
        self.style.configure('H2.Right.Table.TLabel', relief='solid', borderwidth=10)
        # headers will have solid borders
        # Unsure if this is working or not

    def create_header(self, header1: str, header2: str) -> None:
        """Creates the headers for the 2 columns.
        Will be placed as the top row of the table.
        """
        # create the header labels
        header1_label: Label = Label(master=self, text=header1, style='H1.Left.Table.TLabel')
        header2_label: Label = Label(master=self, text=header2, style='H2.Right.Table.TLabel')

        # place the header labels
        header1_label.grid(row=0, column=0)
        header2_label.grid(row=0, column=1)

    def create_scrollbar(self, num_row: int) -> None:
        """Creates a vertical scrollbar and places it on the right side."""
        scrollbar: Scrollbar = Scrollbar(master=self, orient='vertical')
        scrollbar.grid(row=0, column=2, rowspan=num_row)
        # Seems that frames can't accept scrollbars, need a different widget
        # self.config(yscrollcommand=scrollbar.set)
        # scrollbar.config(command=self.yview)


class GunResultTable(ResultTable):
    """Class representing the table used to show gun results in."""

    def __init__(self, master: ResultWindow, results: HitsToKill) -> None:
        """Will create the table with all the results placed within the frame.
        To see the results, just need to place the frame on the master widget.
        """
        super().__init__(master=master, results=results)
        self.create_header("Hits to Kill", "Range it can kill to")
        self.populate_table(results=results)

    def populate_table(self, results: HitsToKill) -> None:
        """Populates the table with data from results
        and places it on the frame.
        """
        # TODO - Maybe moved to parent class
        num_row: int = 1  # keeps track of what row to insert to
        for hits, kill_range in results.items():
            # create the labels
            hits_label: Label = Label(master=self, text=hits, style='Left.Table.TLabel')
            range_label: Label = Label(master=self, text=str(kill_range), style='Right.Table.TLabel')

            # place the labels on self
            hits_label.grid(row=num_row, column=0)
            range_label.grid(row=num_row, column=1)
            num_row += 1  # add 1 to num_row for next loop having correct row number
        # TODO - figure out a way to solve issues when have so many items in results, goes offscreen
        # even with fullscreen being used
