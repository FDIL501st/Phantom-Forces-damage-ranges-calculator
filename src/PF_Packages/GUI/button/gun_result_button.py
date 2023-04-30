from typing import TypeAlias
from . import button_frame
from .result_button import ResultButton
from .results_window.result_window import ResultWindow
from ...parser.damage_info_control import DamageInfoControl
from ...damage_info import DamageInfo

ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'
DmgInfo: TypeAlias = 'DamageInfo.DamageInfo'


class GunResultButton(ResultButton):
    """Class for the button when pressed should
    calculate hits to kill of a gun and
    display the results.
    """

    def __init__(self, master: ButtonFrame) -> None:
        super().__init__(master=master)
        gun_label: str = "Calculate hits to kill"
        self.label.set(gun_label)
        self.config(command=self.calculate_and_display)

    def calculate_and_display(self) -> None:
        # need to remove from grid of GUI if there was an error message (re-enter their data)
        self.gui.error_message.grid_forget()

        damage_info_control: DamageInfoControl = DamageInfoControl(damage_frame=self.gui.damage_frame,
                                                                   multi_frame=self.gui.multi_frame)
        # this constructor call is the only difference between the 2 buttons (gun and grenade)

        # verify all the fields before going on with calculations
        verify_flags: list[bool] = damage_info_control.verify_all_fields()
        if False in set(verify_flags):
            # there was at least 1 field with an issue
            self.gui.error_message.add_all_error_messages(verify_flags=verify_flags)
            self.gui.error_message.grid(row=1, column=1)

        else:
            # having verified all the fields, now we can calculate and display the results
            gun_dmg_info: DmgInfo = damage_info_control.createDamageInfo()
            # send the gun damage info to the ResultWindow
            result_win: ResultWindow = ResultWindow(gun_dmg_info)
