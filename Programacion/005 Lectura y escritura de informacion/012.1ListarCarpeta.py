
import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)     #En visual hay que darle el directorio

for elemento in elementos:
    print(elemento)
    print(os.path.getsize(elemento),"bytes")
    print(os.path.getmtime(elemento),"seegundos")