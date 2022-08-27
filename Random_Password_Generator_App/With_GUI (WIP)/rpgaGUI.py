#import all the stuff or bad
import string
import os
import PySimpleGUI as psg
import random
from dataclasses import dataclass

#dataclass for PW properties
@dataclass
class PasswordProperties:
    lenght: int = 10
    AllUppercase: bool = False
    MixedCharacters: bool = False
    value: str = ''

#class for layout cause why not
class MyLayout():
    layout = [[]]

MyLayout.layout = [#[psg.Text('Open On Startup')],
            [psg.Text('Please enter the password lenght. Default password lenght is 10. Maxmium value is 100'), psg.InputText()],
            [psg.Button(button_text = 'All Uppercase', size = (15, 1), button_color = ('white', 'red'), key = 'AllUppercaseUpdate')],
            [psg.Button(button_text = 'Mixed Characters', size = (15, 1), button_color = ('white', 'red'), key = 'MixedCharactersUpdate')],
            [psg.Button(button_text = 'Generate Password', size = (15, 1), key = 'PrintPw')],
            [psg.Button('Exit', key = 'Exit_Program')],
            [psg.Text(PasswordProperties.value, key = 'PWV')]]

#create password object
password = PasswordProperties()

window = psg.Window('Password Generator', MyLayout.layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = True)
counter = 1

while True:
    
    event, values = window.read()

    #input password lenght
    # print(values[0])
    if values[0] == None or values[0] == '' or int(values[0]) > 100:
        password.lenght = 10
    elif int(values[0]) > 10:
        password.lenght = int(values[0])

    # Break if window is closed or 'Exit_Program is called
    if event == psg.WIN_CLOSED or event == 'Exit_Program':
        break

    elif event == 'AllUppercaseUpdate':
        if password.AllUppercase is False:
            window['AllUppercaseUpdate'].update(button_color = ('white','green'))
            password.AllUppercase = True
        elif password.AllUppercase is True:
            window['AllUppercaseUpdate'].update(button_color = ('white','red'))
            password.AllUppercase = False

    elif event == 'MixedCharactersUpdate':
        if password.MixedCharacters is False:
            window['MixedCharactersUpdate'].update(button_color = ('white','green'))
            password.MixedCharacters = True
        elif password.MixedCharacters is True:
            window['MixedCharactersUpdate'].update(button_color = ('white','red'))
            password.MixedCharacters = False

    #print it or even more pepega
    elif event == "PrintPw":
        #create list or boom?
        usable_characters = []

        #usable characters watching inputs
        if password.AllUppercase == True:
            usable_characters = string.ascii_uppercase
            # print('pw_alluppercase is 1')
        elif password.AllUppercase == False:
            usable_characters = string.ascii_letters
            # print('pw_alluppercase is 0')

        #mixed characters watching inputs
        if password.MixedCharacters == True:
            usable_characters = usable_characters + string.digits

        #make sure it's empty before generating a new one!
        password.value = ''

        #generate password or pepega lmao

        for x in range(password.lenght):
            password.value = password.value + random.choice(usable_characters)
        #print(f'Your password is: {password.value}')
        window['PWV'].update(f'Your password is: {password.value}')

window.close()