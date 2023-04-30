from typing import TypeAlias
from .result_button import ResultButton
from . import button_frame
from .results_window.result_window import ResultWindow
from ...parser.damage_info_control import DamageInfoControl
from ...damage_info import DamageInfo

ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'
DamageInfo: TypeAlias = 'DamageInfo.DamageInfo'


class GrenadeResultButton(ResultButton):
    """Class for the button when pressed
    should calculate killing radius of a grenade
    and display the results.
    """

    def __init__(self, master: ButtonFrame) -> None:
        super().__init__(master=master)
        grenade_label: str = "Calculate killing radius"
        self.label.set(grenade_label)

    def calculate_and_display(self) -> None:
        # need to remove from grid of GUI if there was an error message (re-enter their data)
        self.gui.error_message.grid_forget()

        damage_info_control: DamageInfoControl = DamageInfoControl(damage_frame=self.gui.damage_frame)
        # this constructor call is one of 2 difference between the 2 buttons

        # verify all the fields before going on with calculations
        verify_flags: list[bool] = damage_info_control.verify_all_fields()
        if False in set(verify_flags):
            # there is at least 1 field that has an issue
            self.gui.error_message.add_all_error_messages(verify_flags=verify_flags)
            self.gui.error_message.grid(row=1, column=1)

        else:
            # having verified all the fields, now we can calculate and display the results
            grenade_dmg_info: DamageInfo = damage_info_control.createDamageInfo()
            # send the grenade damage to the result window
            result_win: ResultWindow = ResultWindow(grenade_dmg_info, grenade=True)
            # this constructor call with grenade=True is second difference between the buttons
