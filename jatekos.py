import random

class Jatekos():

    def __init__(self, nev:str="Játékos", ugyesseg:int=0, eletero:int=0, szerencse:int=0):
        
        self.nev = nev
        self.ugyesseg = ugyesseg
        self.eletero = eletero
        self.szerencse = szerencse
        self.set_ugyesseg()
        self.set_eletero()
        self.set_szerencse()
        
    def set_ugyesseg(self):
        self.ugyesseg = random.randint(1,6) + 6
       
    
    def set_eletero(self):
        self.eletero = random.randint(1,6) + 12
    
    def set_szerencse(self):
        self.szerencse = random.randint(1,6) + 6
    
    def ketto_kockadobas_osszegadva(self):
        dobas1:int = self.set_ugyesseg()
        dobas2:int = self.set_ugyesseg()

        return dobas1 + dobas2
        
    def __str__(self):
        return f"➝ Ügyességed: {self.ugyesseg} ✦\n ➝ Életerőd: {self.eletero} ❤️\n ➝ Szerencséd: {self.szerencse} 🍀"