from typing import TypeAlias
import unittest
from ..PF_Packages.damage_function.function_calculator import FunctionCalculator
from ..PF_Packages.damage_info import GunDamageInfo

DmgFuncCalc: TypeAlias = 'FunctionCalculator.DamageFunctionCalculator'
GunDmgInfo: TypeAlias = 'GunDamageInfo.GunDamageInfo'

class Test_test_DamageFunctionCalculator_damage_one_hit(unittest.TestCase):

    def setup(self):
        # Make a DamageFunctionCalculator object
        # First need damage_info
        MAX_HP: int = 100
        # TRG 42 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        TRG_42: GunDmgInfo = GunDmgInfo(100, 65, 60, 160, 1, 3)
        TRG_42_DmgCalc: DmgFuncCalc = DmgFuncCalc(TRG_42, MAX_HP)

        # TAR-21 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        TAR_21: GunDmgInfo = GunDmgInfo(29, 22, 70, 140, 1.1, 1.5)
        TAR_21_DmgCalc: DmgFuncCalc = DmgFuncCalc(TAR_21, MAX_HP)
        
        # GYROJET MK 1 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        GYROJET_MK_1: GunDmgInfo = GunDmgInfo(35, 45, 35, 180, 2.25, 3.5)
        GYROJET_MK_1_DmgCalc: DmgFuncCalc = DmgFuncCalc(GYROJET_MK_1, MAX_HP)

                
    def test_A(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
