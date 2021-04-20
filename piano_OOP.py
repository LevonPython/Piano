from tkinter import *
import tkinter.font as tk_font
import pygame
import os

# impolement recording
# implement volume from mouse
# implement turn off/on
# implement new voice stytles
# implement click when pressing

class Piano:

    class Window:

        def __init__(self):
            self.root = Tk()
            self.root.title("Piano")

            # self.windowSTYLES
            self.fontStyle = tk_font.Font(size=32, family="Courier", weight="bold")
            self.fontStyle2 = tk_font.Font(size=18, family="Courier")
            self.fontStyle3 = tk_font.Font(size=8, family="Courier")
            self.feature_font = tk_font.Font(family='Helvetica', size=10, weight=tk_font.BOLD)

            self.style_name = "Piano_"
            self.volume = 0.05

            # WINDOWS

            self.window = Entry(self.root, width=10, borderwidth=0, bg="#f2f2f2", justify='right', font=self.fontStyle)
            self.window.grid(row=0, column=0, columnspan=4, padx=20, pady=12, ipadx=450, ipady=50)

            # set default digit zero in the window
            self.window.insert(0, "Welcome")

    class Functionality(Window):

        def __init__(self):
            super().__init__()
            self.dir = os.path.dirname(__file__)
            self.font_func = tk_font.Font(family='Helvetica', size=10, weight=tk_font.BOLD)
            Label(self.window, text="Volume \ncontroller", font=self.font_func).place(x=5)
            self.vertical = Scale(self.window, from_=100, to=0, troughcolor='white', cursor="arrow", bd=3, width=20,
                                  command=self.volume_controller)
            self.vertical.place(x=1, y=35)

        def volume_controller(self, *args):
            print(self.vertical.get(), self.vertical.get()/100)
            self.volume = self.vertical.get()/100

        def button_click(self, note):
            self.window.delete(0, END)
            self.window.insert(0, "Please select a voice")



        class RadioButton:
            def __init__(self, window, text_info, buttons_dict, feature_font, intro):
                super().__init__()
                self.font_radio_but = feature_font
                Label(window, text=text_info, font=self.font_radio_but).place(x=110)
                self.var = StringVar()
                self.var.set(intro)
                self.window = window
                self.v0 = IntVar()
                self.v0.set(1)
                self.r1 = Radiobutton(self.window, text="Standard", variable=self.v0, value=1,
                                      command=lambda: self.button_fn(buttons_dict))
                self.r2 = Radiobutton(self.window, text="Colorful", variable=self.v0, value=2,
                                      command=lambda: self.button_fn(buttons_dict))
                self.r1.place(x=110, y=40)
                self.r2.place(x=110, y=70)

            def button_fn(self, buttons_dict):
                self.window.delete(0, END)
                if self.v0.get() == 1:
                    self.window.insert(0, "Color: Standard")
                else:
                    self.window.insert(0, "Color: Colorful")
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

        class Voices:

            def __init__(self, notes_voices_dict, window, direction, volume, vertical_vol, feature_font,
                         style_name, root):
                # super().__init__()
                self.style_name = style_name
                self.root = root
                self.root.bind('a', lambda event, parameter=f'{self.style_name}C_3': self.press(parameter))
                self.root.bind('w', lambda event, parameter=f'{self.style_name}C#_3': self.press(parameter))
                self.root.bind('s', lambda event, parameter=f'{self.style_name}D_3': self.press(parameter))
                self.root.bind('e', lambda event, parameter=f'{self.style_name}D#_3': self.press(parameter))
                self.root.bind('d', lambda event, parameter=f'{self.style_name}E_3': self.press(parameter))
                self.root.bind('f', lambda event, parameter=f'{self.style_name}F_3': self.press(parameter))
                self.root.bind('t', lambda event, parameter=f'{self.style_name}F#_3': self.press(parameter))
                self.root.bind('g', lambda event, parameter=f'{self.style_name}G_3': self.press(parameter))
                self.root.bind('y', lambda event, parameter=f'{self.style_name}G#_3': self.press(parameter))
                self.root.bind('h', lambda event, parameter=f'{self.style_name}A_3': self.press(parameter))
                self.root.bind('u', lambda event, parameter=f'{self.style_name}A#_3': self.press(parameter))
                self.root.bind('j', lambda event, parameter=f'{self.style_name}B_3': self.press(parameter))
                self.root.bind('A', lambda event, parameter=f'{self.style_name}C_4': self.press(parameter))
                self.root.bind('B', lambda event, parameter=f'{self.style_name}C#_4': self.press(parameter))
                self.root.bind('S', lambda event, parameter=f'{self.style_name}D_4': self.press(parameter))
                self.root.bind('R', lambda event, parameter=f'{self.style_name}D#_4': self.press(parameter))
                self.root.bind('D', lambda event, parameter=f'{self.style_name}E_4': self.press(parameter))
                self.root.bind('F', lambda event, parameter=f'{self.style_name}F_4': self.press(parameter))
                self.root.bind('T', lambda event, parameter=f'{self.style_name}F#_4': self.press(parameter))
                self.root.bind('G', lambda event, parameter=f'{self.style_name}G_4': self.press(parameter))
                self.root.bind('Y', lambda event, parameter=f'{self.style_name}G#_4': self.press(parameter))
                self.root.bind('H', lambda event, parameter=f'{self.style_name}A_4': self.press(parameter))
                self.root.bind('U', lambda event, parameter=f'{self.style_name}A#_4': self.press(parameter))
                self.root.bind('J', lambda event, parameter=f'{self.style_name}B_4': self.press(parameter))
                self.root.bind('<Up>', lambda event, parameter=f'vol_up': self.press(parameter))
                self.root.bind('<Down>', lambda event, parameter=f'vol_down': self.press(parameter))

                # voice selecting elements
                self.voices = notes_voices_dict
                self.window = window
                self.dir = direction
                self.feature_font = feature_font
                self.option_list = [
                    "Piano",
                    "Synthesizer"
                ]
                self.variable = StringVar(self.window)
                self.variable.set("Not selected")
                self.opt = OptionMenu(self.window, self.variable, *self.option_list)
                self.opt.config(width=10, font=self.feature_font)
                self.opt.place(x=250, y=35)
                self.labelTest = Label(text="Select a voice\n*required", font=self.feature_font, fg='red')
                self.labelTest.place(x=270, y=13)
                self.variable.trace("w", self.callback)
                # volume controller elements
                self.volume = volume
                print(f"self.volume in voices: {self.volume}")
                self.vertical_vol = vertical_vol
                self.vertical_vol.configure(command=self.volume_controller)

            def volume_controller(self, *args):
                print(f"Volume: {self.vertical_vol.get()} {self.vertical_vol.get() / 100}")
                self.volume = self.vertical_vol.get() / 100
                self.window.delete(0, END)
                self.window.insert(0, f"Volume: {self.vertical_vol.get()}")

            def volume_controller2(self, *args):
                print("------")
                print(f"Volume: {args}")
                self.volume = args[0]
                self.window.delete(0, END)
                self.window.insert(0, f"Volume: {self.volume}")

            def callback(self, *args):
                print(self.variable.get())
                if self.variable.get() == "Piano":
                    style_name = "Piano_"
                else:
                    style_name = "Synthesizer_"
                self.labelTest.configure(text="The selected voice is {}".format(self.variable.get()), fg='black')
                print(self.voices)
                self.change_voice(style_name, self.voices)

            def change_voice(self, name, voices):
                super().__init__()
                for k, v in voices.items():
                    self.configure_voices(name, k, v)
                self.window.delete(0, END)
                self.window.insert(0, f"Voice: {name.split('_')[0]}")

            def configure_voices(self, name, key, value):
                key.configure(command=lambda: self.button_click(f'{name}{value}'))

            def button_click(self, note):
                self.window.delete(0, END)
                self.window.insert(0, note.split('_')[1])
                if note  == 'vol_up':
                    self.volume += 0.1
                    print(f"self.volume: {self.volume}")
                    return self.volume_controller2(self.volume)
                elif note == 'vol_down':
                    self.volume -= 0.1
                    print(f"self.volume: {self.volume}")
                    return self.volume_controller2(self.volume)

                pygame.init()
                rel_path = f"sounds/{note}.mp3"
                full_path = os.path.join(self.dir, rel_path)
                print(full_path)
                sound = pygame.mixer.Sound(f"{full_path}")
                sound.set_volume(self.volume)
                sound.play()
                print(f"Voice.volume is: {self.volume}")
                return

            # KEYBOARD PRESS LOGIC
            def press(self, digit=None):
                if self.variable.get() == "Not selected":
                    self.window.delete(0, END)
                    self.window.insert(0, "Please select a voice")
                    return
                note_name = '_'.join(digit.split('_')[1:])
                print(f"note_name is {note_name}")
                for k, v in self.voices.items():
                    if v == note_name:
                        self.change_on_hover(k, "#e6e9eb", k.cget('bg'))
                return self.button_click(digit)

            def change_on_hover(self, button, on_hover, on_leave):
                # background on entering widget
                button.config(background=on_hover)
                self.root.after(100, lambda: button.config(background=on_leave))

        class Switch:

            def __init__(self, root):
                self.root = root
                self.on_off = Button(self.root, text="ON / OFF", command=self.switch_button_state())
                self.on_off.place(x=10, y=10)


            def switch_button_state(self):
                # if (self.on_off['state'] == NORMAL):
                #     # button1['state'] = tk.DISABLED
                #     print("IS NORMAL")
                #     pass
                # else:
                #     # button1['state'] = tk.NORMAL
                #     pass
                pass



    class Interface(Functionality):

        def __init__(self):
            super().__init__()

            # --------- THE INTERFACE ------------
            # BUTTONS


            # white notes
            buttons = Button(self.root, pady=110)
            buttons.grid(row=1, column=0)

            button_do_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}C_3'))
            button_do_oct1.place(x=42, y=175)
            button_re_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}D_3'))
            button_re_oct1.place(x=109, y=175)
            button_mi_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}E_3'))
            button_mi_oct1.place(x=176, y=175)
            button_fa_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}F_3'))
            button_fa_oct1.place(x=243, y=175)
            button_sol_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                     command=lambda: self.button_click(f'{self.style_name}G_3'))
            button_sol_oct1.place(x=310, y=175)
            button_la_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}A_3'))
            button_la_oct1.place(x=377, y=175)
            button_si_oct1 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}B_3'))
            button_si_oct1.place(x=444, y=175)
            button_do_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}C_4'))
            button_do_oct2.place(x=511, y=175)
            button_re_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}D_4'))
            button_re_oct2.place(x=578, y=175)
            button_mi_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}E_4'))
            button_mi_oct2.place(x=645, y=175)
            button_fa_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}F_4'))
            button_fa_oct2.place(x=712, y=175)
            button_sol_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                     command=lambda: self.button_click(f'{self.style_name}G_4'))
            button_sol_oct2.place(x=779, y=175)
            button_la_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}A_4'))
            button_la_oct2.place(x=846, y=175)
            button_si_oct2 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}B_4'))
            button_si_oct2.place(x=913, y=175)
            button_do_oct3 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}C_5'))
            button_do_oct3.place(x=980, y=175)
            button_re_oct3 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}D_5'))
            button_re_oct3.place(x=1047, y=175)
            button_mi_oct3 = Button(self.root, padx=29, pady=110, bg="white",
                                    command=lambda: self.button_click(f'{self.style_name}E_5'))
            button_mi_oct3.place(x=1114, y=175)

            # black notes
            button_do_dies_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}C#_3'))
            button_do_dies_oct1.place(x=85, y=175)
            button_re_dies_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}D#_3'))
            button_re_dies_oct1.place(x=152, y=175)
            button_fa_dies_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}F#_3'))
            button_fa_dies_oct1.place(x=286, y=175)
            button_sol_dies_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                          command=lambda: self.button_click(f'{self.style_name}G#_3'))
            button_sol_dies_oct1.place(x=353, y=175)
            button_la_dies_oct1 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}A#_3'))
            button_la_dies_oct1.place(x=420, y=175)
            button_do_dies_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}C#_4'))
            button_do_dies_oct2.place(x=554, y=175)
            button_re_dies_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}D#_4'))
            button_re_dies_oct2.place(x=621, y=175)
            button_fa_dies_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}F#_4'))
            button_fa_dies_oct2.place(x=755, y=175)
            button_sol_dies_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                          command=lambda: self.button_click(f'{self.style_name}G#_4'))
            button_sol_dies_oct2.place(x=822, y=175)
            button_la_dies_oct2 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}A#_4'))
            button_la_dies_oct2.place(x=889, y=175)
            button_do_dies_oct3 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}C#_54'))
            button_do_dies_oct3.place(x=1023, y=175)
            button_re_dies_oct3 = Button(self.root, padx=14, pady=60, bg="black",
                                         command=lambda: self.button_click(f'{self.style_name}D#_5'))
            button_re_dies_oct3.place(x=1090, y=175)

            buttons_dict = {
                button_do_oct1: "#c92216", button_re_oct1: "#ff991c", button_mi_oct1: "#fff705",
                button_fa_oct1: "#7aff05", button_sol_oct1: "#056dff", button_la_oct1: "#5c05ff",
                button_si_oct1: "#8205ff", button_do_oct2: "#c92216", button_re_oct2: "#ff991c",
                button_mi_oct2: "#fff705", button_fa_oct2: "#7aff05", button_sol_oct2: "#056dff",
                button_la_oct2: "#5c05ff", button_si_oct2: "#8205ff", button_do_oct3: "#c92216",
                button_re_oct3: "#ff991c", button_mi_oct3: "#fff705"
            }
            notes_voices = {
                button_do_oct1: 'C_3', button_re_oct1: 'D_3', button_mi_oct1: 'E_3', button_fa_oct1: 'F_3',
                button_sol_oct1: 'G_3', button_la_oct1: 'A_3', button_si_oct1: 'B_3', button_do_oct2: 'C_4',
                button_re_oct2: 'D_4', button_mi_oct2: 'E_4', button_fa_oct2: 'F_4', button_sol_oct2: 'G_4',
                button_la_oct2: 'A_4', button_si_oct2: 'B_4', button_do_oct3: 'C_5', button_re_oct3: 'D_5',
                button_mi_oct3: 'E_5', button_do_dies_oct1: 'C#_3', button_re_dies_oct1: 'D#_3',
                button_fa_dies_oct1: 'F#_3', button_sol_dies_oct1: 'G#_3', button_la_dies_oct1: 'A#_3',
                button_do_dies_oct2: 'C#_4', button_re_dies_oct2: 'D#_4', button_fa_dies_oct2: 'F#_4',
                button_sol_dies_oct2: 'G#_4', button_la_dies_oct2: 'A#_4', button_do_dies_oct3: 'C#_5',
                button_re_dies_oct3: 'D#_5'
            }
            text_info = "Select a piano \ncolor-style"

            self.RadioButton(self.window, text_info, buttons_dict, self.feature_font, intro="Standard")
            self.Voices(notes_voices, self.window, self.dir, self.volume, self.vertical, self.feature_font,
                        self.style_name, self.root)
            self.Switch(self.root)


    class Manage(Interface):
        def __init__(self):
            super().__init__()
            self.root.mainloop()


if __name__ == "__main__":
    start = Piano()
    start.Manage()
