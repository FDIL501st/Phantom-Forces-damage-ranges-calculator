import tkinter
from typing import TypeAlias, Literal
from tkinter import ttk, Toplevel
from . import result_tables, save_result, filename_frame
from ....dataTypes import HitsToKill

Label: TypeAlias = ttk.Label
Button: TypeAlias = ttk.Button
Entry: TypeAlias = ttk.Entry
StringVar: TypeAlias = tkinter.StringVar
BOTH: Literal["both"] = tkinter.BOTH
GunResultTable: TypeAlias = result_tables.GunResultTable
GrenadeResultTable: TypeAlias = result_tables.GrenadeResultTable
FileNameFrame: TypeAlias = filename_frame.FileNameFrame
SaveButton: TypeAlias = save_result.SaveButton


class ResultWindow(Toplevel):
    """
    Window that displays the results of the calculations done when the button is pressed.
    """

    count: int = 0  # counts number of results window created

    def __init__(self, results: HitsToKill, grenade: bool = False) -> None:
        super().__init__()
        # Will not link to gui, as want this window to be separate
        # allows for more flexibility on user end as can make more than 1

        ResultWindow.count += 1  # add 1 to count as a new window was created

        # configure the window
        self.title("Results" + str(ResultWindow.count))  # window title
        self.geometry("550x600")  # window size

        # Add the widgets and related variables

        self.back_button: Button = Button(master=self, command=self.close)
        # X button exists, to might be unneeded

        # create the result table
        if not grenade:
            self.result_table: GunResultTable = GunResultTable(master=self, results=results)
        else:
            self.result_table: GrenadeResultTable = GrenadeResultTable(master=self, results=results)
        self.result_table.pack(fill=BOTH)

        # create the widget to enter result save __filename
        self.filename_frame: FileNameFrame = FileNameFrame(master=self)
        self.filename_frame.pack()

        # create the save button
        self.save_button: SaveButton = SaveButton(master=self)
        self.save_button.pack()

    def close(self) -> None:
        """Closes the window."""
        self.destroy()
