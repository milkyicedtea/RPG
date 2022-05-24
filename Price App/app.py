import os

from dataclasses import dataclass
import PySimpleGUI as psg
from utils.open_on_startup import OpenOnStartup as oos

class MyLayout():
    layout = [[]]

file_to_open = open('appInfo/switchstate.txt', 'r+')
result = file_to_open.readline()
print(result)
if result == '' or result == None:
    result = "F"
    file_to_open.write(result)
    is_on:bool = False
    print('pp0')
    print(result)
file_to_open.close()

psg.theme('DarkAmber') # theme setting

if result == 'T':
        is_on = True
        MyLayout.layout = [  [psg.Text('Open On Startup')],
            [psg.Button(button_text = 'On', size = (3, 1), button_color = ('white', 'green'), key = 'Oss_Edit')],
            [psg.Button(button_text = 'Add new product', key = 'Add_New_Product')],
            [psg.Button('Exit', key = 'Exit_Program')]]
        print('pp')
elif result == "F":
        is_on = False
        MyLayout.layout = [  [psg.Text('Open On Startup')],
            [psg.Button(button_text = 'Off', size = (3, 1), button_color = ('white', 'red'), key = 'Oss_Edit')],
            [psg.Button(button_text = 'Add new product', key = 'Add_New_Product')],
            [psg.Button('Exit', key = 'Exit_Program')]
         ]
        print('pp2')

# create the windows passing in name, 'layout' and some properties
window = psg.Window('MyVeryCoolApp.py', MyLayout.layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = True) # pass in the window title and the layout


while True:

    # read events and values from the window
    event, value = window.read()
    print(event)
    # switch event
    if event == 'Oss_Edit':
        if is_on == True:
            f = open('appInfo/switchstate.txt', 'r+')
            f.write(f'T')

        elif is_on == False:
            f = open('appInfo/switchstate.txt', 'r+')
            f.write(f'F')
            print(__file__)
            oos.AddToRegistry(__file__)

        is_on = not is_on
        print(is_on)
        file_to_open.close()
        window.Element('Oss_Edit').Update(('Off', 'On')[is_on], button_color = (('white', ('red', 'green')[is_on])))
        

    # Break if window is closed or 'Exit_Program is called
    if event == psg.WIN_CLOSED or event == 'Exit_Program':
        break

window.close()