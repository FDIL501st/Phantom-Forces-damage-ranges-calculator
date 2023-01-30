from typing import TypeAlias
from .result_button import ResultButton
from . import button_frame
from ...parser.damage_info_control import DamageInfoControl

ButtonFrame: TypeAlias = 'button_frame.ButtonFrame'


class GunResultButton(ResultButton):
    """Class for the button when pressed should
    calculate hits to kill of a gun and
    display the results.
    """

    def __init__(self, master: ButtonFrame) -> None:
        super().__init__(master=master)
        gun_label: str = "Calculate hits to kill"
        self.label.set(gun_label)
        self.config(command=self.calculate_hits_to_kill)

    def calculate_hits_to_kill(self) -> None:
        """Reads gun damage info(damage, damage ranges and multis) from GUI fields,
        calculates all hits to kills and displays the result.
        """

        # At the moment, won't do everything, just do a quick test if verify works or not
        damage_info_control: DamageInfoControl = DamageInfoControl(damage_frame=self.gui.damage_frame,
                                                                   multi_frame=self.gui.multi_frame)
        # So print result of verify
        print(damage_info_control.verify_all_fields())
