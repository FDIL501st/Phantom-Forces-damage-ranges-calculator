from typing import TypeAlias, List, Optional
from .PF_regex import PF_Regex
from ..GUI import multi_frame, damage_frame
from ..damage_info import GunDamageInfo, GrenadeDamageInfo, DamageInfo

DamageFrame: TypeAlias = 'damage_frame.DamageFrame'
MultiFrame: TypeAlias = 'multi_frame.MultiFrame'
DmgInfo: TypeAlias = 'DamageInfo.DamageInfo'


class DamageInfoControl:
    """Deals with the information damage information from the GUI.
    This includes verifying proper data given, parsing the data
    and passing it on to one of the DamageInfo classes.
    """

    def __init__(self, damage_frame: DamageFrame, multi_frame: Optional[MultiFrame] = None) -> None:
        """Reads all fields from GUI."""
        # First get values from all the entry fields
        self.__damage: str = damage_frame.damage.get()
        self.__damage_range: str = damage_frame.damage_range.get()

        if multi_frame:
            # Can send None to multi_frame if dealing with grenade damage
            # So only get values if dealing with a gun(thus multis are relevant)
            self.__head_multi: str = multi_frame.head_multi.get()
            self.__torso_multi: str = multi_frame.torso_multi.get()
            self.__have_multis: bool = True
        else:
            self.__have_multis: bool = False

        # self.__have_multis stores if we have multi fields or not

    def verify_all_fields(self) -> List[bool]:
        """Verifies all the fields provided.
        Returns a list of flags which tracks which fields have issues or not.
        Any True means verify passed. False means verify failed.
        Order of flags are: damage, damage ranges, multis(if applicable)"""

        verify_flags: List[bool] = [True for i in range(2)]
        verify_flags[0] = self.__verify_damage()
        verify_flags[1] = self.__verify_damageRange()

        if self.__have_multis:
            verify_flags.append(self.__verify_multis())

        return verify_flags

    def __verify_damage(self) -> bool:
        """
        Verifies the damage field from the GUI.
        This means having 2 non-negative numbers.
        Also checks if both numbers are not the same.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in the fields.
        """
        # Calculations fails if damage drop is 0 (e.g. 24 -> 24)
        # Also at that point this calculator isn't needed

        if not PF_Regex.match_two_nums(self.__damage):
            return False
        # Calculations fails if damage drop is 0 (e.g. 24 -> 24)
        # So need to check for that, this app won't support no damage drop
        damages: list[float] = PF_Regex.find_all_nums(self.__damage)
        if damages[0] == damages[1]:
            return False

        # passed all checks, can return True
        return True

    def __verify_damageRange(self) -> bool:
        """
        Verifies the damage range field from the GUI.
        This means having 2 non-negative numbers.
        Also check if second number is greater than first number. 
        Now allowed to give ranges in opposite order.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in the fields.
        """
        match_result: bool = PF_Regex.match_two_nums(self.__damage_range)
        if match_result:
            # Need to check if second number greater than first number
            ranges: List[float] = PF_Regex.find_all_nums(self.__damage_range)
            if ranges[0] < ranges[1]:
                return True

        return False

    def __verify_multis(self) -> bool:
        """Verifies the head and toro multi fields from the GUI.
        All this means is having a positive number. This also includes decimals.
        Returns true if all fields can be used/are in proper format.
        Returns false if there is an issue with the data in the fields."""
        head_result: bool = PF_Regex.match_one_non_zero_num(self.__head_multi)
        torso_result: bool = PF_Regex.match_one_non_zero_num(self.__torso_multi)
        return head_result and torso_result

    def createDamageInfo(self) -> DmgInfo:
        """Parses the data and creates one of the DamageInfo objects.
        If have multis, creates GunDamageInfo object. 
        If not, then GrenadeDamageInfo object.
        Should be used after using the verify_all_fields() and it returns true.
        Not doing so may result in an exception being thrown.
        """
        # Extract damage info and damage range info
        # get this first as common between all DamageInfo classes
        damage_result: List[float] = PF_Regex.find_all_nums(self.__damage)
        damage_range_result: List[float] = PF_Regex.find_all_nums(self.__damage_range)

        d1: float = damage_result[0]
        d2: float = damage_result[1]

        r1: float = damage_range_result[0]
        r2: float = damage_range_result[1]

        if self.__have_multis:
            # Extract multi info
            h_multi_result: List[float] = PF_Regex.find_all_nums(self.__head_multi)
            t_multi_result: List[float] = PF_Regex.find_all_nums(self.__torso_multi)

            h_multi: float = h_multi_result[0]
            t_multi: float = t_multi_result[0]

            # Now have all needed info, create and return GunDamageInfo object
            return GunDamageInfo.GunDamageInfo(d1, d2, r1, r2, t_multi, h_multi)

        else:
            # Don't have multis, so create and return GrenadeDamageInfo object
            return GrenadeDamageInfo.GrenadeDamageInfo(d1, d2, r1, r2)
