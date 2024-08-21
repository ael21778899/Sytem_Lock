# System_Lock v2.0
# 2024 / 8 / 20
# written by ael2177

import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import keyboard
import json
import os

# functions
def Prevent_Security_management():
    os.system('shutdown -s -t 0')

def Password_Judgement():
    Password = Password_input.get()
    if Password == Password_Load():
        SCREEN.quit()
        SCREEN.destroy()

    else:
        tkinter.messagebox.showinfo(title = '', message = 'The password is wrong!')

def Password_Load():
    with open('Password.json', mode = 'r', encoding = 'utf-8') as File:
        dict = json.load(File)
        Password = dict['Password']
        return Password

# hotkeys
# example:
# keyboard.add_hotkey('ctrl+alt+delete', Prevent_Security_management) # Security_management


keyboard.add_hotkey('ctrl+alt+enter', Password_Judgement)

# main screen
SCREEN = tkinter.Tk()

SCREEN.attributes('-fullscreen', True)

Text = tkinter.Label(SCREEN, text = 'Please enter password :')
Text.pack()

Password_input = tkinter.Entry(SCREEN, show = ' ')
Password_input.pack()

SCREEN.protocol('WM_DELETE_WINDOW', Prevent_Security_management)

SCREEN.mainloop()