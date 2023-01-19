from tkinter import Tk
from damage_frame import DamageFrame
from multi_frame import MultiFrame
from weapon_labelframe import WeaponLabelframe

class GUI(Tk):
    """The main window of the GUI.
    The main entry point to the entire GUI."""
    def __init__(self) -> None:
        super().__init__()

        #Configure the  main window
        self.title("Phantom Forces Damage Ranges App")  # name of the window
        self.geometry("600x400")                        # size of the window

        self.__createGUI()

    def __createGUI(self) -> None:
        """Creates the main window of the GUI and runs it."""
        self.__createGrid()

        self.__createFrames()


    def __createGrid(self) -> None:
        """Creates the grid of the main window."""
        # configure the rows
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=1)

        # configure the columns
        self.columnconfigure(index=0, weight=2)
        self.columnconfigure(index=0, weight=1)


    def __createFrames(self) -> None:
        """Creates the frames that will be placed on the grid."""
        self.damage_frame: DamageFrame = DamageFrame(master=self)
        self.damage_frame.grid(column=0, row=1)
        
        self.multi_frame: MultiFrame = MultiFrame(master=self)
        self.multi_frame.grid(column=0, row=2)
        
        self.weapon_frame: WeaponLabelframe = WeaponLabelframe(master=self)
        self.weapon_frame.grid(column=0, row=0)
        
if __name__ == '__main__':
    # Testing GUI
    gui = GUI()
    gui.mainloop()