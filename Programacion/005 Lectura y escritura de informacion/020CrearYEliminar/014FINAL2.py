
#Este programa no lo entiendo

import os
import zipfile
import time
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

def comprimir():
    ruta = filedialog.askdirectory(title="Selecciona una carpeta para comprimir")
    if not ruta:
        return

    borrar = var_borrar.get()
    elementos = []
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            elementos.append(os.path.join(carpeta, archivo))
        for subcarpeta in subcarpetas:
            elementos.append(os.path.join(carpeta, subcarpeta))

    total = len(elementos)
    if total == 0:
        messagebox.showinfo("Aviso", "No hay archivos ni carpetas en esa ruta.")
        return

    progreso["maximum"] = total
    progreso["value"] = 0
    ventana.update()

    inicio = time.time()
    procesados = 0

    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for nombre in archivos:
            ruta_archivo = os.path.join(carpeta, nombre)
            nombre_zip = ruta_archivo + ".zip"

            with zipfile.ZipFile(nombre_zip, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(ruta_archivo, os.path.basename(ruta_archivo))

            if borrar:
                os.remove(ruta_archivo)

            procesados += 1
            progreso["value"] = procesados
            porcentaje = (procesados / total) * 100
            label_estado.config(text=f"{porcentaje:.1f}% completado")
            ventana.update_idletasks()

        for subcarpeta in subcarpetas:
            ruta_sub = os.path.join(carpeta, subcarpeta)
            nombre_zip = ruta_sub + ".zip"

            with zipfile.ZipFile(nombre_zip, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                for carpeta2, _, archivos2 in os.walk(ruta_sub):
                    for archivo2 in archivos2:
                        ruta_archivo2 = os.path.join(carpeta2, archivo2)
                        zipf.write(ruta_archivo2, os.path.relpath(ruta_archivo2, ruta_sub))

            if borrar:
                for carpeta2, subcarpetas2, archivos2 in os.walk(ruta_sub, topdown=False):
                    for archivo2 in archivos2:
                        os.remove(os.path.join(carpeta2, archivo2))
                    for sub2 in subcarpetas2:
                        os.rmdir(os.path.join(carpeta2, sub2))
                os.rmdir(ruta_sub)

            procesados += 1
            progreso["value"] = procesados
            porcentaje = (procesados / total) * 100
            label_estado.config(text=f"{porcentaje:.1f}% completado")
            ventana.update_idletasks()

    tiempo_total = time.time() - inicio
    messagebox.showinfo("Completado", f"Proceso terminado en {tiempo_total:.1f} segundos.")
    label_estado.config(text="✅ Proceso completado.")


# ---- Interfaz ----
ventana = tk.Tk()
ventana.title("Compresor con Control de Borrado")
ventana.geometry("400x200")

btn_seleccionar = tk.Button(ventana, text="Seleccionar carpeta y comprimir", command=comprimir)
btn_seleccionar.pack(pady=15)

var_borrar = tk.BooleanVar()
chk_borrar = tk.Checkbutton(ventana, text="Borrar archivos originales después de comprimir", variable=var_borrar)
chk_borrar.pack()

progreso = ttk.Progressbar(ventana, length=300, mode="determinate")
progreso.pack(pady=15)

label_estado = tk.Label(ventana, text="Esperando acción...")
label_estado.pack()

ventana.mainloop()
