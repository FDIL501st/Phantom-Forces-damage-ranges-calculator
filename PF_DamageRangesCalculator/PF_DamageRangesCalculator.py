import sys
import typing
#sys.path.append(".\PF_Packages")

import PF_Packages.damage_info.GunDamageInfo

GunDmgInfo: typing.TypeAlias = PF_Packages.damage_info.GunDamageInfo.GunDamageInfo

def main():
    for search_path in sys.path:
        print(search_path)

    gun_dmg_inf: GunDmgInfo = GunDmgInfo(29, 19, 40, 170, 1, 1.4)

    print(gun_dmg_inf.reverse_damage_drop)

    

if __name__ == "__main__":
    main()

