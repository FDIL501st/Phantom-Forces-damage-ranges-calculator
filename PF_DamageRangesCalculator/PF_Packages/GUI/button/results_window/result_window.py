from typing import TypeAlias
from tkinter import ttk, StringVar, Toplevel
from ....dataTypes import HitsToKill

Label: TypeAlias = ttk.Label
Button: TypeAlias = ttk.Button


class ResultWindow(Toplevel):
    """
    Window that displays the results of the calculations done when the button is pressed.
    """

    def __init__(self, results: HitsToKill) -> None:
        super().__init__()
        # Will not link to gui, as want this window to be separate
        # allows for more flexibility on user end

        self.__results: HitsToKill = results

        # configure the window
        self.title("Results")  # window title
        self.size("400x400")

        # Add the widgets and related variables
        self.display_text: StringVar = StringVar()
        self.display_label: Label = Label(master=self, textvariable=self.display_text)
        self.back_button: Button = Button(master=self, command=self.close)

    def close(self) -> None:
        """Closes the window."""
        self.destroy()
