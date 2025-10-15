
'''
Rodrigo Menéndez Molina
factura_con_iva_descuento v0.1
Factura con IVA y descuento según precio
'''

#Constantes
IVA = 0.21
DESCUENTO = 10

#Variables pedidas al cliente
nombre_cliente = input("Dame tu nombre: ")
precio_bruto = float(input("Dame el precio bruto del producto: "))

#Calculos de IVA
iva_aplicado = precio_bruto * IVA
subtotal_con_iva = iva_aplicado + precio_bruto

#Aplicacion o no del descuento
if precio_bruto >= 50:
    total = subtotal_con_iva - DESCUENTO
    descuento_muestra = DESCUENTO
else:
    total = subtotal_con_iva
    descuento_muestra = 0

#Salida de datos
print("\n-------- Factura --------")
print("Nombre:",nombre_cliente)
print("Precio bruto:",precio_bruto,"€")
print("IVA aplicado:",iva_aplicado,"€")
print("Descuento aplicado:",descuento_muestra,"€")
print("Total",total,"€")
print("-------------------------")