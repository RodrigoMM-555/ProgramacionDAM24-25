
#Recuerda la primera en mayuscula
class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

#Uso de la clase
cliente1 = Cliente()
cliente1.email = input("Email: ")
cliente1.nombre = input("Nombre: ")
cliente1.direccion = input("Direccion: ")

#Esto te dice donde esta el cliente en la memoria RAM
print(cliente1)

#Esto ya muestra los datos del cliente1
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)

