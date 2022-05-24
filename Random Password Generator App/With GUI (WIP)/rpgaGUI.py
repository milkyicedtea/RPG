#import all the stuff or bad
import string
import os
import PySimpleGUI as psg
import random
from dataclasses import dataclass

#class for layout cause why not, right?
class MyLayout():
    layout = [[]]

MyLayout.layout = [[psg.Text('Open On Startup')],
            [psg.Text('Please enter the password lenght. Default password lenght is 10'), psg.InputText()],
            [psg.Button(button_text = 'All Uppercase', size = (3, 1), button_color = ('white', 'red'), key = 'AllUppercaseUpdate')],
            [psg.Button(button_text = 'Mixed Characters', size = (3, 1), button_color = ('white', 'red'), key = 'MixedCharactersUpdate')],
            [psg.Button('Exit', key = 'Exit_Program')]]

#class for PW properties
@dataclass
class PasswordProperties:
    lenght: int = 10
    AllUppercase: bool = False
    MixedCharacters: bool = False
    value: str = ""

#create password object
password = PasswordProperties()

window = psg.Window('Password Generator', MyLayout.layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = True)
counter = 1

while True:
    
    event, values = window.read()

    #input password lenght
    password.lenght = values[0]
    print(password.lenght)

    """
    #selection for uppercase only characters
    selection:int = int(input('Select if your password has to be uppercase only (0 for mixed, 1 for uppercase only) '))
    print(f'selection is {selection}')
    if selection == 1:
        password.AllUppercase = True
    else:
        password.AllUppercase = False
    print(password.AllUppercase)

    #selection for adding numbers or having letters only
    selection = int(input('Select if your password will contain letter only (0 for only letters, 1 for both) '))
    if selection == 1:
        password.MixedCharacters = True
    else:
        password.MixedCharacters = False

    #create list or boom?
    usable_characters = []

    #usable characters watching inputs
    if password.AllUppercase == True:
        usable_characters = string.ascii_uppercase
        print('pw_alluppercase is 1')
    elif password.AllUppercase == False:
        usable_characters = string.ascii_letters
        print('pw_alluppercase is 0')

    #mixed characters watching inputs
    if password.MixedCharacters == True:
        usable_characters = usable_characters + string.digits
        
    #generate password or pepega lmao
    for x in range(password.lenght):
        password.value = password.value + random.choice(usable_characters)
        x+=1
    """


    # Break if window is closed or 'Exit_Program is called
    if event == psg.WIN_CLOSED or event == 'Exit_Program':
        break

    #print it or even more pepega
    print(f'Your password is: {password.value}')

window.close()