import unittest
from typing import TypeAlias
from PF_Packages.damage_function.GunDamageFunction import GunDamageOverRangeFunction
from PF_Packages.damage_info import GunDamageInfo

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
        e = {"1 | 0 | 0": INF, "0 | 0 | 1": 60, "0 | 0 | 2": INF}

        self.assertDictEqual(a, e)
        # Can also use assertDictContainsSubset, though that doesn't check order, which isn't really important

    def test_GYROJET_MK_1_hits_to_kill(self) -> None:
        """Tests if can calculate all hits to kill of Gyrojet Mk 1."""
        a = self.GYROJET_MK_1_DmgFunc.calculate_all_combinations_hits_to_kill()
        e = {"1 | 0 | 0": INF, "0 | 0 | 3": INF, "0 | 1 | 0": 171.944,
             "0 | 1 | 1": INF, "0 | 2 | 0": INF}

        self.assertDictEqual(e, a)

    def test_TAR_21_hits_to_kill(self) -> None:
        """Tests if can calculate all hits to kill of TAR 21."""
        a = self.TAR_21_DmgFunc.calculate_all_combinations_hits_to_kill()

        # Need to change this
        e = {"1 | 0 | 2": 74.286, "1 | 0 | 3": 137.778, "1 | 0 | 4": INF,
             "1 | 1 | 1": 82.222, "1 | 1 | 2": INF,
             "1 | 2 | 0": 89.73, "1 | 2 | 1": INF,
             "1 | 3 | 0": INF,
             "2 | 0 | 1": 110.0, "2 | 0 | 2": INF,
             "2 | 1 | 0": 116.098, "2 | 1 | 1": INF,
             "2 | 2 | 0": INF,
             "3 | 0 | 0": 137.778, "3 | 0 | 1": INF,
             "3 | 1 | 0": INF,
             "4 | 0 | 0": INF,
             "0 | 1 | 3": 116.098, "0 | 1 | 4": INF,
             "0 | 2 | 2": 121.905, "0 | 2 | 3": INF,
             "0 | 3 | 1": 127.442, "0 | 3 | 2": INF,
             "0 | 4 | 0": 132.727, "0 | 4 | 1": INF,
             "0 | 5 | 0": INF,
             "0 | 0 | 4": 110, "0 | 0 | 5": INF}

        self.assertDictEqual(e, a)


if __name__ == '__main__':
    unittest.main()
