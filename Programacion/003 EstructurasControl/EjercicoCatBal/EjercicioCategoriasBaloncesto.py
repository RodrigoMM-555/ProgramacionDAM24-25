
'''
Programa clasificador de baloncesto
v0.1 Rodrigo Menendez Molina
El programa clasifica categorias por edades
'''

#No hya importaciones

#Declaracion de variables
edad=0
categoria=""

#No hay funciones/clases

#Funcion principal

edad=int(input("Edad: "))

if edad<8:
    categoria="pre-mini"

elif 8>=edad<=11:
    categoria="mini"

elif 12>=edad<15:
    categoria="infantil"

elif 16>=edad<17:
    categoria="cadete"

elif 18>=edad<20:
    categoria="junior"

else:
    categoria="senior"

print("Tienes",edad,"años y tu categoria es",categoria)

if edad>40:
    print("Vetereano con experiencia")
