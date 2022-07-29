import argparse, sys
import tkinter as tk
import tkinter.messagebox as tkMessageBox


def update_timeText():
    global timer, window_title
    if state:
        if countdown:
            if (timer[0] == 0 and timer[1] <= 1):
                reset()
                tkMessageBox.showinfo(title=window_title,
                        message='Time out!')
                return #Timer exited, return and do nothing.
            # Decrement a second at every call to this function
            timer[1] -= 1
            if (timer[1] <= 0):
                timer[0] -= 1
                timer[1] = 59
        else:
            # Every time this function is called, increment 1 second
            timer[1] += 1
            if (timer[1] >= 60):
                timer[0] += 1
                timer[1] = 0

        # ----------- Common for both countdown and countup
        timeString = pattern.format(timer[0], timer[1])

        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)

    # Call the update_timeText() function after 1 second
    root.after(1000, update_timeText)

def start():
    global state
    state = True

def pause():
    global state
    state = False

def reset():
    global state, timer, countdown, pattern
    state = False
    if countdown:
        timer = [timelimit , 0]
        timestr = pattern.format(timer[0], timer[1])
    else:
        timer = [0, 0]
        timestr = '00:00'

    timeText.configure(text=timestr)

def quitclock():
    root.destroy()

def gt_zero(s):
    try:
        if int(s) > 0:
            return int(s)
        else:
            raise argparse.ArgumentTypeError('Time limit must be an int > 0')
    except:
        raise argparse.ArgumentTypeError('Time limit must be an int > 0')

if __name__=='__main__':
    countdown = False
    timestr = ''
    parser = argparse.ArgumentParser(description='Simple timer')
    parser.add_argument('--name', '-n', help='Name of the timer widget',
            default=' <=-=- Simple timer -=-=> ')
    parser.add_argument('--reverse', '-r', type = gt_zero,
            help='Countdown timer with time limit (>0)')
    parser.add_argument('--size', '-s',
            help='Font size for the timer', default='75')
    values = parser.parse_args()
    window_title = values.name
    font_size = values.size

    if values.reverse:
        countdown = True
        timelimit = int(values.reverse)

    # Simple status flag; False => timer is not running, True otherwise
    state = False
    # For the padding format
    pattern = '{0:02d}:{1:02d}'

    root = tk.Tk()
    root.wm_title(window_title)

    # Create a timeText Label (a text box)
    timeText = tk.Label( root,
            text = timestr, font = ("Sans",font_size),
            background = 'black', foreground = 'green')
    timeText.pack(fill='x')

    buttons = [ ('Start/Unpause', start), ('Pause', pause),
            ('Reset', reset), ('Quit', quitclock) ]

    for btn in buttons:
        tk.Button(root, text = btn[0], command=btn[1]).pack(fill='x')

    reset()
    update_timeText()
    root.mainloop()
