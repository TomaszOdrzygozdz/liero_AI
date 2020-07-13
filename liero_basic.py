import os
import time
from collections import namedtuple, defaultdict

os.system('xset r off')

import random

from tkinter import *

from GAME_SETTINGS import SPF
from game_objects import State, Vector

master = Tk()



w = Canvas(master, width=900, height=900)
w.pack()



# w.create_rectangle(50, 20, 150, 80, fill="#476042")
# w.create_rectangle(65, 35, 135, 65, fill="yellow")
# w.create_line(0, 0, 50, 20, fill="#476042", width=3)
# w.create_line(0, 100, 50, 80, fill="#476042", width=3)
# w.create_line(150,20, 200, 0, fill="#476042", width=3)
# w.create_line(150, 80, 200, 100, fill="#476042", width=3)
#w.create_oval(0,0,200,200, fill="red")

xxx = State()

def keydown(e):
    print(f'pressed {e.char}')
    xxx.worms[1].pressed_keys[e.keysym] = True

def keyup(e):
    print(f'rel {e}')
    xxx.worms[1].pressed_keys[e.keysym] = False

master.bind("<KeyPress>", keydown)
master.bind("<KeyRelease>", keyup)



#mainloop()

def ask_for_update():
    xxx.move_worm()
    w.delete("all")
    xxx.draw_state(w)
    # print(xxx.worms[1].pressed_keys)
    master.after(SPF, ask_for_update)

master.after(0, ask_for_update)
master.mainloop()