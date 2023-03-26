###############
#             #
#     RPG     #
#             #
###############

# Some comments might be old!

#import all the stuff or bad
import os
import string
import PySimpleGUI as psg

from Utils.buttonHandlers import ButtonHandlers
from Utils.passwordClasses import PasswordGen, PasswordProperties

#create pass_prop object
pass_prop = PasswordProperties()
        
#create actual pwGen object which will contain the properties from pass_prop
pwGen = PasswordGen(pass_prop)

#define layout
layout = [#[psg.Text('Open On Startup')],
            [psg.Text('Password Generator', font = '_ 15', justification = 'c', expand_x = True)],
            [psg.Text('Minimum and default lenght is 12 characters. Maximum value is 200.')],
            [psg.Text('Your password will be copied to your clipboard when generated.')],
            [psg.Text('Please enter the your password lenght'), psg.InputText(default_text ='12', size = 4)],
            [psg.Button(button_text = 'All Uppercase', size = (15, 1), button_color = ('white', 'red'), key = 'AllUppercaseUpdate')],
            [psg.Button(button_text = 'Use Numbers', size = (15, 1), button_color = ('white', 'red'), key = 'UseNumbersUpdate')],
            [psg.Button(button_text = 'Use Symbols', size = (15, 1), button_color = ('white', 'red'), key = 'UseSymbolsUpdate')],
            [psg.Button(button_text = 'Use Parenthesis', size = (15, 1), button_color = ('white', 'red'), key = 'UseParenthesisUpdate')],
            [psg.Button(button_text = 'Use Minus', size = (15, 1), button_color = ('white', 'red'), key = 'UseMinusUpdate')],
            [psg.Button(button_text = 'Use Underscore', size = (15, 1), button_color = ('white', 'red'), key = 'UseUnderscoreUpdate')],
            [psg.Button(button_text = 'Generate Password', size = (15, 1), key = 'PrintPw')],
            [psg.Button('Exit', key = 'Exit_Program')],
            [psg.Text('Your password is:'), psg.InputText(pwGen.value, size = 20, key = 'PWV')],
            [psg.Text(f'Password lenght: 12', key = 'PWL')]]

#initialize window
window = psg.Window('Password Generator', layout,  resizable = True, grab_anywhere_using_control = True, finalize = False)

def main_app():
    while True:
        
        event, values = window.read()

        # Break if window is closed or 'Exit_Program is called
        if event == psg.WIN_CLOSED or event == 'Exit_Program':
            break

        #uppercase button
        elif event == 'AllUppercaseUpdate':
            ButtonHandlers.UppercaseUpdate(pass_prop, window)

        #numbers button
        elif event == 'UseNumbersUpdate':
            ButtonHandlers.NumbersUpdate(pass_prop, window)

        #symbol button
        elif event == 'UseSymbolsUpdate':
            ButtonHandlers.SymbolsUpdate(pass_prop, window)

        #parenthesis button
        elif event == 'UseParenthesisUpdate':
            ButtonHandlers.ParenthesisUpdate(pass_prop, window)

        #minus button
        elif event == 'UseMinusUpdate':
            ButtonHandlers.MinusUpdate(pass_prop, window)

        #underscore button
        elif event == 'UseUnderscoreUpdate':
            ButtonHandlers.UnderscoreUpdate(pass_prop, window)

        #generate button
        elif event == "PrintPw":

            #get pass_prop lenght from the text area
            if (int(values[0]) < 12) or (int(values[0]) > 200):
                pass_prop.lenght = 12
            elif int(values[0]) > 12:
                pass_prop.lenght = int(values[0])

            #make sure it's empty before generating a new one
            pwGen.value = ''

            #finally generate the password!
            characters = pwGen.getCharacters()
            pwGen.generate(characters) 

            #do all the checks
            #counter: int = 0
            while not pwGen.checksResult():
                #print(pwGen.value)
                #counter+=1
                #if any of the check returns false, reset and generate once again
                pwGen.value = ''
                pwGen.generate(characters)

            #print(counter)
            
            #print(f'Your password is: {pwGen.value}')

            #save in clipboard for easy access and update the fields
            psg.clipboard_set(pwGen.value)
            window['PWV'].update(f'{pwGen.value}')
            window['PWL'].update(f'Password lenght: {len(pwGen.value)}')

    window.close()

if __name__ == "__main__":
    main_app()