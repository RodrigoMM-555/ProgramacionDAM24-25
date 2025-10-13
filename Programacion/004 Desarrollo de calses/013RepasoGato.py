

class Gato():
    def __init__(self,edad,nombre):
        self.edad = edad       #El comstructor se eejcuta si o si. Por eso la propiedades se definen dentro suyo
        self.nombre = nombre
        self.color = ""
    
    def maulla(self):           #El resto de metodos solo se ejecutan si los llamas 
        return "Maullo"

gato1 = Gato(5,"misifu")            #Al definir la clase ponemos que necesitamos definir la edad (self,edad)
print(gato1.edad)                   #y a la hora de dar la clase al objeto ponemos la edad.  
                                    #Podemos poner mas de uno,(self,edad,nombre) y el self no cuenta    
print(gato1.maulla())               #Podemos no poner una caracteristica incluso si esta definida, como el color