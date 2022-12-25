class Persona:
    def __init__(self, nom, ape, dni, tel):
        self.nombre = nom
        self.apellido = ape
        self.dni = dni
        self.tel = tel
    
    def __str__(self):
        return self.nombre + " " + self.dni