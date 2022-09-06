#import all the stuff or bad
import os
import string
import PySimpleGUI as psg
import random
from dataclasses import dataclass

#dataclass because string sucks
@dataclass
class PasswordExtra:
    minus:str = '-'
    underline: str = '_'
    symbols:str = '!@#$%&'
    parenthesis:str = r'()[]{}'


#dataclass for PW properties
@dataclass
class PasswordProperties:
    lenght: int = 10
    AllUppercase: bool = False
    UseNumbers: bool = False
    UseMinus:bool = False
    UseUnderline:bool = False
    UseSymbols: bool = False
    UseParenthesis:bool = False
    value: str = ''

#class for layout cause why not
class MyLayout():
    layout = [[]]

MyLayout.layout = [#[psg.Text('Open On Startup')],
            [psg.Text('Please enter the password lenght. Default password lenght is 10. Maxmium value is 100'), psg.InputText()],
            [psg.Button(button_text = 'All Uppercase', size = (15, 1), button_color = ('white', 'red'), key = 'AllUppercaseUpdate')],
            [psg.Button(button_text = 'Use Numbers', size = (15, 1), button_color = ('white', 'red'), key = 'UseNumbersUpdate')],
            [psg.Button(button_text = 'Use Minus', size = (15, 1), button_color = ('white', 'red'), key = 'UseMinusUpdate')],
            [psg.Button(button_text = 'Use Underline', size = (15, 1), button_color = ('white', 'red'), key = 'UseUnderlineUpdate')],
            [psg.Button(button_text = 'Use Symbols', size = (15, 1), button_color = ('white', 'red'), key = 'UseSymbolsUpdate')],
            [psg.Button(button_text = 'Use Parenthesis', size = (15, 1), button_color = ('white', 'red'), key = 'UseParenthesisUpdate')],
            [psg.Button(button_text = 'Generate Password', size = (15, 1), key = 'PrintPw')],
            [psg.Button('Exit', key = 'Exit_Program')],
            [psg.Text(PasswordProperties.value, key = 'PWV')]]

#create password object
password = PasswordProperties()
extra = PasswordExtra()

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

    #uppercase
    elif event == 'AllUppercaseUpdate':
        if password.AllUppercase is False:
            window['AllUppercaseUpdate'].update(button_color = ('white','green'))
            password.AllUppercase = True
        elif password.AllUppercase is True:
            window['AllUppercaseUpdate'].update(button_color = ('white','red'))
            password.AllUppercase = False

    #numbers
    elif event == 'UseNumbersUpdate':
        if password.UseNumbers is False:
            window['UseNumbersUpdate'].update(button_color = ('white','green'))
            password.UseNumbers = True
        elif password.UseNumbers is True:
            window['UseNumbersUpdate'].update(button_color = ('white','red'))
            password.UseNumbers = False

    #minus
    elif event == 'UseMinusUpdate':
        if password.UseMinus is False:
            window['UseMinusUpdate'].update(button_color = ('white','green'))
            password.UseMinus = True
        elif password.UseMinus is True:
            window['UseNumbersUpdate'].update(button_color = ('white','red'))
            password.UseMinus = False

    #underline
    elif event == 'UseUnderlineUpdate':
        if password.UseUnderline is False:
            window['UseUnderlineUpdate'].update(button_color = ('white','green'))
            password.UseUnderline = True
        elif password.UseUnderline is True:
            window['UseUnderlineUpdate'].update(button_color = ('white','red'))
            password.UseUnderline = False

    elif event == 'UseSymbolsUpdate':
        if password.UseSymbols is False:
            window['UseSymbolsUpdate'].update(button_color = ('white','green'))
            password.UseSymbols = True
        elif password.UseSymbols is True:
            window['UseSymbolsUpdate'].update(button_color = ('white','red'))
            password.UseSymbols = False

    #parenthesis
    elif event == 'UseParenthesisUpdate':
        if password.UseParenthesis is False:
            window['UseParenthesisUpdate'].update(button_color = ('white','green'))
            password.UseParenthesis = True
        elif password.UseParenthesis is True:
            window['UseParenthesisUpdate'].update(button_color = ('white','red'))
            password.UseParenthesis = False

    #print it or even more pepega
    elif event == "PrintPw":
        #create list or boom?
        usable_characters = []

        if password.AllUppercase is True:
            usable_characters = string.ascii_uppercase
            # print('pw_alluppercase is 1')
        elif password.AllUppercase is False:
            usable_characters = string.ascii_letters
            # print('pw_alluppercase is 0')


        if password.UseNumbers is True:
            usable_characters += string.digits

        if password.UseMinus is True:
            usable_characters += extra.minus

        if password.UseUnderline is True:
            usable_characters += extra.underline

        if password.UseSymbols is True:
            usable_characters += extra.symbols

        if password.UseParenthesis is True:
            usable_characters += extra.parenthesis


        #make sure it's empty before generating a new one!
        password.value = ''

        #generate password or pepega lmao

        for x in range(password.lenght):
            password.value = password.value + random.choice(usable_characters)
        #print(f'Your password is: {password.value}')
        window['PWV'].update(f'Your password is: {password.value}')

window.close()