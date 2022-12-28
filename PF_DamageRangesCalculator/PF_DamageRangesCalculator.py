import sys
import typing
#sys.path.append(".\PF_Packages")

import PF_Packages.damage_info.GunDamageInfo
import PF_Packages.damage_calculator.GunDamageCalculator

GunDmgInfo: typing.TypeAlias = PF_Packages.damage_info.GunDamageInfo.GunDamageInfo
GunDmgCalc: typing.TypeAlias = PF_Packages.damage_calculator.GunDamageCalculator.GunDamageCalculator

def main():
    for search_path in sys.path:
        print(search_path)

    gun_dmg_inf: GunDmgInfo = GunDmgInfo(29, 19, 40, 170, 1, 1.5)

    print(gun_dmg_inf.reverse_damage_drop)

    gun_dmg_calc: GunDmgCalc = GunDmgCalc(gun_dmg_inf)

    print(gun_dmg_calc.gun_damage_info.head_multi)

    

if __name__ == "__main__":
    main()

