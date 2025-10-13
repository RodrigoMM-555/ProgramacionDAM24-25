# Programas de empesas se forman por:
# CRUD
# C reate
# R ead
# U pdate
# D elete

#Clase cliente
class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

print("Programa de gestion de clientes v0.1 Rodrigo Menendez Moloina")

#Menu
print("Selecciona una opcion")
print("1. Inserta cliente")
print("2. Lista clientes")
print("3. Actualizar clientes")
print("4. Eliminar clientes")

#Creo lista vacia
clientes = []

#Bucle menu
while True:                                             #Bucle infinito controlado
    opcion = int(input("Escoge una opcion: "))          #Escoge una opcion

    #Añadir un cliente como objeto
    if opcion == 1:
        print("\nVamos a insertar un cliente")
        nuevo_cliente = Cliente()
        
        nuevo_cliente.nombre = input("Nombre del cliente: ")
        nuevo_cliente.email = input("Email del cliente: ")
        nuevo_cliente.direccion = input("Direccion del cliente: ")
        
        clientes.append(nuevo_cliente)                  #Subir el cliente a la lista
    
    
    #Mostrar la lista de objetos
    elif opcion == 2:
        print("\nVamos a ver los clientes")
        for c in clientes:
            print(c.nombre, c.email, c.direccion)
    
    
    #Actualizar un cliente
    elif opcion == 3:
        print("\nVamos a actualizar un cliente")
        
        for c in clientes:
            print(c.nombre,)
        e = input("Cual quieres actualizar: ")
        n = -1
        for c in clientes:
            n += 1
            if c.nombre == e:
                print(c.nombre, c.email, c.direccion)

    #Eliminar un cliente
    elif opcion == 4:
        print("\nVamos a eliminar un cliente")
        
        for c in clientes:
            print(c.nombre,)
        e = input("Cual quieres eleminar: ")
        n = -1
        for c in clientes:
            n += 1
            if c.nombre == e:
                del clientes[n]
                

    else:
        break
        
