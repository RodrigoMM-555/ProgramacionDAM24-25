
class Cliente():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
        
cliente = []
while True:
    
    nombre = input("Introduce el nombre del cliente: ")
    apellidos = input("Introduce los apellidos del cliente: ")
    email = input("Introduce el email del cliente: ")
    direccion = input("Itroduce la direccion del cliente: ")
    print("\n")
    
    cliente1 = Cliente(nombre,apellidos,email,direccion)







