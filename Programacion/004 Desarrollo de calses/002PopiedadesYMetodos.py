

'''
- Propiedades - codigo que no cambia, son como 
- Metodos - codigo que puede cambiear, son como funciones

matematicas.pi      Propiedad
matematicas.ceil()  Metodo
Etsos salen de la alibreria math
'''


class Gato:
    def __init__(self):
        self.color=""                   #Esto son propiedades
        self.edad=0
    def maulla(self):
        print("El gato esta maullando") #Esto es un metodo



jagger=Gato()
jagger.color="crema"
jagger.edad=9
jagger.maulla()



lana=Gato()
lana.color="gris"
lana.edad=11
lana.maulla()



