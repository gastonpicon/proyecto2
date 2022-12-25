from POO.Persona import Persona

class Empleado(Persona):
    def __init__(self, nom, ape, dni, tel, sal):
        super().__init__(nom, ape, dni, tel)
        self.salario = sal