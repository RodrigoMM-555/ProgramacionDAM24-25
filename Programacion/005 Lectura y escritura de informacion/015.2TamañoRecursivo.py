
import os

carpeta = input("Indica una carpeta: ")

grande = 1024*1024*1024                 #1 giga

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if ps.àth.getsize(ruta) > grande:
                print(ruta, os.path.getsize(ruta)/(1024/1024),"MB")
        except:
            pass                       

#Esto solo mostrara los archivos de ams de un giga
