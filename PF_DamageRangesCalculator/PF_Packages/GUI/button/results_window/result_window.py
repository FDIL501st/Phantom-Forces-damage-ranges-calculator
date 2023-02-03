from typing import TypeAlias
from tkinter import ttk, Toplevel
from ....dataTypes import HitsToKill

Label: TypeAlias = ttk.Label
Button: TypeAlias = ttk.Button


class ResultWindow(Toplevel):
    """
    Window that displays the results of the calculations done when the button is pressed.
    """

    count: int = 0  # counts number of results window created

    def __init__(self, results: HitsToKill) -> None:
        super().__init__()
        # Will not link to gui, as want this window to be separate
        # allows for more flexibility on user end as can make more than 1

        ResultWindow.count += 1  # add 1 to count as a new window was created

        self.__results_str: str = ""
        for hits_to_kill, kill_range in results.items():
            self.__results_str += hits_to_kill + ', ' + str(kill_range) + '\n'
        # TODO - better results formatting

        # configure the window
        self.title("Results" + str(ResultWindow.count))  # window title
        self.geometry("400x400")  # window size

        # Add the widgets and related variables

        self.display_label: Label = Label(master=self, text=self.__results_str)
        self.back_button: Button = Button(master=self, command=self.close)
        self.save_button: Button = Button(master=self, command=self.save_results)

        self.display_label.pack()
        # TODO - better placements of widgets

    def close(self) -> None:
        """Closes the window."""
        self.destroy()

    def save_results(self) -> None:
        """Creates a .txt file to which the results are written into.
        Then the .txt file will be saved within a local folder.
        """
