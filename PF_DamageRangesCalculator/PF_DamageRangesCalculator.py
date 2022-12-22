import sys

sys.path.append(".\PF_Packages\\")

import PF_Packages.damage_calculator.GunDamageCalculator as GunDmgCalc


def main():
    for search_path in sys.path:
        print(search_path)

    gun_dmg_calc = GunDmgCalc.GunDamageCalculator()
    
    print(gun_dmg_calc.__module__)

    

if __name__ == "__main__":
    main()

