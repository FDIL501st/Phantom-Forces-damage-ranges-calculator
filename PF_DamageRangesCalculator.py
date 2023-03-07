from typing import TypeAlias

import src.PF_Packages.GUI.main_window

GUI: TypeAlias = src.PF_Packages.GUI.main_window.GUI


def main():
    gui: GUI = GUI()
    gui.mainloop()


if __name__ == "__main__":
    main()
