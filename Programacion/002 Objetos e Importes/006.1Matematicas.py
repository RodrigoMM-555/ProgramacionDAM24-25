
class Matematicas():
    def __inir__(self):
        self.numero = 0
    def suma(self,a,b):
        return a+b

operacion1 = Matematicas
print(operacion1.suma(4,3,4))

operacion2 = Matematicas
print(operacion2.suma(6,7,0))

#Esto e smuy lento, es un metodo dinamico que no sirve para cosas como estas