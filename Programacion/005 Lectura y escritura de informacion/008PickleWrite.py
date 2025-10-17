
import pickle

archivo = open("datos.bin","wb")            #.bin es un achivo en binario
                                            #wb es para escribir en binario
cadena = "Porondrigo"

pickle.dump(cadena,archivo)

archivo.close