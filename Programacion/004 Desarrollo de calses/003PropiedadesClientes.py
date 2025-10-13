
#Uso poco escalable para varios clientes
#estas cuatro variables a ojos del programam son independientes
cliente1_email="2@email"
cliente1_direccion="Calle2"
cliente1_nombre="A"
cliente2_apellidos="p c"

cliente2_email="2@email"
cliente2_direccion="Calle2"
cliente2_nombre="B"
cliente2_apellidos="q v"



#Mas escalable con clases
class Cliente:
    def __init__(self):
        self.email=""
        self.direccion=""
        self.apellidos=""
        self.nombre=""

#Al hacerlo asi el programa reconoce que estas propiedades pertenecen a cliente1
#Cliente1 es un objeto de clse cliente
cliente1=Cliente()
cliente1.email=""
cliente1.direccion=""
cliente1.apellidos=""
cliente1.nombre=""





























