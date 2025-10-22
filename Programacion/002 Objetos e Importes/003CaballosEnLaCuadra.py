
''''
    Calculadora de cuadras
    v0.1 (c) 2025 Rodrigo Menendez Molina
    Programa que calcula en numero de cuadras a partir del de caballos
'''

#Importamos
import math as mat

#Datos
caballos=0
cuadras=0
caballos_por_cuadras=0

#Recivimos datos
caballos=int(input("Introduce el numero de caballos: "))
caballos_por_cuadras=int(input("Introduce el numero de caballos por cuadras: "))

#Operamos
cuadras=(caballos/caballos_por_cuadras)
cuadras=(mat.ceil(cuadras))
#cuadras=(mat.ceil(caballos/3))

#Devolvemos los datos
print("Si tienes", caballos,"caballos")
print("y te caben 3 caballos por cuadra.")
print("Necesitaras", cuadras,"cuadras")

del mat


