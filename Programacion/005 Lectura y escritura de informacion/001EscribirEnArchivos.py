
#Escribir
archivo = open("nombreArchivo.txt","w") #w = escribir / r = leer

archivo.write("Esto es un aprueba")

archivo.close()

#Leer
archivo = open("nombreArchivo.txt","r") #w = escribir / r = leer

linia = archivo.readline()
#Tambien puede ser readlines(), en plural

print(linia)

archivo.close()


#En visual estudio los archivos deben estar en la raiz del proyecto, la carpeta de mas afuera.