from typing import TypeAlias
from . import button_frame
from .result_button import ResultButton
from ...parser.damage_info_control import DamageInfoControl
from ...damage_info import DamageInfo

ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'
DamageInfo: TypeAlias = 'DamageInfo.DamageInfo'


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

        if damage_info_control.verify_all_fields():
            # having verified the fields, now we can calculate and display the results

            gun_dmg_info: DamageInfo = damage_info_control.createDamageInfo()
            gun_dmg_info.calculate_killing_ranges()
            # now gun_dmg_info.calculator has result


        else:
            self.gui.error_message.grid(row=1, column=1)
