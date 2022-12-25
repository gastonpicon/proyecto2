from POO.Empleado import Empleado
from POO.Cliente import Cliente

def cargar():
    pregunta = input('va a cargar un empleado')
    nombre = input('ingrese el nombre ')
    apellido = input('ingrese el apellido ')
    dni = input('ingrese el dni ')
    telefono = input('ingrese el telefono ')

    if pregunta == "si":
        salario = input('ingrese salario ')
        empleado1 = Empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(empleado1)
    else:
        categoria = input('ingrese categoria')
        cliente1 = Cliente(nombre,apellido,dni,telefono,categoria)
        personas.append(cliente1)

personas=[]
cargar()

for persona in personas:
    print(persona)




