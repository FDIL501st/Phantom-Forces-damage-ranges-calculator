import unittest
import sys
sys.path.append('C:/Users/fdilf\Desktop/Phantom-Forces-damage-ranges-calculator/PF_DamageRangesCalculator/PF_Packages/')

import PF_Packages.damage_info.GunDamageInfo
# Having importing troubles, so can't run the test
# ModuleNotFoundError: No module named 'PF_Packages'

GunDmgInfo = PF_Packages.damage_info.GunDamageInfo.GunDmgInfo

class Test_test_DamageInfo(unittest.TestCase):
    def test_GunDamageInfo_setter_getters(self):
        d1: float = 29
        d2: float = 19
        r1: float = 100
        r2: float = 200
        headMulti: float = 1.4
        torsoMulti: float = 1

        test_obj: GunDmgInfo = GunDmgInfo(d1,d2, r1, r2, torsoMulti, headMulti)

        self.assertEqual(test_obj.max_damage, d1, "Constructor didn't assign d1 to max_damage.")



if __name__ == '__main__':
    for p in sys.path:
        print(p)
    unittest.main()
