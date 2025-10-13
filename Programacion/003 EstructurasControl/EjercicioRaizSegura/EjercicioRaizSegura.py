
def hazRaiz(numero):
    
    '''
    Funcion de raiz
    Entradas: Valor que se espera que sea numerico
    Salidas: Resultado de la raiz con numero (o cero si hay fallo)
    Capturas de error:
        1. Si es numerico
        2. Si se puede convertir a numero
        3. Si no es menor que cero
    '''
    
    import math as mates
    #comprovar si son numeros
    print("Entramos los datos a la funcion")
    
    if isinstance(numero, (int,float,complex)):
        print("Parece que el paramentro es numerico")
        #comprovaremos si es mayor o igal que cero
        
        if numero>=0:
            print("Se puede hacer la raiz")
            resultado=mates.sqrt(numero)
        else:
            print("No puedo hacer la raiz porque es negativo")
            resultado=0
        return resultado
    
    else:
        
        print("El parametro no es un numero, voy a intentar convertirlo")
        #convertimos numeros en cadenas de texto a valores numerales
        
        try:
            print("Intento convertirlo en un numero")
            numero=float(numero)
            resultado=mates.sqrt(numero)
            return resultado
        except:
            print("No he podido convertirlo a numero")
            return 0

#Ejemplos de error con "a", 0 y "3" en el divisor    
print(hazRaiz("a"))
