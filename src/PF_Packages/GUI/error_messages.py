from typing import TypeAlias
from tkinter.ttk import Label, Frame
from . import main_window

GUI: TypeAlias = 'main_window.GUI'


# Will create some labels that can be created
# these labels are error messages that tell user they put incorrect info

class ErrorMessage(Frame):
    # mapping of flag index to error
    flagIndex_to_errorMessage: dict[int, str] = {
        0: "Invalid damage input: d1 != d2",
        1: "Invalid range input: d1 < d2",
        2: "Invalid multi input: multi != 0"
    }

    def __init__(self, master: GUI) -> None:
        super().__init__(master=master)
        self.gui = master

    def add_all_error_messages(self, verify_flags: list[bool]) -> None:
        """
        Places all error messages from the error flags. Any flags set to false means there is an error.
        This doesn't place the frame itself on master, just place the error message on the frame.
        :param verify_flags: Flags telling which field verification failed
        """
        for i in range(len(verify_flags)):
            if not verify_flags[i]:
                # this flag needs an error message
                self.__add_error_message(ErrorMessage.flagIndex_to_errorMessage[i])

    def __add_error_message(self, message: str) -> None:
        """
        Adds error message to the frame.
        """
        error_label: Label = Label(master=self, text=message, foreground='#FF0000')
        error_label.pack()

    def grid_forget(self) -> None:
        super().grid_forget()
        # Need to remove all error messages
        self.__clear_error_messages()

    def __clear_error_messages(self) -> None:
        """Removes all error messages from the frame."""
        for child in self.winfo_children():
            child.destroy()
