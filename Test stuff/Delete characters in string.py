import os
from open_on_startup import OpenOnStartup

def DeleteCharacters():
    for filename in os.listdir('./Test stuff'):
        if filename == os.path.basename(__file__) and filename.endswith('.py'): #prints the current launched file
            print(filename[:-3])

Atr = OpenOnStartup(os.path.basename(__file__))
Atr.AddToRegistry()

#if __name__ == '__main__':
    #DeleteCharacters()
