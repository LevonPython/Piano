import time
from tkinter import *
import tkinter.font as tk_font
import pygame
import os
from PIL import ImageTk, Image
# pip install pillow
import pyaudio
import wave
# pip install pipwin
# pipwin install pyaudio
from datetime import datetime
import threading

# --- TO DO ---
# show window countdown 3,2,1 and voice 0%
# implement background enable changing 0%
# implement input as array to playing a music 0%
# --- DOING ---
# implement new voice stytles 15%
# impelement recording 20%
# --- DONE ---
# implement volume from mouse 100%
# implement turn off/on 100%
# implement click when pressing 100%


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
            self.window.grid(row=0, column=0, columnspan=4, padx=20, pady=15, ipadx=450, ipady=50)

            # set default digit zero in the window
            self.window.insert(0, "Welcome, please turn ON")

    class Functionality(Window):

        def __init__(self):
            super().__init__()
            self.dir = os.path.dirname(__file__)
            self.font_func = tk_font.Font(family='Helvetica', size=10, weight=tk_font.BOLD)

            # volume controller
            Label(self.window, text="Volume \ncontroller", font=self.font_func).place(x=69)
            self.vertical = Scale(self.window, from_=100, to=0, troughcolor='white', cursor="arrow", bd=3, width=20,
                                  activebackground='white', state=DISABLED, command=self.volume_controller)
            self.vertical.place(x=65, y=35)

        def volume_controller(self, *args):
            print(self.vertical.get(), self.vertical.get() / 100)
            self.volume = self.vertical.get() / 100

        def button_click(self, note):
            self.window.delete(0, END)
            self.window.insert(0, "Please select a voice")

        class RadioButton:
            def __init__(self, window, text_info, buttons_dict, feature_font, intro):
                super().__init__()
                self.font_radio_but = feature_font
                Label(window, text=text_info, font=self.font_radio_but).place(x=164)
                self.var = StringVar()
                self.var.set(intro)
                self.window = window
                self.v0 = IntVar()
                self.v0.set(1)
                self.r1 = Radiobutton(self.window, text="Standard", variable=self.v0, value=1, state=DISABLED,
                                      command=lambda: self.button_fn(buttons_dict))
                self.r2 = Radiobutton(self.window, text="Colorful", variable=self.v0, value=2, state=DISABLED,
                                      command=lambda: self.button_fn(buttons_dict))
                self.r1.place(x=164, y=40)
                self.r2.place(x=164, y=70)

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
                         style_name, root, rec_obj):
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
                self.root.bind("<MouseWheel>", self.mouse_wheel_handler)

                # voice selecting elements
                self.voices = notes_voices_dict
                self.window = window
                self.dir = direction
                self.feature_font = feature_font
                self.option_list = [
                    "Piano",
                    "GrandPiano",
                    "ModernPiano",
                    "Synthesizer"
                ]
                self.variable = StringVar(self.window)
                self.variable.set("Not selected")
                self.opt = OptionMenu(self.window, self.variable, *self.option_list)
                self.opt.config(width=10, font=self.feature_font, state=DISABLED)
                self.opt.place(x=304, y=35)
                self.labelTest = Label(text="Select a voice\n*required", font=self.feature_font, fg='red')
                self.labelTest.place(x=324, y=13)
                self.variable.trace("w", self.callback)

                # volume controller elements
                self.volume = volume
                print(f"self.volume in voices: {self.volume}")
                self.vertical_vol = vertical_vol
                self.vertical_vol.configure(command=self.volume_controller)

                self.rec_obj = rec_obj

            def volume_controller(self, *args):
                print("------")
                print(f"Volume: {self.vertical_vol.get()} {self.vertical_vol.get() / 100}")
                self.volume = self.vertical_vol.get() / 100
                self.window.delete(0, END)
                self.window.insert(0, f"Volume: {self.vertical_vol.get()}")

            def volume_controller2(self, *args):
                print("------")
                print(f"Volume2: {args[0]}")
                self.volume = args[0]
                volume = round(self.volume * 100)
                self.vertical_vol.set(volume)
                self.window.delete(0, END)
                self.window.insert(0, f"Volume: {volume}")

            def callback(self, *args):
                print(self.variable.get())
                if self.variable.get() == "Piano":
                    style_name = "Piano_"
                elif self.variable.get() == "GrandPiano":
                    style_name = "Piano2_"
                elif self.variable.get() == "ModernPiano":
                    style_name = "Synthesizer_"
                else:
                    style_name = "Synthesizer2_"
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
                super().__init__()
                # print(f"note::: {note}")
                self.window.delete(0, END)
                self.window.insert(0, note.split('_')[1])
                pygame.init()
                rel_path = f"static/sounds/{note}.mp3"
                full_path = os.path.join(self.dir, rel_path)
                print(full_path)
                sound = pygame.mixer.Sound(f"{full_path}")
                sound.set_volume(self.volume)
                sound.play()
                print(f"Voice.volume is: {self.volume}")
                return

            def button_volume(self, note):
                super().__init__()
                self.window.delete(0, END)
                self.window.insert(0, note.split('_')[1])
                if note == 'vol_up':
                    self.volume += 0.1
                elif note == 'vol_down':
                    self.volume -= 0.1

                # check volume range
                if self.volume > 1.0:
                    self.volume = 1.0
                elif self.volume < 0.0:
                    self.volume = 0
                print(f"self.volume: {self.volume}")
                return self.volume_controller2(self.volume)

            # KEYBOARD PRESS LOGIC
            def press(self, digit=None):
                if self.variable.get() == "Not selected":
                    self.window.delete(0, END)
                    self.window.insert(0, "Please select a voice")
                    return
                note_name = '_'.join(digit.split('_')[1:])
                print(f"note_name is {note_name}")

                # if note is refers to volume
                if note_name in ('up', 'down'):
                    return self.button_volume(digit)
                # else

                for k, v in self.voices.items():
                    # hovers on the note if press
                    if v == note_name:
                        self.change_on_hover(k, "#e6e9eb", k.cget('bg'))
                print(f"digit: {digit}")
                return self.button_click(digit)

            def mouse_wheel_handler(self, event):
                self.volume += self.delta(event)
                # check volume range
                if self.volume > 1.0:
                    self.volume = 1.0
                elif self.volume < 0.0:
                    self.volume = 0
                print(f"self.volume: {self.volume}")
                return self.volume_controller2(self.volume)

            def delta(self, event):
                if event.delta < 0:
                    return -0.1
                return 0.1

            def change_on_hover(self, button, on_hover, on_leave):
                # background on entering widget
                button.config(background=on_hover)
                self.root.after(100, lambda: button.config(background=on_leave))

        class RecorderBlock:
            """
            If you create an application on windows platform, you can use default stereo mixer virtual device to
            record your PC's output.
            - enable stereo mixer
            https://www.howtogeek.com/howto/39532/how-to-enable-stereo-mix-in-windows-7-to-record-audio/
            """

            def __init__(self, root, window, switch_font):
                self.window = window
                self.root = root
                self.switch_font = switch_font

                # Define Our Images

                self.start_rec = ImageTk.PhotoImage(Image.open(r"static\pics\rec_start.png"))
                self.stop_rec = ImageTk.PhotoImage(Image.open(r"static\pics\rec_stop.png"))
                self.stop = ImageTk.PhotoImage(Image.open(r"static\pics\stop2.png"))
                self.start = ImageTk.PhotoImage(Image.open(r"static\pics\play2.png"))
                # self.start_rec = PhotoImage(file=r"static\pics\rec_start.png")
                # self.stop_rec = PhotoImage(file=r"static\pics\off.png")
                self.record_label = Label(self.root, text="Recorder", font=self.switch_font).place(x=8, y=85)
                self.rec_on_off = Button(self.root, image=self.stop_rec, command=lambda: [self.start_recording(), self.recorder()], state=DISABLED)
                self.rec_on_off.place(x=8, y=105)

                self.rec_tab = Button(self.root, image=self.stop, command=self.recorder_stop, state=DISABLED)
                self.rec_tab.place(x=8, y=140)

                self.recording_status = False
                """
                pyaudio gives you more low-level control, it is possible to get and set parameters
                for your input and output devices, and to check your CPU load and input or output latency.
                """
                self.chunk = 1024  # Record in chunks of 1024 samples
                self.sample_format = pyaudio.paInt16  # 16 bits per sample
                self.channels = 2
                self.fs = 44100  # Record at 44100 samples per second
                self.seconds = 1
                self.file_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                self.filename = f"records/record_{self.file_date}.wav"
                print(self.filename)

                self.p = pyaudio.PyAudio()  # Create an interface to PortAudio

                self.stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs,
                                          frames_per_buffer=self.chunk, input=True)
                self.frames = []  # Initialize array to store frames
                self.seconds_count = 0

            def recorder(self):
                self.rec_on_off.configure(image=self.start_rec, relief=SUNKEN)
                self.rec_tab.configure(image=self.stop, state=NORMAL, relief=SUNKEN)
                self.recording_status = True
                print("Record?")
                # self.root.after(1, self.start_recording())
                t = threading.Thread(target=self.start_recording)
                t.start()

            def start_recording(self):
                print("GOT IT", self.rec_on_off['image'])
                while self.rec_on_off['image'] == "pyimage1":
                    print('Recording started')
                    # Store data in chunks for specified time (seconds)
                    for i in range(0, int(self.fs / self.chunk * self.seconds)):
                        data = self.stream.read(self.chunk)
                        self.frames.append(data)
                    # if self.seconds_count > 5:
                    #     break
                    self.seconds_count += 1
                    print(self.seconds_count)

            def recorder_stop(self):
                self.rec_on_off.configure(image=self.stop_rec)
                self.rec_tab.configure(image=self.start, state=DISABLED)
                self.recording_status = False
                print("Stop Recording?")

                # Stop and close the stream
                self.stream.stop_stream()
                self.stream.close()
                # Terminate the PortAudio interface
                self.p.terminate()

                print('Finished recording')

                # Save the recorded data as a WAV file
                wf = wave.open(self.filename, 'wb')
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.p.get_sample_size(self.sample_format))
                wf.setframerate(self.fs)
                wf.writeframes(b''.join(self.frames))
                wf.close()
                print(f"{self.seconds_count} seconds recorded")

        class Switch:

            def __init__(self, root, radio_obj, voice_obj, rec_obj, rec_obj2, vertical, window, notes_voices,
                         black_notes, switch_font):
                """
                This class is written for turning on/off state of all features
                :param root:
                :param radio_obj:
                :param voice_obj:
                :param vertical:
                :param window:
                """
                self.window = window
                self.radio_obj = radio_obj
                self.voice_obj = voice_obj
                self.rec_obj = rec_obj
                self.rec_obj2 = rec_obj2
                self.vertical = vertical
                self.notes_voices = notes_voices
                self.black_notes = black_notes
                self.root = root
                self.switch_font = switch_font
                # Define Our Images
                self.on = PhotoImage(file=r"static\pics\on.png")
                self.off = PhotoImage(file=r"static\pics\off.png")
                self.switch_label = Label(self.root, text="Switch\ncontroller", font=self.switch_font).place(x=8, y=12)
                self.on_off = Button(self.root, image=self.off, command=self.switch_button_state)
                self.on_off.place(x=8, y=50)

                self.start_rec = ImageTk.PhotoImage(Image.open(r"static\pics\rec_start.png"))
                self.stop_rec = ImageTk.PhotoImage(Image.open(r"static\pics\rec_stop.png"))
                self.stop = ImageTk.PhotoImage(Image.open(r"static\pics\stop2.png"))
                self.start = ImageTk.PhotoImage(Image.open(r"static\pics\play2.png"))

            def switch_button_state(self):
                """
                Disable or enable feature buttons' state when the swtich button is off or on
                :return:
                """
                if self.voice_obj.opt['state'] == NORMAL:
                    self.voice_obj.opt['state'] = DISABLED
                    self.vertical.configure(state=DISABLED, takefocus=0, troughcolor='#f2f2f2')
                    self.radio_obj.r1['state'] = DISABLED
                    self.radio_obj.r2['state'] = DISABLED
                    # self.on_off.configure(bg="#d12144", text="IS OFF")
                    self.on_off.configure(image=self.off)
                    self.rec_obj2.configure(image=self.start, state=DISABLED)
                    self.rec_obj.configure(image=self.stop_rec, state=DISABLED)
                    for k, v in self.notes_voices.items():
                        k.configure(bg='#f2f2f2', state=DISABLED)
                    for k, v in self.black_notes.items():
                        k.configure(bg='#d4d4d4', state=DISABLED)

                    self.window.delete(0, END)
                    self.window.insert(0, f"Turned OFF")
                else:
                    self.voice_obj.opt['state'] = NORMAL
                    self.vertical.configure(state=NORMAL, takefocus=0, troughcolor='white')
                    self.radio_obj.r1['state'] = NORMAL
                    self.radio_obj.r2['state'] = NORMAL
                    # self.on_off.configure(bg="#248a41", text="IS ON")
                    self.on_off.configure(image=self.on)
                    self.rec_obj['state'] = NORMAL
                    # self.rec_obj2['state'] = NORMAL
                    self.rec_obj.configure(image=self.stop_rec)
                    for k, v in self.notes_voices.items():
                        k.configure(bg='white', state=NORMAL)
                    for k, v in self.black_notes.items():
                        k.configure(bg='black', state=NORMAL)

                    self.window.delete(0, END)
                    self.window.insert(0, f"Turned ON")
                return self

    class Interface(Functionality):

        def __init__(self):
            super().__init__()

            # --------- THE INTERFACE ------------
            # BUTTONS
            # white notes
            buttons = Button(self.root, pady=110)
            buttons.grid(row=1, column=0)

            button_do_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}C_3'))
            button_do_oct1.place(x=42, y=175)
            button_re_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}D_3'))
            button_re_oct1.place(x=109, y=175)
            button_mi_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}E_3'))
            button_mi_oct1.place(x=176, y=175)
            button_fa_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}F_3'))
            button_fa_oct1.place(x=243, y=175)
            button_sol_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                     command=lambda: self.button_click(f'{self.style_name}G_3'))
            button_sol_oct1.place(x=310, y=175)
            button_la_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}A_3'))
            button_la_oct1.place(x=377, y=175)
            button_si_oct1 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}B_3'))
            button_si_oct1.place(x=444, y=175)
            button_do_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}C_4'))
            button_do_oct2.place(x=511, y=175)
            button_re_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}D_4'))
            button_re_oct2.place(x=578, y=175)
            button_mi_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}E_4'))
            button_mi_oct2.place(x=645, y=175)
            button_fa_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}F_4'))
            button_fa_oct2.place(x=712, y=175)
            button_sol_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                     command=lambda: self.button_click(f'{self.style_name}G_4'))
            button_sol_oct2.place(x=779, y=175)
            button_la_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}A_4'))
            button_la_oct2.place(x=846, y=175)
            button_si_oct2 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}B_4'))
            button_si_oct2.place(x=913, y=175)
            button_do_oct3 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}C_5'))
            button_do_oct3.place(x=980, y=175)
            button_re_oct3 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}D_5'))
            button_re_oct3.place(x=1047, y=175)
            button_mi_oct3 = Button(self.root, padx=29, pady=110, bg="#f2f2f2", state=DISABLED,
                                    command=lambda: self.button_click(f'{self.style_name}E_5'))
            button_mi_oct3.place(x=1114, y=175)

            # black notes
            button_do_dies_oct1 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}C#_3'))
            button_do_dies_oct1.place(x=85, y=175)
            button_re_dies_oct1 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}D#_3'))
            button_re_dies_oct1.place(x=152, y=175)
            button_fa_dies_oct1 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}F#_3'))
            button_fa_dies_oct1.place(x=286, y=175)
            button_sol_dies_oct1 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                          command=lambda: self.button_click(f'{self.style_name}G#_3'))
            button_sol_dies_oct1.place(x=353, y=175)
            button_la_dies_oct1 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}A#_3'))
            button_la_dies_oct1.place(x=420, y=175)
            button_do_dies_oct2 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}C#_4'))
            button_do_dies_oct2.place(x=554, y=175)
            button_re_dies_oct2 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}D#_4'))
            button_re_dies_oct2.place(x=621, y=175)
            button_fa_dies_oct2 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}F#_4'))
            button_fa_dies_oct2.place(x=755, y=175)
            button_sol_dies_oct2 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                          command=lambda: self.button_click(f'{self.style_name}G#_4'))
            button_sol_dies_oct2.place(x=822, y=175)
            button_la_dies_oct2 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}A#_4'))
            button_la_dies_oct2.place(x=889, y=175)
            button_do_dies_oct3 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
                                         command=lambda: self.button_click(f'{self.style_name}C#_54'))
            button_do_dies_oct3.place(x=1023, y=175)
            button_re_dies_oct3 = Button(self.root, padx=14, pady=60, bg="#d4d4d4", state=DISABLED,
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
            black_notes = {
                button_do_dies_oct1: 'C#_3', button_re_dies_oct1: 'D#_3', button_fa_dies_oct1: 'F#_3',
                button_sol_dies_oct1: 'G#_3', button_la_dies_oct1: 'A#_3', button_do_dies_oct2: 'C#_4',
                button_re_dies_oct2: 'D#_4', button_fa_dies_oct2: 'F#_4', button_sol_dies_oct2: 'G#_4',
                button_la_dies_oct2: 'A#_4', button_do_dies_oct3: 'C#_54', button_re_dies_oct3: 'D#_5'
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
            rec_obj = self.RecorderBlock(self.root, self.window, self.feature_font)
            radio_obj = self.RadioButton(self.window, text_info, buttons_dict, self.feature_font, intro="Standard")
            voice_obj = self.Voices(notes_voices, self.window, self.dir, self.volume, self.vertical, self.feature_font,
                                    self.style_name, self.root, rec_obj)

            self.Switch(self.root, radio_obj, voice_obj, rec_obj.rec_on_off, rec_obj.rec_tab, self.vertical,
                        self.window, buttons_dict, black_notes, self.feature_font)

    class Manage(Interface):
        def __init__(self):
            super().__init__()
            self.root.mainloop()


if __name__ == "__main__":
    start = Piano()
    start.Manage()
