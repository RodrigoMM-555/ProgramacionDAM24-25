
def hazDivision(dividendo,divisor):
    
    #comprovar si son numeros
    if isinstance(dividendo, (int,float,complex)) and isinstance(divisor, (int,float,complex)): 
        #comprovar si se divide entre cero
        if divisor!=0:
            resultado=dividendo/divisor
        else:
            resultado=0
        return resultado
    else:
        #convertimos numeros en cadenas de texto a valores numerales
        try:
            dividendo=float(dividendo)
            divisor=float(divisor)
            resultado=dividendo/divisor
            return(resultado)
        except:
            return 0

#Ejemplos de error con a, "a", 0 y "3" en el divisor    
print(hazDivision(4,"3"))

