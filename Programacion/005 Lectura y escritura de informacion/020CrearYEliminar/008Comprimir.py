
import zipfile

origen = "miarchivo.txt"

destino = "comprimido.zip"

#De la libreria zipfile usamos el metodo ZipFile
archivo = zipfile.ZipFile(destino,"w")
archivo.write(origen)
