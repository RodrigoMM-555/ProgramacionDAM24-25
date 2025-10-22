import os
import zipfile

#Recuerda que lo que esta en español se puede cambiar
carpeta = "archivos"

for directorio,subcarpetas,archivos in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio,nombre_archivo)
        destino = os.path.join(directorio,nombre_archivo+".zip")
        archivo = zipfile.ZipFile(destino,"w",compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre_archivo)

#esto crea una copia comprimida de todo lo que hay en la carpeta archivos de forma separada