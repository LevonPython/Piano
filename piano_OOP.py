from tkinter import *
import tkinter.font as tk_font
import math


class StandardCalculator:

    class Window:

        def __init__(self):
            self.root = Tk()
            self.root.title("Piano")

            # self.windowSTYLES
            self.fontStyle = tk_font.Font(size=32, family="Courier", weight="bold")
            self.fontStyle2 = tk_font.Font(size=18, family="Courier")

            # WINDOWS

            self.window = Entry(self.root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=self.fontStyle)
            self.window.grid(row=1, column=0, columnspan=4, padx=20, pady=12, ipady=22)

            # set default digit zero in the window
            self.window.delete(0, 0)


    class Functionality(Window):
        pass

    class Interface(Functionality):
        pass

    class Manage(Interface):
        def __init__(self):
            super().__init__()
            self.root.mainloop()


if __name__ == "__main__":
    start = StandardCalculator()
    start.Manage()