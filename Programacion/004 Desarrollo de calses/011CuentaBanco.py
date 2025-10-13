
limitesaldo = 1000

class cuentaBancaria():
    def __init__(self):
        self.__saldo = 0                            #Definimos que el saldo inicial en la clase es de 0
        self.__cliente = ""
        
        
        
        
    def setSaldo(self,nuevoSaldo):
        if nuevoSaldo > self.__saldo + limitesaldo:                 #Si el nuevo saldo es mayor que el saldo actual mas 
            print("Voy a avisar a la entidad de un gran ingreso")   #limitesaldo no se podra
        else:
            self.__saldo = nuevoSaldo
    def getSaldo(self):
        return self.__saldo




    def setCliente(self,nuevoCliente):
        self.__cliente = nuevoCliente
    def getCliente(self):
        return self.__cliente
    
        

    
    
    
cuentaCliente1 = cuentaBancaria()

cuentaCliente1.setSaldo(10)
print(cuentaCliente1.getSaldo())

cuentaCliente1.setSaldo(20)
print(cuentaCliente1.getSaldo())
