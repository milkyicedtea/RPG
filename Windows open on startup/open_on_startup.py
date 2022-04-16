import os
import winreg as reg #module to edit the windows registry

def AddToRegistry():

    #__file__ = folder where the file is being executed from
    pth = os.path.dirname(os.path.realpath(__file__))

    #name of the script
    scipt_name = 'open_on_startup.py' #edit this if you need to change the file name

    #joins file name to the end of the path
    address = os.join(pth, scipt_name)

    #key to change is HKEY_CURRENT_USER
    #key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = HKEY_CURRENT_USER
    key_value = 'Software\Microsoft\Windows\CurrentVersion\Run'

    #open the key
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)

    #modify the key
    reg.SetValueEx(open, 'any_name', 0, reg.REG_SZ, address)

    #close key
    reg.CloseKey(open)

if __name__ == '__main__':
    AddToRegistry()