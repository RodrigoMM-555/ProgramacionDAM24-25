
#Creamos la clase
class Cliente():
    def __init__(self):
        self.nombre = ""
        self.genreo = None
        self.edad = 0
        self.telefonos = []     #Esto es un array, una lista. Una propiedad con varios valores
        
#Creamos el objeto
cliente1 = Cliente()

#Asignamos las propiedades
cliente1.nombre = "Jose Vicente"
print("El nombre del cliente es:",cliente1.nombre)

cliente1.telefonos.append("123456789")
cliente1.telefonos.append("987654321")

print(cliente1.telefonos)
