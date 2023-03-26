from Utils.passwordClasses import PasswordProperties
from PySimpleGUI import Window

class ButtonHandlers:
    def UppercaseUpdate(prop: PasswordProperties, window: Window):
        if not prop.AllUppercase:
            window['AllUppercaseUpdate'].update(button_color = ('white', 'green'))
            prop.AllUppercase = True
        else:
            window['AllUppercaseUpdate'].update(button_color = ('white', 'red'))
            prop.AllUppercase = False

    def NumbersUpdate(prop: PasswordProperties, window: Window):
        if not prop.UseNumbers:
            window['UseNumbersUpdate'].update(button_color = ('white', 'green'))
            prop.UseNumbers = True
        else:
            window['UseNumbersUpdate'].update(button_color = ('white', 'red'))
            prop.UseNumbers = False

    def SymbolsUpdate(prop: PasswordProperties, window: Window):
        if not prop.UseSymbols:
            window['UseSymbolsUpdate'].update(button_color = ('white', 'green'))
            prop.UseSymbols = True
        else:
            window['UseSymbolsUpdate'].update(button_color = ('white', 'red'))
            prop.UseSymbols = False

    def ParenthesisUpdate(prop: PasswordProperties, window: Window):
        if not prop.UseParenthesis:
            window['UseParenthesisUpdate'].update(button_color = ('white', 'green'))
            prop.UseParenthesis = True
        else:
            window['UseParenthesisUpdate'].update(button_color = ('white', 'red'))
            prop.UseParenthesis = False

    def MinusUpdate(prop: PasswordProperties, window: Window):
        if not prop.UseMinus:
            window['UseMinusUpdate'].update(button_color = ('white', 'green'))
            prop.UseMinus = True
        else:
            window['UseMinusUpdate'].update(button_color = ('white', 'red'))
            prop.UseMinus = False

    def UnderscoreUpdate(prop: PasswordProperties, window: Window):
        if not prop.UseUnderscore:
            window['UseUnderscoreUpdate'].update(button_color = ('white', 'green'))
            prop.UseUnderscore = True
        else:
            window['UseUnderscoreUpdate'].update(button_color = ('white', 'red'))
            prop.UseUnderscore = False