from typing import TypeAlias
from .result_button import ResultButton
from . import button_frame
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
        # this constructor call is the only difference between the 2 buttons

        if damage_info_control.verify_all_fields():
            # having verified the fields, now we can calculate and display the results

            gun_dmg_info: DamageInfo = damage_info_control.createDamageInfo()
            gun_dmg_info.calculate_killing_ranges()

        else:
            self.gui.error_message.grid(row=1, column=1)
