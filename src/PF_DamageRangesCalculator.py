from typing import TypeAlias

import PF_Packages.GUI.main_window
import PF_Packages.dict_sorter.HitsToKill_Sorter

GUI: TypeAlias = PF_Packages.GUI.main_window.GUI
HitsToKillSorter: TypeAlias = PF_Packages.dict_sorter.HitsToKill_Sorter.HitsToKillSorter
INF: float = float('inf')


def main():
    gui: GUI = GUI()
    gui.mainloop()


def test():
    hits_to_kill = {"1 headshot, 2 limb shots": 74.286, "1 headshot, 3 limb shots": 137.778,
                    "1 headshot, 4 limb shots": INF,
                    "1 headshot, 1 torso shot, 1 limb shot": 82.222, "1 headshot, 1 torso shot, 2 limb shots": INF,
                    "1 headshot, 2 torso shots": 89.73, "1 headshot, 2 torso shots, 1 limb shot": INF,
                    "1 headshot, 3 torso shots": INF, "2 headshots, 1 limb shot": 110.0,
                    "2 headshots, 2 limb shots": INF,
                    "2 headshots, 1 torso shot": 116.098, "2 headshots, 1 torso shot, 1 limb shot": INF,
                    "2 headshots, 2 torso shots": INF, "3 headshots": 137.778, "3 headshots, 1 limb shot": INF,
                    "3 headshots, 1 torso shot": INF, "4 headshots": INF,
                    "1 torso shot, 3 limb shots": 116.098, "1 torso shot, 4 limb shots": INF,
                    "2 torso shots, 2 limb shots": 121.905, "2 torso shots, 3 limb shots": INF,
                    "3 torso shots, 1 limb shot": 127.442, "3 torso shots, 2 limb shots": INF,
                    "4 torso shots": 132.727, "4 torso shots, 1 limb shot": INF, "5 torso shots": INF,
                    "4 limb shots": 110, "5 limb shots": INF}

    hits_to_kill_sorted: HitsToKillSorter = HitsToKillSorter(hits_to_kill)

    for kill in hits_to_kill_sorted:
        print(kill)
    # iterator works as intended
    # inserts work as intended
    # constructor also works as intended(though it is just an insert chain)


if __name__ == "__main__":
    test()
    # main()
