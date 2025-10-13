
while True:
    print("Dime lo que quieres hacer: ")
    print("1. Introducir un nuevo contacto")
    print("2. Leer todos los contactos")
    opcion = int(input("Escoge una opcion: "))
    print("\n")

    if opcion == 1:
        nombre = input("Nombre del contacto: ")
        email = input("Email del contacto: ")
        archivo = open("018Agenda.txt","a")
        archivo.write(nombre + "," + email + "\n")
        archivo.close()
        print("\n")
        
    elif opcion == 2:
        archivo = open("018Agenda.txt","r")
        lineas = archivo.readlines()
        for linia in lineas:
            print(linia)
        archivo.close()
        
 