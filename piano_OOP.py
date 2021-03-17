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
            self.window.grid(row=0, column=0, columnspan=4, padx=20, pady=12, ipadx=800, ipady=50)

            # set default digit zero in the window
            self.window.insert(0, "Welcome")


    class Functionality(Window):
        pass

    class Interface(Functionality):

        def __init__(self):
            super().__init__()
            # --------- THE INTERFACE ------------
            # BUTTONS
            # white notes
            button_do = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_do.grid(row=1, column=0)  # x = 42, y = 175

            button_re = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_re.place(x=42, y=175)

            button_mi = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_mi.place(x=109, y=175)

            button_fa = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_fa.place(x=176, y=175)

            button_sol = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_sol.place(x=243, y=175)

            button_la = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_la.place(x=310, y=175)

            button_si = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(1))
            button_si.place(x=377, y=175)

            # black notes
            button_do_diez = Button(self.root, padx=14, pady=60, bg="black", command=lambda: self.button_click(1))
            button_do_diez.place(x=85, y=175)

            button_re_diez = Button(self.root, padx=14, pady=60, bg="black", command=lambda: self.button_click(1))
            button_re_diez.place(x=152, y=175)

        def button_click(self, number):
            pass

    class Manage(Interface):
        def __init__(self):
            super().__init__()
            self.root.mainloop()


if __name__ == "__main__":
    start = StandardCalculator()
    start.Manage()