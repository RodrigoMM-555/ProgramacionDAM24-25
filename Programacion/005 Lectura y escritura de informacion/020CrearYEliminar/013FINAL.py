
'''
1. Pedir una ruta de una carpeta con input
2. Repasar todas las subcarpetas y archivos dentro de esa carpeta
3. Para cada archivo oc arpeta hay que comprimirla en un zip
4. Una vez comprimido ese zip quiero eliminar los contenidos originales
'''

import os
import zipfile
import time
import sys

ruta = input("Introduce la ruta de la carpeta: ")

# Recolectar todos los elementos (archivos + carpetas)
elementos = []
for carpeta, subcarpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        elementos.append(os.path.join(carpeta, archivo))
    for subcarpeta in subcarpetas:
        elementos.append(os.path.join(carpeta, subcarpeta))

total = len(elementos)
procesados = 0
inicio = time.time()

def mostrar_progreso(procesados, total, inicio):
    if total == 0:
        return
    porcentaje = (procesados / total) * 100
    transcurrido = time.time() - inicio
    if procesados > 0:
        tiempo_estimado = transcurrido / procesados * (total - procesados)
    else:
        tiempo_estimado = 0
    barra = int(porcentaje // 2)
    sys.stdout.write(
        f"\r[{'#' * barra}{'-' * (50 - barra)}] {porcentaje:6.2f}%  "
        f"Tiempo restante: {tiempo_estimado:6.1f}s"
    )
    sys.stdout.flush()

# Procesar cada elemento
for carpeta, subcarpetas, archivos in os.walk(ruta):
    for nombre in archivos:
        ruta_archivo = os.path.join(carpeta, nombre)
        nombre_zip = ruta_archivo + ".zip"

        with zipfile.ZipFile(nombre_zip, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(ruta_archivo, os.path.basename(ruta_archivo))

        os.remove(ruta_archivo)
        procesados += 1
        mostrar_progreso(procesados, total, inicio)

    for subcarpeta in subcarpetas:
        ruta_sub = os.path.join(carpeta, subcarpeta)
        nombre_zip = ruta_sub + ".zip"

        with zipfile.ZipFile(nombre_zip, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
            for carpeta2, _, archivos2 in os.walk(ruta_sub):
                for archivo2 in archivos2:
                    ruta_archivo2 = os.path.join(carpeta2, archivo2)
                    zipf.write(ruta_archivo2, os.path.relpath(ruta_archivo2, ruta_sub))

        for carpeta2, subcarpetas2, archivos2 in os.walk(ruta_sub, topdown=False):
            for archivo2 in archivos2:
                os.remove(os.path.join(carpeta2, archivo2))
            for sub2 in subcarpetas2:
                os.rmdir(os.path.join(carpeta2, sub2))
        os.rmdir(ruta_sub)
        procesados += 1
        mostrar_progreso(procesados, total, inicio)

print("\n✅ Proceso completado.")

