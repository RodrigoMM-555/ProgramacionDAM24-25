
archivo = open("mapa.txt","r")
busca = input("Que tipo de archivo quieres buscar: ")

lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("-------------------------")
        print("Encontrado!:",linea)

close.archivo()

#Buscara lo que le diga el ususario