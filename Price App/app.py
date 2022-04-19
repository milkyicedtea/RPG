import os
import PySimpleGUI as psg
import json
from utils.open_on_startup import OpenOnStartup as oos

psg.theme('Reddit') # theme setting

layout = [  [psg.Text('Open On Startup')],
            [psg.Button(button_text = '', key = 'Oss_Edit')],
            [psg.Button('Exit', key = 'Exit_Program')]
         ]

# now we create the windows
window = psg.Window('MyVeryCoolApp.py', layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = True) # pass in the window title and the layout

while True:
    event, value = window.read()   # read events and values from the window

    if event == psg.WIN_CLOSED or event == 'Exit_Program': # Break if window is closed
        break

window.close()