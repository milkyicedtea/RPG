import secrets

import string

#class for password "extras"
class PasswordExtra:
    symbols: str = '!@#$%&'
    parenthesis: str = r'()[]{}'
    minus: str = '-'
    underscore: str = '_'

#class for password properties
class PasswordProperties:
    def __init__(self):
        self.lenght: int = 12
        self.AllUppercase: bool = False
        self.UseNumbers: bool = False
        self.UseSymbols: bool = False
        self.UseParenthesis: bool = False
        self.UseMinus: bool = False
        self.UseUnderscore: bool = False

#class for password generation + various checks
class PasswordGen:
    def __init__(self, prop: PasswordProperties) -> None:
        self.prop = prop
        self.value: str = ''

    def getCharacters(self):
        # usable letters check
        if self.prop.AllUppercase:
            usable_characters = string.ascii_uppercase
        else:
            usable_characters = string.ascii_letters

        # usable numbers
        if self.prop.UseNumbers:
            usable_characters += string.digits

        # usable symbols
        if self.prop.UseSymbols:
            usable_characters += PasswordExtra.symbols

        # usable parenthesis
        if self.prop.UseParenthesis:
            usable_characters += PasswordExtra.parenthesis

        #usable minus
        if self.prop.UseMinus:
            usable_characters += PasswordExtra.minus

        #usable underscore
        if self.prop.UseUnderscore:
            usable_characters += PasswordExtra.underscore

        return usable_characters

    def generate(self, usable_characters:str):
        for x in range(self.prop.lenght):
            self.value = self.value + secrets.choice(usable_characters)

    def checkAllUpperCase(self) -> bool:
        if not self.prop.AllUppercase:
            return True
        
        return self.value.isupper()
                
    def checkNumbers(self) -> bool:
        if not self.prop.UseNumbers:
            return True
        
        else:
            f_res = False
            for lenght in range(self.prop.lenght):
                for numbers in range(len(string.digits)):
                    if self.value[lenght] == string.digits[numbers]:
                        f_res = True
                        break

        #print(f'checkNumbers is {f_res}')
        return f_res
    
    def checkSymbols(self) -> bool:
        if not self.prop.UseSymbols:
            return True

        else:
            f_res = False
            for lenght in range(self.prop.lenght):
                for symbols in range(len(PasswordExtra.symbols)):
                    if self.value[lenght] == PasswordExtra.symbols[symbols]:
                        f_res = True
                        break
        
        #print(f'checkSymbols is {f_res}')
        return f_res
    
    def checkParenthesis(self) -> bool:
        if not self.prop.UseParenthesis:
            return True
        
        else:
            f_res = False
            for lenght in range(self.prop.lenght):
                for parenthesis in range(len(PasswordExtra.parenthesis)):
                    if self.value[lenght] == PasswordExtra.parenthesis[parenthesis]:
                        f_res = True
                        break
        
        #print(f'checkParenthesis is {f_res}')
        return f_res
    
    def checkMinus(self) -> bool:
        if not self.prop.UseMinus:
            return True
        
        else:
            f_res = False
            for lenght in range(self.prop.lenght):
                if self.value[lenght] == PasswordExtra.minus:
                    f_res = True
                    break
        #print(f'checkMinus is {f_res}')
        return f_res
    
    def checkUnderscore(self) -> bool:
        if not self.prop.UseUnderscore:
                return True
            
        else:
            f_res = False
            for lenght in range(self.prop.lenght):
                if self.value[lenght] == PasswordExtra.underscore:
                    f_res = True
                    break
            #print(f'checkMinus is {f_res}')
        return f_res
    
    def checksResult(self) -> bool:
        return self.checkAllUpperCase() and self.checkNumbers() and self.checkParenthesis() and \
            self.checkSymbols() and self.checkMinus() and self.checkUnderscore()