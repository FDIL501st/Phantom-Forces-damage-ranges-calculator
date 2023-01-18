from typing import Tuple
from tkinter import Tk, StringVar


class GUI:
    """The main GUI window.
    This class will call upon all the other features that are used."""

    def __init__(self) -> None:
        self.win: Tk = Tk()     #represents the main window of the GUI

        #Configure the  main window
        self.win.title("Phantom Forces Damage Ranges App")  # name of the window
        self.win.geometry("600x400")    # size of the window


        self.weapon: StringVar = StringVar()    # stores result of radio button for weapon type
        self.weapon.initialize("gun")
        # Set default to gun being selected if use GUI without selecting a button

        # For values below, might decide to just have them set when they actually are set
        # Then just need to check for Attribute Error when running GUI without setting the values
        self.damage: Tuple[float, float] = None
        self.damage_ranges: Tuple[float, float] = None
        self.head_multi: float = 0
        self.torso_multi: float = 0
        # Stores damage information, will be set to actual values later when using GUI


    def createGUI(self) -> None:
        """Creates the main window of the GUI and runs it."""

        self.win.mainloop()


if __name__ == '__main__':
    # Testing GUI
    gui = GUI()
    gui.createGUI()