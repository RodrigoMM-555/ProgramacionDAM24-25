
import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)     #En visual hay que darle el directorio

for elemento in elementos:
    print("Aechivo:",elemento)
    print(os.path.getsize(elemento)/(1024*1024),"MB")
    print(os.path.getmtime(elemento),"seegundos")