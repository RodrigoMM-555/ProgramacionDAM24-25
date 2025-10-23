
import os
import zipfile

origen =" archivos"
destino = "archivos.zip"

archivo = zipfile.ZipFile(destino,"w",zipfile.ZIP_DEFLATED)
for directorio, carpeta, archivos in os.walk(origen):
    for archiv in archivos:
        rutaarchivo = os.path.join(archivo)
        rutarelativa = os.path.relpath(rutaarchivo, origen)
        archivozip.write(rutaarchivo,rutarelativa)

    archivozip.close()

#esto comprime la carpeta archivos entera