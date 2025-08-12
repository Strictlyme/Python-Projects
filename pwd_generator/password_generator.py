import string; from random import choice; from colorama import Fore as c
class PwdGenerator:
    def __init__(self):
        self.characters = string.ascii_letters+string.digits+string.punctuation
        self.characters = self.characters.replace("'","")
        self.characters = self.characters.replace("`","")
        self.characters = self.characters.replace('"',"")
        self.running = True
    def generate(self, length: int):
        self.length = length
        if self.length <= 8 or self.length >= 200:
            print(c.RED+'Password length should be in the range of 8-199.'+c.RESET)
        else:
            self.password = ''.join(choice(self.characters) for _ in range(self.length))
            print('Password: '+c.GREEN+str(self.password)+c.RESET)
            print(c.MAGENTA+'Do you wish to save the password in a text file(y/n)?'+c.RESET)
            while self.running:
                self.choice = str(input('-> '))
                if self.choice.lower() == 'y':
                    self.savePwd()
                    self.running = False
                elif self.choice.lower() == 'n':
                    self.running = False
                else:
                    print(c.RED+'Invalid choice.'+c.RESET)
                    continue
    def savePwd(self):
        with open('pwd.txt', 'a+') as pwd_file:
            pwd_file.write('\n'+str(self.password))
pwdgen = PwdGenerator()
pwdgen.generate(28)