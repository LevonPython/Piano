from tkinter import *
import tkinter.font as tk_font
import pygame
import os


class Piano:

    class Window:

        def __init__(self):
            self.root = Tk()
            self.root.title("Piano")

            # self.windowSTYLES
            self.fontStyle = tk_font.Font(size=32, family="Courier", weight="bold")
            self.fontStyle2 = tk_font.Font(size=18, family="Courier")
            self.fontStyle3 = tk_font.Font(size=8, family="Courier")

            # WINDOWS

            self.window = Entry(self.root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=self.fontStyle)
            self.window.grid(row=0, column=0, columnspan=4, padx=20, pady=12, ipadx=200, ipady=50)

            # set default digit zero in the window
            self.window.insert(0, "Welcome")

    class Functionality(Window):
        def __init__(self):
            super().__init__()
            self.dir = os.path.dirname(__file__)
            pass

        def change_color(self):
            pass

        def button_click(self, note):
            self.window.delete(0, END)
            self.window.insert(0, note)
            pygame.init()
            rel_path = f"sounds/piano_{note}_3.mp3"
            full_path = os.path.join(self.dir, rel_path)
            print(full_path)
            sound = pygame.mixer.Sound(f"{full_path}")
            sound.play()
            return

        # KEYBOARD PRESS LOGIC
        def press(self, digit=None):
            return self.button_click(digit)

        class RadioButton:

            def __init__(self, choicewin, text_info, buttons_dict, intro):
                self.helv36 = tk_font.Font(family='Helvetica', size=10, weight=tk_font.BOLD)
                Label(choicewin, text=text_info, font=self.helv36).place(x=0)
                self.var = StringVar()
                self.var.set(intro)
                self.choicewin = choicewin
                self.v0 = IntVar()
                self.v0.set(1)
                self.r1 = Radiobutton(choicewin, text="Standard", variable=self.v0, value=1,
                                      command=lambda: self.buttonfn(buttons_dict))
                self.r2 = Radiobutton(choicewin, text="Colorfull", variable=self.v0, value=2,
                                      command=lambda: self.buttonfn(buttons_dict))
                self.r1.place(x=10, y=30)
                self.r2.place(x=10, y=60)

            def buttonfn(self, buttons_dict):
                # print(self.v0.get())
                self.color_change(self.v0.get(), buttons_dict)
                return self.v0.get()

            @staticmethod
            def color_change(value, buttons_dict):
                if value == 1:
                    for k in buttons_dict.keys():
                        k.configure(bg="white")
                else:
                    for k, v in buttons_dict.items():
                        k.configure(bg=v)

    class Interface(Functionality):

        def __init__(self):
            super().__init__()

            # --------- THE INTERFACE ------------
            # BUTTONS

            # white notes
            buttons = Button(self.root)  # , padx=29, pady=110
            buttons.grid(row=1, column=0)

            button_do_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('C'))
            button_do_oct1.place(x=42, y=175)
            button_re_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('D'))
            button_re_oct1.place(x=109, y=175)
            button_mi_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('E'))
            button_mi_oct1.place(x=176, y=175)
            button_fa_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('F'))
            button_fa_oct1.place(x=243, y=175)
            button_sol_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('G'))
            button_sol_oct1.place(x=310, y=175)
            button_la_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('A'))
            button_la_oct1.place(x=377, y=175)
            button_si_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('B'))
            button_si_oct1.place(x=444, y=175)

            # black notes
            button_do_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('C#'))
            button_do_diez_oct1.place(x=85, y=175)
            button_re_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('D#'))
            button_re_diez_oct1.place(x=152, y=175)
            button_fa_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('F#'))
            button_fa_diez_oct1.place(x=286, y=175)
            button_sol_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                          command=lambda: self.button_click('G#'))
            button_sol_diez_oct1.place(x=353, y=175)
            button_la_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('A#'))
            button_la_diez_oct1.place(x=420, y=175)
            buttons_dict = {button_do_oct1: "#c92216", button_re_oct1: "#ff991c", button_mi_oct1: "#fff705",
                            button_fa_oct1: "#7aff05", button_sol_oct1: "#056dff", button_la_oct1: "#5c05ff",
                            button_si_oct1: "#8205ff"}
            text_info = "Select a piano color-style"

            self.root.bind('a', lambda event, parameter='C': self.press(parameter))
            self.root.bind('s', lambda event, parameter='D': self.press(parameter))
            self.root.bind('d', lambda event, parameter='E': self.press(parameter))
            self.root.bind('f', lambda event, parameter='F': self.press(parameter))
            self.root.bind('g', lambda event, parameter='G': self.press(parameter))
            self.root.bind('h', lambda event, parameter='A': self.press(parameter))
            self.root.bind('j', lambda event, parameter='B': self.press(parameter))

            self.RadioButton(self.window, text_info, buttons_dict, intro="Standard")

    class Manage(Interface):
        def __init__(self):
            super().__init__()
            self.root.mainloop()


if __name__ == "__main__":
    start = Piano()
    start.Manage()
