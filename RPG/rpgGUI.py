#import all the stuff or bad
import os
import string
import PySimpleGUI as psg
import random
from Utils.passwordClasses import PasswordExtra, PasswordProperties

#create pass_prop object
pass_prop = PasswordProperties()

#password generating class
class PasswordGen:
    def __init__(self, prop) -> None:
        self.prop = prop
        self.value:str = ''

    def generate(self, usable_charaters):
        for x in range(self.prop.lenght):
            self.value = self.value + random.choice(usable_characters)

    def checkAllUpperCase(self) -> bool:
        f_res: bool = False
        if self.prop.AllUppercase is True:
            for lenght in range(self.prop.lenght):
                for chars in range(len(string.ascii_uppercase)):
                    if self.value[lenght] == string.ascii_uppercase[chars]:
                        f_res = True
        else:
            f_res = True
        #print(f'checkAllUpperCase is {f_res}')
        return f_res
                
    def checkNumbers(self) -> bool:
        f_res: bool = False
        if self.prop.UseNumbers == True:
            for lenght in range(self.prop.lenght):
                for numbers in range(len(string.digits)):
                    if self.value[lenght] == string.digits[numbers]:
                        f_res = True
        else:
            f_res = True

        #print(f'checkNumbers is {f_res}')
        return f_res
    
    def checkSymbols(self) -> bool:
        f_res: bool = False
        if self.prop.UseSymbols == True:
            for lenght in range(self.prop.lenght):
                for symbols in range(len(extra.symbols)):
                    if self.value[lenght] == extra.symbols[symbols]:
                        f_res = True
        else:
            f_res = True
        
        #print(f'checkSymbols is {f_res}')
        return f_res
    
    def checkParenthesis(self) -> bool:
        f_res: bool = False
        if self.prop.UseParenthesis == True:
            for lenght in range(self.prop.lenght):
                for parenthesis in range(len(extra.parenthesis)):
                    if self.value[lenght] == extra.parenthesis[parenthesis]:
                        f_res = True
        else:
            f_res = True
        
        #print(f'checkParenthesis is {f_res}')
        return f_res
        
        
#change pwd properties if needed
pwGen = PasswordGen(pass_prop)
extra = PasswordExtra()

#class for layout cause why not

layout = [[]]

layout = [#[psg.Text('Open On Startup')],
            [psg.Text('Please enter the password lenght. Minimum and default lenght is 12 characters. Maximum value is 200'), psg.InputText(default_text ='12')],
            [psg.Button(button_text = 'All Uppercase', size = (15, 1), button_color = ('white', 'red'), key = 'AllUppercaseUpdate')],
            [psg.Button(button_text = 'Use Numbers', size = (15, 1), button_color = ('white', 'red'), key = 'UseNumbersUpdate')],
            [psg.Button(button_text = 'Use Symbols', size = (15, 1), button_color = ('white', 'red'), key = 'UseSymbolsUpdate')],
            [psg.Button(button_text = 'Use Parenthesis', size = (15, 1), button_color = ('white', 'red'), key = 'UseParenthesisUpdate')],
            [psg.Button(button_text = 'Generate Password', size = (15, 1), key = 'PrintPw')],
            [psg.Button('Exit', key = 'Exit_Program')],
            [psg.InputText(pwGen.value, key = 'PWV')],
            [psg.Text(f'Password lenght: ', key = 'PWL')]]

#initialize window
window = psg.Window('Password Generator', layout, size = (1000, 600),  resizable = True, grab_anywhere_using_control = True, finalize = False)
counter = 1

while True:
    
    event, values = window.read()

    # Break if window is closed or 'Exit_Program is called
    if event == psg.WIN_CLOSED or event == 'Exit_Program':
        break

    #uppercase
    elif event == 'AllUppercaseUpdate':
        if pass_prop.AllUppercase is False:
            window['AllUppercaseUpdate'].update(button_color = ('white','green'))
            pass_prop.AllUppercase = True
        elif pass_prop.AllUppercase is True:
            window['AllUppercaseUpdate'].update(button_color = ('white','red'))
            pass_prop.AllUppercase = False

    #numbers
    elif event == 'UseNumbersUpdate':
        if pass_prop.UseNumbers is False:
            window['UseNumbersUpdate'].update(button_color = ('white','green'))
            pass_prop.UseNumbers = True
        elif pass_prop.UseNumbers is True:
            window['UseNumbersUpdate'].update(button_color = ('white','red'))
            pass_prop.UseNumbers = False

    elif event == 'UseSymbolsUpdate':
        if pass_prop.UseSymbols is False:
            window['UseSymbolsUpdate'].update(button_color = ('white','green'))
            pass_prop.UseSymbols = True
        elif pass_prop.UseSymbols is True:
            window['UseSymbolsUpdate'].update(button_color = ('white','red'))
            pass_prop.UseSymbols = False

    #parenthesis
    elif event == 'UseParenthesisUpdate':
        if pass_prop.UseParenthesis is False:
            window['UseParenthesisUpdate'].update(button_color = ('white','green'))
            pass_prop.UseParenthesis = True
        elif pass_prop.UseParenthesis is True:
            window['UseParenthesisUpdate'].update(button_color = ('white','red'))
            pass_prop.UseParenthesis = False

    #print it or even more pepega
    elif event == "PrintPw":

        #input pass_prop lenght
        if (int(values[0]) < 12) or (int(values[0]) > 200):
            pass_prop.lenght = 12
        elif int(values[0]) > 12:
            pass_prop.lenght = int(values[0])

        #create list or boom?
        usable_characters = []

        # usable letters check
        if pass_prop.AllUppercase is True:
            usable_characters = string.ascii_uppercase
            # print('pw_alluppercase is 1')
        elif pass_prop.AllUppercase is False:
            usable_characters = string.ascii_letters
            # print('pw_alluppercase is 0')

        # usable numbers
        if pass_prop.UseNumbers is True:
            usable_characters += string.digits

        # usable symbols
        if pass_prop.UseSymbols is True:
            usable_characters += extra.symbols

        # usable parenthesis
        if pass_prop.UseParenthesis is True:
            usable_characters += extra.parenthesis

        # make sure it's empty before generating a new one
        pwGen.value = ''
        pwGen.generate(usable_characters) 

        while (pwGen.checkAllUpperCase() == False or pwGen.checkNumbers() == False or pwGen.checkParenthesis() == False or pwGen.checkSymbols() == False):
            #print(pwGen.value)
            pwGen.value = ''
            pwGen.generate(usable_characters)
        
        #print(f'Your password is: {pwGen.value}')
        window['PWV'].update(f'Your password is: {pwGen.value}')
        window['PWL'].update(f'Password lenght: {len(pwGen.value)}')

window.close()