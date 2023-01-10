#class for password "extras"
class PasswordExtra:
    symbols:str = '!@#$%&'
    parenthesis:str = r'()[]{}'


#class for password properties
class PasswordProperties:
    def __init__(self):
        self.lenght: int = 12
        self.AllUppercase: bool = False
        self.UseNumbers: bool = False
        self.UseSymbols: bool = False
        self.UseParenthesis:bool = False