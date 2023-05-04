import unittest
from typing import TypeAlias
from PF_Packages.damage_function.function_calculator import FunctionCalculator
from PF_Packages.damage_info import GunDamageInfo
from PF_Packages.dataTypes import Hits

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
        # Expected ranges
        expected_r1: float = float('inf')   # 1 headshot
        expected_r2: float = float('inf')   # 1 torso + 1 limb
        expected_r3: float = 60             # 1 limb
        expected_r4: float = 60             # 1 torso
        expected_r5: float = float('inf')   # 2 torso
        expected_r6: float = float('inf')   # 2 limb

        # Hits to kill
        hits1: Hits = (1, 0, 0)
        hits2: Hits = (0, 1, 1)
        hits3: Hits = (0, 0, 1)
        hits4: Hits = (0, 1, 0)
        hits5: Hits = (0, 2, 0)
        hits6: Hits = (0, 0, 2)

        # Actual ranges
        actual_r1: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits1)
        actual_r2: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits2)
        actual_r3: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits3)
        actual_r4: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits4)
        actual_r5: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits5)
        actual_r6: float = self.TRG_42_DmgCalc.calculate_max_range_hits_kill(hits6)
        
        # Tests
        delta: float = 0.001
        self.assertAlmostEqual(expected_r1, actual_r1, msg=f"Didn't calculate correct max range for {hits1}", delta=delta)
        self.assertAlmostEqual(expected_r2, actual_r2, msg=f"Didn't calculate correct max range for {hits2}", delta=delta)
        self.assertAlmostEqual(expected_r3, actual_r3, msg=f"Didn't calculate correct max range for {hits3}", delta=delta)
        self.assertAlmostEqual(expected_r4, actual_r4, msg=f"Didn't calculate correct max range for {hits4}", delta=delta)
        self.assertAlmostEqual(expected_r5, actual_r5, msg=f"Didn't calculate correct max range for {hits5}", delta=delta)
        self.assertAlmostEqual(expected_r6, actual_r6, msg=f"Didn't calculate correct max range for {hits6}", delta=delta)

    def test_TART_21_hits_to_kill_ranges(self):
        """Tests correct range output from calculate_max_range_hits_kill for TAR 21."""
        # Expected ranges
        expected_r1: float = -1         # 1 headshot
        expected_r2: float = -1         # 1 torso + 1 limb
        expected_r3: float = -1         # 3 limb
        expected_r4: float = -1         # 3 torso
        expected_r5: float = -1         # 1 head + 1 torso

        expected_r6: float = 89.730     # 1 head + 2 torso
        expected_r7: float = 74.286     # 1 head + 2 limb
        expected_r8: float = 121.905    # 2 limb + 2 torso
        expected_r9: float = 82.222     # 1 head + 1 torso + 1 limb
        expected_r10: float = 116.098   # 2 head + 1 toso

        expected_r11: float = float('inf')  # 2 head + 1 torso + 1 limb
        expected_r12: float = float('inf')  # 2 head + 2 limb
        expected_r13: float = float('inf')  # 2 head + 2 torso
        expected_r14: float = 137.778   # 3 head
        expected_r15: float = float('inf')  # 3 head + 1 limb

        expected_r16: float = 132.727   # 4 torso
        expected_r17: float = 110       # 4 limb
        expected_r18: float = float('inf')  # 1 head + 4 limb
        expected_r19: float = 137.778   # 1 head + 3 limb
        expected_r20: float = float('inf')  # 1 head + 3 torso

        # Hits to kill
        hits1: Hits = (1, 0, 0)
        hits2: Hits = (0, 1, 1)
        hits3: Hits = (0, 0, 3)
        hits4: Hits = (0, 0, 2)
        hits5: Hits = (0, 1, 0)

        hits6: Hits = (1, 2, 0)
        hits7: Hits = (1, 0, 2)
        hits8: Hits = (0, 2, 2)
        hits9: Hits = (1, 1, 1)
        hits10: Hits = (2, 1, 0)

        hits11: Hits = (2, 1, 1)
        hits12: Hits = (2, 0, 2)
        hits13: Hits = (2, 2, 0)
        hits14: Hits = (3, 0, 0)
        hits15: Hits = (3, 0, 1)

        hits16: Hits = (0, 4, 0)
        hits17: Hits = (0, 0, 4)
        hits18: Hits = (1, 0, 4)
        hits19: Hits = (1, 0, 3)
        hits20: Hits = (1, 3, 0)

        # Actual ranges
        actual_r1: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits1)
        actual_r2: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits2)
        actual_r3: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits3)
        actual_r4: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits4)
        actual_r5: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits5)

        actual_r6: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits6)
        actual_r7: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits7)
        actual_r8: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits8)
        actual_r9: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits9)
        actual_r10: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits10)

        actual_r11: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits11)
        actual_r12: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits12)
        actual_r13: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits13)
        actual_r14: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits14)
        actual_r15: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits15)

        actual_r16: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits16)
        actual_r17: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits17)
        actual_r18: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits18)
        actual_r19: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits19)
        actual_r20: float = self.TAR_21_DmgCalc.calculate_max_range_hits_kill(hits20)

        # Tests
        delta: float = 0.001
        self.assertAlmostEqual(expected_r1, actual_r1, msg=f"Didn't calculate correct max range for {hits1}", delta=delta)
        self.assertAlmostEqual(expected_r2, actual_r2, msg=f"Didn't calculate correct max range for {hits2}", delta=delta)
        self.assertAlmostEqual(expected_r3, actual_r3, msg=f"Didn't calculate correct max range for {hits3}", delta=delta)
        self.assertAlmostEqual(expected_r4, actual_r4, msg=f"Didn't calculate correct max range for {hits4}", delta=delta)
        self.assertAlmostEqual(expected_r5, actual_r5, msg=f"Didn't calculate correct max range for {hits5}", delta=delta)

        self.assertAlmostEqual(expected_r6, actual_r6, msg=f"Didn't calculate correct max range for {hits6}", delta=delta)
        self.assertAlmostEqual(expected_r7, actual_r7, msg=f"Didn't calculate correct max range for {hits7}", delta=delta)
        self.assertAlmostEqual(expected_r8, actual_r8, msg=f"Didn't calculate correct max range for {hits8}", delta=delta)
        self.assertAlmostEqual(expected_r9, actual_r9, msg=f"Didn't calculate correct max range for {hits9}", delta=delta)
        self.assertAlmostEqual(expected_r10, actual_r10, msg=f"Didn't calculate correct max range for {hits10}", delta=delta)

        self.assertAlmostEqual(expected_r11, actual_r11, msg=f"Didn't calculate correct max range for {hits11}", delta=delta)
        self.assertAlmostEqual(expected_r12, actual_r12, msg=f"Didn't calculate correct max range for {hits12}", delta=delta)
        self.assertAlmostEqual(expected_r13, actual_r13, msg=f"Didn't calculate correct max range for {hits13}", delta=delta)
        self.assertAlmostEqual(expected_r14, actual_r14, msg=f"Didn't calculate correct max range for {hits14}", delta=delta)
        self.assertAlmostEqual(expected_r15, actual_r15, msg=f"Didn't calculate correct max range for {hits15}", delta=delta)

        self.assertAlmostEqual(expected_r16, actual_r16, msg=f"Didn't calculate correct max range for {hits16}", delta=delta)
        self.assertAlmostEqual(expected_r17, actual_r17, msg=f"Didn't calculate correct max range for {hits17}", delta=delta)
        self.assertAlmostEqual(expected_r18, actual_r18, msg=f"Didn't calculate correct max range for {hits18}", delta=delta)
        self.assertAlmostEqual(expected_r19, actual_r19, msg=f"Didn't calculate correct max range for {hits19}", delta=delta)
        self.assertAlmostEqual(expected_r20, actual_r20, msg=f"Didn't calculate correct max range for {hits20}", delta=delta)

    def test_GYROJECT_MK_1_hits_to_kill_ranges(self):
        """Tests correct range output from calculate_max_range_hits_kill for Gyrojet Mk 1."""
        # Expected ranges
        expected_r1: float = float('inf')   # 1 headshot
        expected_r2: float = float('inf')   # 1 torso + 1 limb
        expected_r3: float = float('inf')   # 3 limb
        expected_r4: float = -1         # 2 limb
        expected_r5: float = 171.944    # 1 torso
        expected_r6: float = -1         # 1 limb

        # Hits to kill
        hits1: Hits = (1, 0, 0)
        hits2: Hits = (0, 1, 1)
        hits3: Hits = (0, 0, 3)
        hits4: Hits = (0, 0, 2)
        hits5: Hits = (0, 1, 0)
        hits6: Hits = (0, 0, 1)

        # Actual ranges
        actual_r1: float = self.GYROJET_MK_1_DmgCalc.calculate_max_range_hits_kill(hits1)
        actual_r2: float = self.GYROJET_MK_1_DmgCalc.calculate_max_range_hits_kill(hits2)
        actual_r3: float = self.GYROJET_MK_1_DmgCalc.calculate_max_range_hits_kill(hits3)
        actual_r4: float = self.GYROJET_MK_1_DmgCalc.calculate_max_range_hits_kill(hits4)
        actual_r5: float = self.GYROJET_MK_1_DmgCalc.calculate_max_range_hits_kill(hits5)
        actual_r6: float = self.GYROJET_MK_1_DmgCalc.calculate_max_range_hits_kill(hits6)

        # Tests
        delta: float = 0.001
        self.assertAlmostEqual(expected_r1, actual_r1, msg=f"Didn't calculate correct max range for {hits1}", delta=delta)
        self.assertAlmostEqual(expected_r2, actual_r2, msg=f"Didn't calculate correct max range for {hits2}", delta=delta)
        self.assertAlmostEqual(expected_r3, actual_r3, msg=f"Didn't calculate correct max range for {hits3}", delta=delta)
        self.assertAlmostEqual(expected_r4, actual_r4, msg=f"Didn't calculate correct max range for {hits4}", delta=delta)
        self.assertAlmostEqual(expected_r5, actual_r5, msg=f"Didn't calculate correct max range for {hits5}", delta=delta)
        self.assertAlmostEqual(expected_r6, actual_r6, msg=f"Didn't calculate correct max range for {hits6}", delta=delta)
        
if __name__ == '__main__':
    unittest.main()
