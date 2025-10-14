
'''
Rodrigo Menendez Molina
Ticket de tienda v0.1
Factura con IVA y descuentos
'''

#Constantes
IVA = 0.21


#Datos de entrada
cliente_nombre = str(input("Dame tu nombre: "))
edad = int(input("Dame tu edad: "))
base_inponible = float(input("Dame la base inponible: "))


#Seleccion de descuento segun base_inponible
if base_inponible < 100:
    descuento = 0
elif base_inponible < 199.99:
    descuento = 0.05
elif base_inponible >= 200:
    descuento = 0.1


#Calculo del descuento y aplicacion a la base imponible
importe_descuento = descuento * base_inponible
base_tras_descuento = base_inponible - importe_descuento


#Importe del IVA sobre la base_tras_descuento y su suma
importe_iva = base_tras_descuento * IVA
total_factura = base_tras_descuento + importe_iva


#Si es menor de edad o la base imponible es negativa no se imprimira el ticket
if edad < 18:
    print("Error, no puede ser menor de edad")
elif base_inponible <= 0:
    print("Error, base inponible invalida")
    

#Ticket
else:
    print("\n--------- Factura ---------")
    print("Nombre:",cliente_nombre)
    print("Edad:",edad)
    print("Base:",base_inponible,"€")
    print("Porcentaje del descuento:",descuento*100,"%")
    print("Importe del descuento:",importe_descuento,"€")
    print("Base tras descuento:",base_tras_descuento,"€")
    print("IVA:",IVA*100,"%")
    print("Importe del IVA:",importe_iva,"€")
    print("Total:",total_factura,"€")
    print("---------------------------")