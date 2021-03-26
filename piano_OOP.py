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

            self.style_name = "piano_"

            # WINDOWS

            self.window = Entry(self.root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=self.fontStyle)
            self.window.grid(row=0, column=0, columnspan=4, padx=20, pady=12, ipadx=450, ipady=50)

            # set default digit zero in the window
            self.window.insert(0, "Welcome")

    class Functionality(Window):
        def __init__(self):
            super().__init__()
            self.dir = os.path.dirname(__file__)

        def button_click(self, note):
            self.window.delete(0, END)
            self.window.insert(0, note.split('_')[0])
            pygame.init()
            rel_path = f"sounds/{note}.mp3"
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
                super().__init__()
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
            buttons = Button(self.root, pady=110)  # , padx=29, pady=110
            buttons.grid(row=1, column=0)

            button_do_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(f'{self.style_name}C_3'))
            button_do_oct1.place(x=42, y=175)
            button_re_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click(f'{self.style_name}D_3'))
            button_re_oct1.place(x=109, y=175)
            button_mi_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('E_3'))
            button_mi_oct1.place(x=176, y=175)
            button_fa_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('F_3'))
            button_fa_oct1.place(x=243, y=175)
            button_sol_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('G_3'))
            button_sol_oct1.place(x=310, y=175)
            button_la_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('A_3'))
            button_la_oct1.place(x=377, y=175)
            button_si_oct1 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('B_3'))
            button_si_oct1.place(x=444, y=175)
            button_do_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('C_4'))
            button_do_oct2.place(x=511, y=175)
            button_re_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('D_4'))
            button_re_oct2.place(x=578, y=175)
            button_mi_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('E_4'))
            button_mi_oct2.place(x=645, y=175)
            button_fa_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('F_4'))
            button_fa_oct2.place(x=712, y=175)
            button_sol_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('G_4'))
            button_sol_oct2.place(x=779, y=175)
            button_la_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('A_4'))
            button_la_oct2.place(x=846, y=175)
            button_si_oct2 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('B_4'))
            button_si_oct2.place(x=913, y=175)
            button_do_oct3 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('C_5'))
            button_do_oct3.place(x=980, y=175)
            button_re_oct3 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('D_5'))
            button_re_oct3.place(x=1047, y=175)
            button_mi_oct3 = Button(self.root, padx=29, pady=110, bg="white", command=lambda: self.button_click('E_5'))
            button_mi_oct3.place(x=1114, y=175)

            # black notes
            button_do_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('C#_3'))
            button_do_diez_oct1.place(x=85, y=175)
            button_re_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('D#_3'))
            button_re_diez_oct1.place(x=152, y=175)
            button_fa_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('F#_3'))
            button_fa_diez_oct1.place(x=286, y=175)
            button_sol_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                          command=lambda: self.button_click('G#_3'))
            button_sol_diez_oct1.place(x=353, y=175)
            button_la_diez_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('A#_3'))
            button_la_diez_oct1.place(x=420, y=175)
            button_do_diez_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('C#_4'))
            button_do_diez_oct2.place(x=554, y=175)
            button_re_diez_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('D#_4'))
            button_re_diez_oct2.place(x=621, y=175)
            button_fa_diez_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('F#_4'))
            button_fa_diez_oct2.place(x=755, y=175)
            button_sol_diez_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                          command=lambda: self.button_click('G#_4'))
            button_sol_diez_oct2.place(x=822, y=175)
            button_la_diez_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('A#_4'))
            button_la_diez_oct2.place(x=889, y=175)
            button_do_diez_oct3 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('C#_54'))
            button_do_diez_oct3.place(x=1023, y=175)
            button_re_diez_oct3 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click('D#_5'))
            button_re_diez_oct3.place(x=1090, y=175)

            self.root.bind('a', lambda event, parameter='C_3': self.press(parameter))
            self.root.bind('w', lambda event, parameter='C#_3': self.press(parameter))
            self.root.bind('s', lambda event, parameter='D_3': self.press(parameter))
            self.root.bind('e', lambda event, parameter='D#_3': self.press(parameter))
            self.root.bind('d', lambda event, parameter='E_3': self.press(parameter))
            self.root.bind('f', lambda event, parameter='F_3': self.press(parameter))
            self.root.bind('t', lambda event, parameter='F#_3': self.press(parameter))
            self.root.bind('g', lambda event, parameter='G_3': self.press(parameter))
            self.root.bind('y', lambda event, parameter='G#_3': self.press(parameter))
            self.root.bind('h', lambda event, parameter='A_3': self.press(parameter))
            self.root.bind('u', lambda event, parameter='A#_3': self.press(parameter))
            self.root.bind('j', lambda event, parameter='B_3': self.press(parameter))
            self.root.bind('A', lambda event, parameter='C_4': self.press(parameter))
            self.root.bind('B', lambda event, parameter='C#_4': self.press(parameter))
            self.root.bind('S', lambda event, parameter='D_4': self.press(parameter))
            self.root.bind('R', lambda event, parameter='D#_4': self.press(parameter))
            self.root.bind('D', lambda event, parameter='E_4': self.press(parameter))
            self.root.bind('F', lambda event, parameter='F_4': self.press(parameter))
            self.root.bind('T', lambda event, parameter='F#_4': self.press(parameter))
            self.root.bind('G', lambda event, parameter='G_4': self.press(parameter))
            self.root.bind('Y', lambda event, parameter='G#_4': self.press(parameter))
            self.root.bind('H', lambda event, parameter='A_4': self.press(parameter))
            self.root.bind('U', lambda event, parameter='A#_4': self.press(parameter))
            self.root.bind('J', lambda event, parameter='B_4': self.press(parameter))

            buttons_dict = {
                button_do_oct1: "#c92216", button_re_oct1: "#ff991c", button_mi_oct1: "#fff705",
                button_fa_oct1: "#7aff05", button_sol_oct1: "#056dff", button_la_oct1: "#5c05ff",
                button_si_oct1: "#8205ff", button_do_oct2: "#c92216", button_re_oct2: "#ff991c",
                button_mi_oct2: "#fff705", button_fa_oct2: "#7aff05", button_sol_oct2: "#056dff",
                button_la_oct2: "#5c05ff", button_si_oct2: "#8205ff", button_do_oct3: "#c92216",
                button_re_oct3: "#ff991c", button_mi_oct3: "#fff705"
            }
            notes_voices = {
                button_do_oct1: 'C_3', button_re_oct1: 'D_3',
                button_mi_oct1: 'E_3', button_fa_oct1: 'F_3',
                button_sol_oct1: 'G_3', button_la_oct1: 'A_3',
                button_si_oct1: 'B_3', button_do_oct2: 'C_4',
                button_re_oct2: 'D_4', button_mi_oct2: 'E_4',
                button_fa_oct2: 'F_4', button_sol_oct2: 'G_4',
                button_la_oct2: 'A_4', button_si_oct2: 'B_4',
                button_do_oct3: 'C_5', button_re_oct3: 'D_5',
                button_mi_oct3: 'E_5'
            }
            text_info = "Select a piano color-style"

            self.RadioButton(self.window, text_info, buttons_dict, intro="Standard")
            self.Voices(self.window, notes_voices, self.window, self.dir)

        class Voices:
            def __init__(self, choicewin, notes_voices_dict, window, dir):
                super().__init__()
                self.choicewin = choicewin
                self.voices = notes_voices_dict
                self.window = window
                self.dir = dir
                self.helv36 = tk_font.Font(family='Helvetica', size=10, weight=tk_font.BOLD)
                self.option_list = [
                    "Piano",
                    "Syntesizer"
                ]
                self.variable = StringVar(self.choicewin)
                self.variable.set(self.option_list[0])
                self.opt = OptionMenu(self.choicewin, self.variable, *self.option_list)
                self.opt.config(width=10, font=self.helv36)
                self.opt.place(x=200, y=30)
                self.labelTest = Label(text="Select a voice", font=self.helv36, fg='red')
                self.labelTest.place(x=220, y=12)
                self.variable.trace("w", self.callback)

            def callback(self, *args):
                print(self.variable.get())
                if self.variable.get() == "Piano":
                    self.style_name = "piano_"
                else:
                    self.style_name = "syntesizer_"
                self.labelTest.configure(text="The selected voice is {}".format(self.variable.get()))
                print(self.voices)
                self.change_voice(self.style_name, self.voices)

            def change_voice(self, name, voices):
                super().__init__()
                if name == "piano_":
                    for k, v in voices.items():
                        k.configure(command=lambda: self.button_click(f'{name}{v}'))
                        print(f"Concatened: f'{name}{v}'")
                elif name == "syntesizer_":
                    for k, v in voices.items():
                        k.configure(command=lambda: self.button_click(f'{name}{v}'))
                        print(f"Concatened: f'{name}{v}'")
                self.window.delete(0, END)
                self.window.insert(0, name.split('_')[0])
            def button_click(self, note):
                self.window.delete(0, END)
                self.window.insert(0, note.split('_')[1])
                pygame.init()
                print(f"note is {note}")
                rel_path = f"sounds/{note}.mp3"
                full_path = os.path.join(self.dir, rel_path)
                print(full_path)
                sound = pygame.mixer.Sound(f"{full_path}")
                sound.play()
                return

    class Manage(Interface):
        def __init__(self):
            super().__init__()
            self.root.mainloop()


if __name__ == "__main__":
    start = Piano()
    start.Manage()
