
import pickle

archivo = open("datos.bin","rb")            #.bin es un achivo en binario
                                            #rb es para leer en binario
cadena = pickle.load(archivo)
print(cadena)

archivo.close