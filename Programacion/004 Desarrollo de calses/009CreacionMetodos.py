
class Gato():
    def __init__(self):
        self.color = ""             #Esto es una propiedad (Sustantivo)
        
    def maulla(self):               #Esto es un metodo (Verbo)
        return "miau"
        
    def setColor(self,nuevocolor):  #Es un metodo que cambia la propiedad (Es un metodo setter)
        self.color = nuevocolor
        
    def getColor(self):              #Esto e sun metodo que muestra la propiedad
       return self.color
       
       
        
gato1 = Gato()

print(gato1.maulla())         #Llamamos a un metodo

gato1.color = "naranja"     #Seteamaos una propiedad directamente (No es buena practica)
gato1.setColor("naranja")   #Esta es una mejor preactica para setear la propiedad

print(gato1.color)          #Acceso directo, no se recomienda
print(gato1.getColor())     #Acceso por metodo, se recomienda






