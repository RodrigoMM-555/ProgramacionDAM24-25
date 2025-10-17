
import os

carpeta = input("indica una carpet: ")
for directorio,carpetas,archivo in os.walk(carpeta):
    print(directorio)
    print(carpetas)
    print(archivo)