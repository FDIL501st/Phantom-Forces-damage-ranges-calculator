from typing import TypeAlias
from tkinter.ttk import Label
from . import main_window

GUI: TypeAlias = 'main_window.GUI'


# Will create some labels that can be created
# these labels are error messages that tell user they put incorrect info

class ErrorMessage(Label):

    def __init__(self, master: GUI) -> None:
        super().__init__(master=master)
        self.gui = master
        self.config(text="Invalid damage info entered.", foreground='#FF0000')

    # consider a way for different variations of error messages via decorator pattern
