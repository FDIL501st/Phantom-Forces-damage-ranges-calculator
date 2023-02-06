import typing

import PF_DamageRangesCalculator.PF_Packages.GUI.main_window

TypeAlias = typing.TypeAlias
GUI: TypeAlias = PF_DamageRangesCalculator.PF_Packages.GUI.main_window.GUI


def main():
    gui: GUI = GUI()
    gui.mainloop()


if __name__ == "__main__":
    main()
