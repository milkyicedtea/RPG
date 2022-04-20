from __future__ import with_statement
from dataclasses import dataclass
import os
import PySimpleGUI as psg
import json
from utils.open_on_startup import OpenOnStartup as oos

@dataclass
class Button:
    is_on = True


with open('appInfo/oos.json') as f:
    s = f.readlines()[1]

result = json.loads(s)

psg.theme('DarkAmber') # theme setting

layout = [  [psg.Text('Open On Startup')],
            [psg.Button(button_text = 'On', size = (3, 1), button_color = ('white', 'green'), key = 'Oss_Edit')],
            [psg.Button('Exit', key = 'Exit_Program')]
         ]

# create the windows passing in name, 'layout' and some properties
window = psg.Window('MyVeryCoolApp.py', layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = True) # pass in the window title and the layout


while True:

    # read events and values from the window
    event, value = window.read()

    # switch event
    if event == 'Oss_Edit':
        Button.is_on = not Button.is_on
        window.Element('Oss_Edit').Update(('Off', 'On')[Button.is_on], button_color = (('white', ('red', 'green')[Button.is_on])))
        if result == "{'oos_value': 'False'}":
            data = {
                "oss_value" : "False"
            }
            with open('appInfo/oos.json', 'w') as outfile:
                json.dump(data, outfile)
        print(result)

    # Break if window is closed or 'Exit_Program is called
    if event == psg.WIN_CLOSED or event == 'Exit_Program':
        break

window.close()