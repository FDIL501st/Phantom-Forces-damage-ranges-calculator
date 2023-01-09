import sys
import typing
#sys.path.append(".\PF_Packages")

import PF_Packages.damage_info.GunDamageInfo
import PF_Packages.damage_calculator.GunDamageCalculator
import PF_Packages.damage_function.function_calculator.FunctionCalculator

GunDmgInfo: typing.TypeAlias = PF_Packages.damage_info.GunDamageInfo.GunDamageInfo
GunDmgCalc: typing.TypeAlias = PF_Packages.damage_calculator.GunDamageCalculator.GunDamageCalculator
DmgInfo: typing.TypeAlias = PF_Packages.damage_info.DamageInfo.DamageInfo
DmgFuncCalc: typing.TypeAlias = PF_Packages.damage_function.function_calculator.FunctionCalculator.DamageFunctionCalculator

def main():
    for search_path in sys.path:
        print(search_path)

    gun_dmg_inf: GunDmgInfo = GunDmgInfo(29, 19, 100, 200, 1, 1.5)

    print(gun_dmg_inf.reverse_damage_drop)

    gun_dmg_calc: GunDmgCalc = GunDmgCalc(gun_dmg_inf)

    print(gun_dmg_calc.gun_damage_info.head_multi)
    print(gun_dmg_calc.gun_damage_info.max_damage)
    print(gun_dmg_inf.damage_drop)
    print(isinstance(gun_dmg_calc, GunDmgInfo))
    print(isinstance(gun_dmg_inf, GunDmgInfo))
    print(isinstance(gun_dmg_inf, DmgInfo)) # also works here as gun_dmg_inf is an isntance of a subclass
    
    func_calc: DmgFuncCalc = DmgFuncCalc(gun_dmg_inf, 100)
    print(func_calc.calculate_damage_one_hit('head', 50))

if __name__ == "__main__":
    main()

