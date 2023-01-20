import sys
import typing
import PF_Packages.damage_info.GunDamageInfo
import PF_Packages.damage_calculator.GunDamageCalculator
import PF_Packages.damage_function.GunDamageFunction
import PF_Packages.damage_info.DamageInfo
import PF_Packages.damage_function.function_calculator.FunctionCalculator
from PF_Packages.parser.HitsToKillParser import HitsToKillParser
import PF_Packages.GUI.main_window

GunDmgInfo: typing.TypeAlias = PF_Packages.damage_info.GunDamageInfo.GunDamageInfo
GunDmgCalc: typing.TypeAlias = PF_Packages.damage_calculator.GunDamageCalculator.GunDamageCalculator
DmgInfo: typing.TypeAlias = PF_Packages.damage_info.DamageInfo.DamageInfo
DmgFuncCalc: typing.TypeAlias = PF_Packages.damage_function.function_calculator.FunctionCalculator.DamageFunctionCalculator
GunDmgFunc: typing.TypeAlias = PF_Packages.damage_function.GunDamageFunction.GunDamageOverRangeFunction
GUI: typing.TypeAlias = PF_Packages.GUI.main_window.GUI 

def main():
    for search_path in sys.path:
        print(search_path)

    gun_dmg_inf: GunDmgInfo = GunDmgInfo(29, 19, 40, 170, 1, 1.5)

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

    print(func_calc.calculate_max_range_hits_kill((1, 0, 0)))
    print(func_calc.calculate_max_range_hits_kill((0, 0, 2)))
    
    hits = (0, 0, 1)
    parsed: str = HitsToKillParser.convert_tuple_to_str(hits)
    print(parsed)

    hits = (0, 0, 4)
    parsed: str = HitsToKillParser.convert_tuple_to_str(hits, True)
    print(parsed)

    gun_dmg_func: GunDmgFunc = GunDmgFunc(gun_dmg_inf)

    print()
    for hits, range in gun_dmg_func.calculate_all_combinations_hits_to_kill().items():
        print("{0} : {1}".format(hits, range))

if __name__ == "__main__":
    main()

