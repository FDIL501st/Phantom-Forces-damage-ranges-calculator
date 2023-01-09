import unittest
from typing import TypeAlias
from PF_Packages.damage_function.function_calculator import FunctionCalculator
from PF_Packages.damage_info import GunDamageInfo
from PF_Packages.dataTypes import HitsToKill

DmgFuncCalc: TypeAlias = FunctionCalculator.DamageFunctionCalculator
GunDmgInfo: TypeAlias = GunDamageInfo.GunDamageInfo

class Test_test_DamageFunctionCalculator_range_hits_kill(unittest.TestCase):
    def setUp(self):
        self.MAX_HP: int = 100
        
        # Make a DamageFunctionCalculator object
        # First need damage_info

        # TRG 42 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.TRG_42: GunDmgInfo = GunDmgInfo(100, 65, 60, 160, 1, 3)
        self.TRG_42_DmgCalc: DmgFuncCalc = DmgFuncCalc(self.TRG_42, self.MAX_HP)

        # TAR-21 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.TAR_21: GunDmgInfo = GunDmgInfo(29, 22, 70, 140, 1.1, 1.5)
        self.TAR_21_DmgCalc: DmgFuncCalc = DmgFuncCalc(self.TAR_21, self.MAX_HP)
        
        # GYROJET MK 1 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.GYROJET_MK_1: GunDmgInfo = GunDmgInfo(35, 45, 35, 180, 2.25, 3.5)
        self.GYROJET_MK_1_DmgCalc: DmgFuncCalc = DmgFuncCalc(self.GYROJET_MK_1, self.MAX_HP)

    def test_TRG_42_hits_to_kill_ranges(self):
        """Tests correct range output from calculate_max_range_hits_kill for TRG 42."""
        expected_r1: float = float('inf')   # 1 headshot
        expected_r2: float = float('inf')   # 1 torso + 1 limb
        expected_r3: float = 60             # 1 limb
        expected_r4: float = 60             # 1 torso
        expected_r5: float = float('inf')   # 2 torso
        expected_r6: float = float('inf')   # 2 limb

        hits1: HitsToKill = (1, 0, 0)
        hits2: HitsToKill = (0, 1, 1)
        hits3: HitsToKill = (0, 0, 1)
        hits4: HitsToKill = (0, 1, 0)
        hits5: HitsToKill = (0, 2, 0)
        hits6: HitsToKill = (0, 0, 2)

        actual_r1: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits1)
        actual_r2: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits2)
        actual_r3: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits3)
        actual_r4: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits4)
        actual_r5: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits5)
        actual_r6: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits6)

        delta: float = 0.001
        self.assertAlmostEqual(expected_r1, actual_r1, msg=f"Didn't calculate correct max range for {hits1}", delta=delta)
        self.assertAlmostEqual(expected_r2, actual_r2, msg=f"Didn't calculate correct max range for {hits2}", delta=delta)
        self.assertAlmostEqual(expected_r3, actual_r3, msg=f"Didn't calculate correct max range for {hits3}", delta=delta)
        self.assertAlmostEqual(expected_r4, actual_r4, msg=f"Didn't calculate correct max range for {hits4}", delta=delta)
        self.assertAlmostEqual(expected_r5, actual_r5, msg=f"Didn't calculate correct max range for {hits5}", delta=delta)
        self.assertAlmostEqual(expected_r6, actual_r6, msg=f"Didn't calculate correct max range for {hits6}", delta=delta)

if __name__ == '__main__':
    unittest.main()
