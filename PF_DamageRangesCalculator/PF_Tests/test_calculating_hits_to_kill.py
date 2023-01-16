import unittest
from typing import TypeAlias
from PF_Packages.damage_function.GunDamageFunction import GunDamageOverRangeFunction
from PF_Packages.damage_info import GunDamageInfo
from PF_Packages.dataTypes import Hits

GunDmgFunc: TypeAlias = GunDamageOverRangeFunction
GunDmgInfo: TypeAlias = GunDamageInfo.GunDamageInfo
INF: float = float('inf')

class Test_test_calculating_hits_to_kill(unittest.TestCase):
    def setUp(self):
        # Make a GunDamageOverRangeFunction object
        # First need damage_info

        # TRG 42 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.TRG_42: GunDmgInfo = GunDmgInfo(100, 65, 60, 160, 1, 3)
        self.TRG_42_DmgFunc: GunDmgFunc = GunDmgFunc(self.TRG_42)

        # TAR-21 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.TAR_21: GunDmgInfo = GunDmgInfo(29, 22, 70, 140, 1.1, 1.5)
        self.TAR_21_DmgFunc: GunDmgFunc = GunDmgFunc(self.TAR_21)
        
        # GYROJET MK 1 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.GYROJET_MK_1: GunDmgInfo = GunDmgInfo(35, 45, 35, 180, 2.25, 3.5)
        self.GYROJET_MK_1_DmgFunc: GunDmgFunc = GunDmgFunc(self.GYROJET_MK_1)

    def test_A(self):
        self.assertEqual(1, 1)

    def test_TRG_42_hits_to_kill(self) -> None:
        """Tests if can calculate all hits to kill of TRG_42."""
        a = self.TRG_42_DmgFunc.calculate_all_combinations_hits_to_kill()
        e = {"1 headshot": INF, "1 torso/limb shot": 60, "2 torso/limb shots": INF}

        self.assertDictEqual(a, e)
        # Can also use assertDictContainsSubset, though that doesn't check order, which isn't really important

    def test_GYROJET_MK_1_hits_to_kill(self) -> None:
        """Tests if can calculate all htis to kill of Gyrojet Mk 1."""
        a = self.GYROJET_MK_1_DmgFunc.calculate_all_combinations_hits_to_kill()
        e = {"1 headshot": INF, "3 limb shots": INF, "1 torso shot": 171.944, 
            "1 torso shot, 1 limb shot": INF, "2 torso shots": INF}
        
        self.assertDictEqual(e, a)
        
if __name__ == '__main__':
    unittest.main()
