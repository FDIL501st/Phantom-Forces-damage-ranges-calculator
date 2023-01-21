from typing import TypeAlias
from ..GUI import damage_frame, multi_frame
from .PF_regex import PF_Regex

DamageFrame: TypeAlias = 'damage_frame.DamageFrame'
MultiFrame: TypeAlias = 'multi_frame.MultiFrame'

class DamageInfoControl:
    """Deals with the information damage information from the GUI.
    This includes verifying proper data given, parsing the data
    and passing it on to one of the DamageInfo classes.
    """
    def __init__(self, damage_frame: DamageFrame, multi_frame: MultiFrame | None) -> None:
        # First get values from all the entry fields
        self.__damage: str = damage_frame.damage.get()
        self.__damage_range: str = damage_frame.damage_range.get()

        if multi_frame:
            # Can send None to multi_frame if dealing with grenade damage
            # So only get values if dealing with a gun(thus multis are relevent)
            self.__head_multi: str = multi_frame.head_multi.get()
            self.__torso_multi: str = multi_frame.torso_multi.get()
            self.__have_multis: bool = True
        else:
            self.__have_multis: bool = False

        # self.__have_multis stores if we have multi fields or not

    def verify_all_fields(self) -> bool:
        """Verifies all the fields provided.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in at least 1 fields."""
        verify_damage: bool = self.__verify_damage()
        verify_range: bool = self.__verify_damageRange()
        
        if self.__have_multis:
            verify_multi: bool = self.__verify_multis()
            return verify_damage and verify_range and verify_multi

        return verify_damage and verify_range

    def __verify_damage(self) -> bool:
        """"Verifies the damage field from the GUI. 
        This means having 2 non-negative numbers numbers.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in the fields."""
        return PF_Regex.match_two_non_neg_nums(self.__damage)

    def __verify_damageRange(self) -> bool:
        """"Verifies the damage range field from the GUI. 
        This means having 2 non-negative numbers.
        Also check if second number is greater than first number. 
        Now allowed to give ranges in opposite order.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in the fields."""
        match_result: bool = PF_Regex.match_two_non_neg_nums(self.__damage_range)
        if match_result:
            # Need to figure out parsing out the numbers, prob need another function from PF_regex
            pass

        return False

    def __verify_multis(self) -> bool:
        """Verifies the head and toro multi fields from the GUI.
        All this means is have a positive number. This also includes decimals.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in the fields."""
        head_result: bool = PF_Regex.match_one_pos_num(self.__head_multi)
        torso_result: bool = PF_Regex.match_one_pos_num(self.__torso_multi)
        return head_result and torso_result
            
    def createDamageInfo(self) -> None:
        """Parses the data and creates a DamageInfo class.
        Should be used after using the verify_all_fields() and it returning true.
        Not doing so can result in an exception being thrown.
        """