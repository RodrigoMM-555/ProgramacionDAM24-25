
class Cliente():
    def __init__(self):                             #Propiedades
        self.nombrecompleto = ""
        self.email = ""
    
    def setNombreCompleto(self,nuevoNombre):        #Setters
        self.nombrecompleto = nuevoNombre
    def setEmail(self,nuevoEmail):
        self.email = nuevoEmail
    
    def getNombreCompleto(self):                    #Getters
        return self.nombrecompleto
    def getEmail(self):
        return self.email
        
######################################################################################

clientes = []
        
#Presentacion
print("Gestor de clientes v0.1 Rodrigo Menendez Moloina")

while True:
    #Menu de funcione sproncipales (Todas las empresas deben tener esto)
    print("Selecciona una opcion")
    print("1. Inserta un nuevo cliente")
    print("2. Lista de clientes")
    opcion = int(input("Escoge una opcion(1,2): "))
    
    if opcion == 1:
        nuevoCliente = Cliente()
        print("Voy a insertar un cliente")
        nombreCliente = input("Introduce el nomnbre del cliente: ")
        nuevoCliente.setNombreCompleto(nombreCliente)
        
        emailCliente = input("Introduce el email del cliente: ")
        nuevoCliente.setEmail(emailCliente)
        
        clientes.append(nuevoCliente)
        
    elif opcion == 2:
        print("Muestro el listado de clientes")
        for cliente in clientes:
            print("--------------------------")
            print("Nombre: ",cliente.getNombreCompleto())
            print("Email: ",cliente.getEmail())
            print("--------------------------")

