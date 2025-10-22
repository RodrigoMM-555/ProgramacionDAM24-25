
archivo = open("mapa.txt","r")

lineas = archivo.readlines()

for linea in lineas:
    if "json" in linea:
        print("-------------------------")
        print("Encontrado!:",linea)

#Buscara un archivo que tenga en su nombre "json" y los mostrara