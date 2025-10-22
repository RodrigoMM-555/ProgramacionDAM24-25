
import zipfile

origen = "tuarchivo.txt"

destino = "basededatos.zip"

archivo = zipfile.ZipFile(destino,"w",compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)

#Esto comprime de la misma manera que el anterior pero con otro algoritmo, o eso creo.
#al comprimir un archivo en un zip en concreto se borra lo anterior 