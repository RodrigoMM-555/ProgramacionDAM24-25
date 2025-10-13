
#Calculadora de impuestosR

'''
    Calculadora de impuestos
    v0.1 por Rodrigo Menendez
    Funcionamiento introduce una base imponible y calcula el IVA y el total    
'''

#No hay importaciones

#Variables
base_imponible=0
total_iva=0
total_factura=0

#Aqui irian funciones/clases

#Presento
print("Programa calculadora\n(C)2025 Rodrigo Menendez Molina")
print("Introduce una base imponible y calculare el IVA y total\n")

#Pido entrada
base_imponible=float(input(print("Introduce la base imponible de la factura: ")))

#Calculamos
total_iva=base_imponible*0.21
total_factura=base_imponible+total_iva

#Presento
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)





















