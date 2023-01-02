from typing import TypeAlias
import unittest
from PF_Packages.damage_function.function_calculator import FunctionCalculator
from PF_Packages.damage_info import GunDamageInfo
from PF_Packages.dataTypes import Hit

DmgFuncCalc: TypeAlias = FunctionCalculator.DamageFunctionCalculator
GunDmgInfo: TypeAlias = GunDamageInfo.GunDamageInfo

class Test_test_DamageFunctionCalculator_damage_one_hit(unittest.TestCase):
    def setUp(self):
        self.MAX_HP: int = 100
        
        # Make a DamageFunctionCalculator object
        # First need damage_info

        # TAR-21 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.TAR_21: GunDmgInfo = GunDmgInfo(29, 22, 70, 140, 1.1, 1.5)
        self.TAR_21_DmgCalc: DmgFuncCalc = DmgFuncCalc(self.TAR_21, self.MAX_HP)
        
        # GYROJET MK 1 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.GYROJET_MK_1: GunDmgInfo = GunDmgInfo(35, 45, 35, 180, 2.25, 3.5)
        self.GYROJET_MK_1_DmgCalc: DmgFuncCalc = DmgFuncCalc(self.GYROJET_MK_1, self.MAX_HP)


    def test_TRG_42_damage(self):
        """Test damage of TRG_42 at given ranges."""
        # Make a DamageFunctionCalculator object
        # First need damage_info

        # TRG 42 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        TRG_42: GunDmgInfo = GunDmgInfo(100, 65, 60, 160, 1, 3)
        TRG_42_DmgCalc: DmgFuncCalc = DmgFuncCalc(TRG_42, self.MAX_HP)

        d1: float = 0
        self.fail("Test not implemented")

    def test_GYROJET_MK_1_limb_damage(self):
        """Test limb damage of GYROJET_MK_1 at given ranges."""
        hit_type: Hit = Hit.Base
        # min_range = 35 studs
        # max_range - 180 studs

        #Expected damage values
        expected_d1: float = 35                 # 1 limb shot before min_range (20 studs)
        expected_d2: float = expected_d1        # 1 limb shot at min_range
        expected_d3: float = 36.034             # 1 limb shot at 50 studs
        expected_d4: float = 38.103             # 1 limb shot at 80 studs
        expected_d5: float = 39.483             # 1 limb shot at 100 studs
        expected_d6: float = 41.552             # 1 limb shot at 130 studs
        expected_d7: float = 42.931             # 1 limb shot at 150 studs
        expected_d8: float = 45                 # 1 limb shot at max_range
        expected_d9: float = expected_d8       # 1 limb shot after max_range (200 studs)
        
        #Range values to test at
        r1: float = 20
        r2: float = 35
        r3: float = 50
        r4: float = 80
        r5: float = 100
        r6: float = 130
        r7: float = 150
        r8: float = 180
        r9: float = 200

        #Calculated/Actual damage values
        actual_d1: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r1)
        actual_d2: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r2)
        actual_d3: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r3)
        actual_d4: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r4)
        actual_d5: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r5)
        actual_d6: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r6)
        actual_d7: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r7)
        actual_d8: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r8)
        actual_d9: float = self.GYROJET_MK_1_DmgCalc.calculate_damage_one_hit(hit_type, r9)

        # Testing if expected damage equal actual damage within 0.001, as python more accurate than desmos points
        self.assertAlmostEqual(expected_d1, actual_d1, delta=0.001,msg=f"Calculated a different damage at {r1} studs. Expected {expected_d1}. Actual {actual_d1}")
        self.assertAlmostEqual(expected_d2, actual_d2, delta=0.001,msg=f"Calculated a different damage at {r2} studs. Expected {expected_d2}. Actual {actual_d2}")
        self.assertAlmostEqual(expected_d3, actual_d3, delta=0.001,msg=f"Calculated a different damage at {r3} studs. Expected {expected_d3}. Actual {actual_d3}")
        self.assertAlmostEqual(expected_d4, actual_d4, delta=0.001,msg=f"Calculated a different damage at {r4} studs. Expected {expected_d4}. Actual {actual_d4}")
        self.assertAlmostEqual(expected_d5, actual_d5, delta=0.001,msg=f"Calculated a different damage at {r5} studs. Expected {expected_d5}. Actual {actual_d5}")
        self.assertAlmostEqual(expected_d6, actual_d6, delta=0.001,msg=f"Calculated a different damage at {r6} studs. Expected {expected_d6}. Actual {actual_d6}")
        self.assertAlmostEqual(expected_d7, actual_d7, delta=0.001,msg=f"Calculated a different damage at {r7} studs. Expected {expected_d7}. Actual {actual_d7}")
        self.assertAlmostEqual(expected_d8, actual_d8, delta=0.001,msg=f"Calculated a different damage at {r8} studs. Expected {expected_d8}. Actual {actual_d8}")
        self.assertAlmostEqual(expected_d9, actual_d9, delta=0.001,msg=f"Calculated a different damage at {r9} studs. Expected {expected_d9}. Actual {actual_d9}")
        

    def test_GYROJET_MK_1_torso_damage(self):
        """Test torso damage of GYROJET_MK_1 at given ranges."""
        expected_d1: float = 78.75  # 1 torso shot before min_range
        self.fail("Test not implemented")

    def test_GYROJET_MK_1_head_damage(self):
        """Test head damage of GYROJET_MK_1 at given ranges."""
        expected_head_d1: float = 122.5  # 1 headshot beefore min_range
        self.fail("Test not implemented")

if __name__ == '__main__':
    unittest.main()
