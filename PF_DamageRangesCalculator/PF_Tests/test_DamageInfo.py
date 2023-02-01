import unittest
from typing import TypeAlias

import PF_DamageRangesCalculator.PF_Packages.damage_info.GunDamageInfo

# Having importing troubles, so can't run the test
# ModuleNotFoundError: No module named 'PF_Packages'
# Somehow vs test explorer can still run the tests

GunDmgInfo: TypeAlias = PF_DamageRangesCalculator.PF_Packages.damage_info.GunDamageInfo.GunDamageInfo


class Test_test_DamageInfo(unittest.TestCase):
    def test_GunDamageInfo_setter_getters(self):
        d1: float = 29
        d2: float = 19
        r1: float = 100
        r2: float = 200
        headMulti: float = 1.4
        torsoMulti: float = 1

        test_obj: GunDmgInfo = GunDmgInfo(d1, d2, r1, r2, torsoMulti, headMulti)

        self.assertEqual(test_obj.max_damage, d1, "Constructor didn't assign d1 to max_damage.")
        self.assertEqual(test_obj.min_damage, d2, "Constructor didn't assign d2 to min_damage.")
        self.assertEqual(test_obj.min_range, r1, "Constructor didn't assign r1 to max_damage_range.")
        self.assertEqual(test_obj.max_range, r2, "Constructor didn't assign r2 to min_damage_range.")
        self.assertEqual(test_obj.reverse_damage_drop, False,
                         "Constructor didn't properly see that damage does not have reverse damage.")
        self.assertEqual(test_obj.torso_multi, torsoMulti, "Constructor didn't assign torsoMulti to torso_multi.")
        self.assertEqual(test_obj.head_multi, headMulti, "Constructor didn't assign headMulti to head_multi.")
        self.assertEqual(test_obj.damage_drop, -0.1, "Did not properly calculate the damage drop.")

    # Need to test set calculator
    # calculate_killing_ranges are set in the testing of the subclasses


if __name__ == '__main__':
    unittest.main()
