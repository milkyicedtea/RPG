import PySimpleGUI as psg
import psycopg2
import dotenv

psg.theme('DarkAmber') # theme setting

layout = [  [psg.Text('Row 1')],
            [psg.Text('Row 2 which is form'), psg.InputText()],
            [psg.Button('Ok'), psg.Button('Cancel')]    ]

# now we create the windows
window = psg.Window('Bad', layout) # pass in the window title and the layout

while True:
    event, values = window.read()   # read values from InputText()
    if event == psg.WIN_CLOSED or event == 'Cancel': # Cancel is the name of the button
        break
    print(values[0])

window.close()