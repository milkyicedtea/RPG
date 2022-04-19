import os
import winreg as reg #module to edit the windows registry

class OpenOnStartup:
    def __init__(self, file_path, imported_from):   #file_path = path of the file calling, imported_from = name of the file calling 
        self.path = file_path
        self.imported_from = imported_from

    #Add value to registry
    def AddToRegistry(self):
        if self.imported_from.endswith('.py'):
            imported_from = self.imported_from[:-3] #name of the file without '.py'
            print(imported_from)

        #joins file name to the end of the path
        address = os.join(self.path, self.imported_from)

        #key to change is HKEY_CURRENT_USER
        #key value is Software\Microsoft\Windows\CurrentVersion\Run
        key = reg.HKEY_CURRENT_USER
        key_value = 'Software\Microsoft\Windows\CurrentVersion\Run'

        #open the key
        open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)

        #modify the key
        reg.SetValueEx(open, self.imported_from, 0, reg.REG_SZ, address)

        #close key
        reg.CloseKey(open)

    #Delete value from registry
    def DeleteFromRegistry(self):
        if imported_from.endswith('.py'):
            imported_from = imported_from[:-3]

        self.path = os.path.dirname(os.path.realpath(__file__))

        self.script_name = imported_from

        address = os.join(self.path, self.script_name)

        key = reg.HKEY_CURRENT_USER
        key_value = 'Software\Microsoft\Windows\CurrentVersion\Run'

        open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)

        reg.DeleteValue(open, self.script_name, 0, reg.REG_SZ, address)

        reg.CloseKey