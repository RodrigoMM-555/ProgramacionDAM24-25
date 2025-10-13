
#Deben escrivirae con Camelcase
#Deben tener un verbo (en infinitivo o impertativo) y un objeto directo
#Deben tenre un nombre descriptivo


def diHola(nombre,edad): #Nombre y edad es la firma, lo que espera recivir la funcion
    #print("Hola",nombre,"tienes",edad,"años y yo te saludo")
    #Una funcion no deberia hacer print, deberia hacer return
    return "Hola "+nombre+" tienes "+str(edad)+" años y yo te saludo"

print(diHola("Rodrigo",19))

resultado=diHola("Paco",10)
print(resultado)

#asi deberia ser una funcion bien hecha
def calculaSuma(op1,op2):
    resultado=op1+op2
    return resultado

