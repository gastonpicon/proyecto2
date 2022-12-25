from POO.Persona import Persona

class Cliente(Persona):
    def __init__(self, nom, ape, dni, tel, cat):
        super().__init__(nom, ape, dni, tel)
        self.categoria = cat