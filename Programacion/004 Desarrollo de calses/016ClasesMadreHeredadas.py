
class Entidad():                        #Clase madre 1
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Animal(Entidad):                  #Clase madre 2 que tiene dentro la 1
    def __init__(self):
        super().__init__()              #Con esto traemos la clase Entidad a la clase Animal
        self.edad = 0
        self.nombre = ""
        self.raza = ""

'''
class Gato():                   #Esto seria como lo hacemos de normal 
    def __init__(self):         #Pero para no repetirlo con gatos y con perros
        self.edad = 0           #Usamos la clase madre para heredar las propiedades
        self.nombre 0 ""
        self.raza = ""
'''


class Gato(Animal):             #Añadimos Animal al definir la clase gato y perro lo que trae la clase
    def __init__(self):         #madre 1 y 2
        super().__init__()
        
class Perro(Animal):            #Lo de super trae todo lo que tenga el superior la clase madre
    def __init__(self):              #Si solo queremos heredar una cosa hya formas de hacerlo
        super().__init__()
        
        
class Roca(Entidad):
    def __init__(self):         #Queremos solamente la posicion por lo que traemos la clase madre 1
        super().__init__()           
        
        
gato1 = Gato()
print(gato1.edad)

perro1 = Perro()
print(perro1.edad)

