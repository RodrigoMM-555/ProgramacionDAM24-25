
import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Rodrigo Menendez Molina","email1"))
clientes.append(Cliente("Roberto Ramiro Recio","email2"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close

print(clientes)