
nomA = input("Dame el nombre del dragon A: ")
edadA = input("Dame la edad del dragon A: ") 
fuerzaA = 0
resistenciaA = 0
categoriaA = ""

nomB = input("Dame el nombre del dragon B: ")
edadB = input("Dame la edad del dragon B: ")
fuerzaB = 0
resistenciaB = 0
categoriaB = ""


######################################################


try:
    edadA=int(edadA)
except:
    edadA=100
try:
    edadB=int(edadB)
except:
    edadB=100

#####################################################


if edadA<50:
    print(nomA,"es joven")
    categoriaA="joven"
elif 50<=edadA<199:
    print(nomA,"es adulto")
    categoriaA="audlto"
else:
    print(nomA,"es anciano")
    categoriaA="anciano"
    
if edadB<50:
    print(nomB,"es joven")
    categoriaB="joven"
elif 50<=edadB<199:
    print(nomB,"es adulto")
    categoriaB="adulto"
else:
    print(nomB,"es anciano")
    categoriaB="anciano"

    
#############################################################


for dia in range(1,4):
    if categoriaA=="joven":
        fuerzaA+=2
        resistenciaA+=2
    elif categoriaA=="adulto":
        fuerzaA+=1
        resistenciaA+=1
    elif categoriaA=="anciano":
        fuerzaA+=1
        resistenciaA+=1
    print("El dragon",nomA,"tiene",fuerzaA,"de fuerza y",resistenciaA,"de resistencia")
    
    if categoriaB=="joven":
        fuerzaB+=2
        resistenciaB+=2
    elif categoriaB=="adulto":
        fuerzaB+=1
        resistenciaB+=1
    elif categoriaB=="anciano":
        fuerzaB+=1
        resistenciaB+=1
    print("El dragon", nomB,"tiene",fuerzaB,"de fuerza y",resistenciaB,"de resistencia")

    print("Fin del dia",dia)

    
####################################################################



















