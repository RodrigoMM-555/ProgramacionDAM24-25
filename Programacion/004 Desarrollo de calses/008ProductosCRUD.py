
'''
    Gestior de productos
    (c) v0.1Rodrigo Menendez Molina 2025
    Esta aplicacion gestiona productos
'''

#No se importa ninguna libreria

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

productos = []

#Presentacion
print("Programa de gestion de productos v0.1 Rodrigo Menendez Moloina")

#Menu de funcione sproncipales (Todas las empresas deben tener esto)
print("Selecciona una opcion")
print("1. Inserta un producto")
print("2. Lista de productos")
print("3. Actualizar los productos")
print("4. Eliminar los productos")

#Bucle
while True:
    #Escoge una opcion
    opcion = int(input("Escoge una opcion: "))

    #Añadir un cliente como objeto
    if opcion == 1:
        print("\nVamos a insertar un producto")
        nuevo_prducto = Producto()
        
        nuevo_prducto.nombre = input("Nombre del producto: ")
        nuevo_prducto.precio = input("Precio del producto: ")
        
        productos.append(nuevo_prducto)   
    
    #Mostrar la lista de objetos
    elif opcion == 2:
        print("\nVamos a ver los productos")
        print(productos)
        for c in productos:
            print(c.nombre,c.precio)

    #Actualizar un producto
    elif opcion == 3:
        print("\nVamos a actualizar un producto") 

    #Eliminar un producto
    elif opcion == 4:
        print("\nVamos a eliminar un producto")
        
    else:
        break
 



