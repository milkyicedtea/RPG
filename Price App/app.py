import os

from dataclasses import dataclass
import PySimpleGUI as psg
import linecache as lc
from utils.open_on_startup import OpenOnStartup as oos

class MyLayout():
    layout = [[]]

is_on:bool = True
result =  lc.getline('appInfo/switchstate.txt', 1)
print(result[0])

psg.theme('DarkAmber') # theme setting

if result[0] == "T":
        is_on = True
        MyLayout.layout = [  [psg.Text('Open On Startup')],
            [psg.Button(button_text = 'On', size = (3, 1), button_color = ('white', 'green'), key = 'Oss_Edit')],
            [psg.Button(button_text = 'Add new product', key = 'Add_New_Product')],
            [psg.Button('Exit', key = 'Exit_Program')]
         ]
        print('pp')
        lc.clearcache()
elif result[0] == "F":
        is_on = False
        MyLayout.layout = [  [psg.Text('Open On Startup')],
            [psg.Button(button_text = 'Off', size = (3, 1), button_color = ('white', 'red'), key = 'Oss_Edit')],
            [psg.Button(button_text = 'Add new product', key = 'Add_New_Product')],
            [psg.Button('Exit', key = 'Exit_Program')]
         ]
        print('pp2')
        lc.clearcache()

# create the windows passing in name, 'layout' and some properties
window = psg.Window('MyVeryCoolApp.py', MyLayout.layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = True) # pass in the window title and the layout


while True:

    # read events and values from the window
    event, value = window.read()
    print(event)
    # switch event
    if event == 'Oss_Edit':
        window.Element('Oss_Edit').Update(('Off', 'On')[is_on], button_color = (('white', ('red', 'green')[is_on])))
        is_on = not is_on
        f = open('appInfo/switchstate.txt', 'w')
        f.write(f'{is_on}')

    # Break if window is closed or 'Exit_Program is called
    if event == psg.WIN_CLOSED or event == 'Exit_Program':
        break

window.close()