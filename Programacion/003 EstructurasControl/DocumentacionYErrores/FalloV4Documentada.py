
def hazDivision(dividendo,divisor):
    
    #docstring de documentacion
    '''
    FUncion de division
    Entradas: Dividendo y divisior que se esperan que sean numericas
    Salidas: Resultado de la division con numero(o cero si hay fallo)
    Capturas de error:
        1. Si es numerico
        2. Si se puede convertir a numero
        3. Si no es division entre cero
    '''
    
    #comprovar si son numeros
    print("entramos la funcion")
    if isinstance(dividendo, (int,float,complex)) and isinstance(divisor, (int,float,complex)):
        
        print("parece que los paramentros son numeros")
        #comprovar si se divide entre cero
        
        if divisor!=0:
            print("parece que los puedo dividir")
            resultado=dividendo/divisor
        else:
            print("No puedo dividir porque el divisor es 0")
            resultado=0
        return resultado
    
    else:
        
        print("Los parametros no son numeros, voy a intentar convertirlos")
        #convertimos numeros en cadenas de texto a valores numerales
        
        try:
            print("Intento convertirlos en numeros")
            dividendo=float(dividendo)
            divisor=float(divisor)
            resultado=dividendo/divisor
            return resultado
        except:
            print("No he podido convertirlo a numeros")
            return 0

#Ejemplos de error con a, "a", 0 y "3" en el divisor    
print(hazDivision(4,"3"))

