#import all the stuff or bad
import string
import os
import PySimpleGUI
import random
from dataclasses import dataclass

#class for PW properties
@dataclass
class PasswordProperties:
    lenght: int = 0
    AllUppercase: bool = False
    MixedCharacters: bool = True
    value: str = ""

#create password object
password = PasswordProperties()

#input password lenght
password.lenght = int(input('Input Password lenght '))

#selection for uppercase only characters
selection:int = int(input('Select if your password has to be uppercase only (0 for mixed, 1 for uppercase only) '))
print(f'selection is {selection}')
if selection == 1:
    password.AllUppercase = True
else:
    password.AllUppercase = False
print(password.AllUppercase)

#selection for adding numbers or having letters only
selection = int(input('Select if your password will contain numbers too (0 for only letters, 1 for both) '))
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

#print it or even more pepega
print(f'Your password is: {password.value}')