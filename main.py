# System_Lock v3.0
# 2024 / X / XX
# written by ael2177

import tkinter
import tkinter.messagebox
import keyboard
import json
import os

# functions
def Prevent_Security_management():
    os.system(command)

def Config_Loder():
    global command
    global password

    with open('config.json', mode = 'r', encoding = 'utf-8') as File:
        config = json.load(File)
        command = config['command']
        password = config['password']

def Password_Judgement():
    Password = Password_input.get()
    if Password == password:
        SCREEN.quit()
        SCREEN.destroy()

    else:
        tkinter.messagebox.showinfo(title = '', message = 'The password is wrong!')

# In development
# def Password_Loadr():
#     with open('Password.json', mode = 'r', encoding = 'utf-8') as File:
#         dict = json.load(File)
#         Password = dict['Password']
#         return Password

# hotkeys
# example:
# keyboard.add_hotkey('ctrl+alt+delete', Prevent_Security_management) # Security_management

keyboard.add_hotkey('windows+tab', Prevent_Security_management) # Switch_Desktop

# start
Config_Loder()
keyboard.add_hotkey('ctrl+alt+enter', Password_Judgement)

# main screen
SCREEN = tkinter.Tk()

SCREEN.attributes('-fullscreen', True)
SCREEN.attributes('-topmost', True)

Text = tkinter.Label(SCREEN, text = 'Please enter password :')
Text.pack()

Password_input = tkinter.Entry(SCREEN, show = ' ')
Password_input.pack()

SCREEN.protocol('WM_DELETE_WINDOW', Prevent_Security_management)

SCREEN.mainloop()