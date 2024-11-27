import random

class Jatekos():

    def __init__(self, nev:str="Játékos"):
        
        self.nev = nev
        self.set_ugyesseg()
        self.eletero()
        self.szerencse()
        
    def set_ugyesseg(self):
        self.ugyesseg = random.randint(1,6) + 6
       
    
    def eletero(self):
        self.eletero = random.randint(1,6) + 12
    
    def szerencse(self):
        self.szerencse = random.randint(1,6) + 6
    
    def __str__(self):
        return f"➝ Ügyességed: {self.ugyesseg}\n ✦ ➝ Életerőd: {self.eletero} ❤️\n ➝ Szerencséd: {self.szerencse} 🍀"