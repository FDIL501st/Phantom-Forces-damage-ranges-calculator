import unittest
from typing import TypeAlias
from PF_Packages.damage_info.GunDamageInfo import GunDamageInfo
from PF_Packages.dataTypes import HitsToKill

GunDmgInfo: TypeAlias = GunDamageInfo
INF: float = float('inf')


class TestGunCalculateChain(unittest.TestCase):
    """
    Tests the function chain for gun hits to kill calculations.
    Does not test if the functions work,
    only if the chain itself returns expected value.
    """

    def test_gun_calculation_chain_works(self):
        # TRG 42 damage info as of 2022 Dec.31 (2022 Winter Update) in main game
        self.TRG_42: GunDmgInfo = GunDmgInfo(100, 65, 60, 160, 1, 3)
        # calculate the killing ranges
        self.TRG_42.calculate_killing_ranges()

        e_hits_to_kill: HitsToKill = {"1 | 0 | 0": INF, "0 | 0 | 1": 60, "0 | 0 | 2": INF}
        a_hits_to_kill: HitsToKill = self.TRG_42.calculator.hits_to_kill
        self.assertDictEqual(a_hits_to_kill, e_hits_to_kill)


if __name__ == '__main__':
    unittest.main()
