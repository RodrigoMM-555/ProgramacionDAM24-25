
archivo = open("basededatos.txt","r")

lineas = archivo.readlines()        #En singular leera todo el documento

print(lineas)                       #Lo mostarar en forma de lista

for linea in lineas:
    print(linea)

archivo.close()