
'''
Programa contador de fabricacionde patitos
v0.1 Rodrigo Menendez Molina
El programa dira cuantos patos se gan fabricado por dia y el total
fabricados durante 25 años
'''

total=0

for año in range(2000,2026):
    for mes in range(1,13):
        for dia in range(1,31):
            total+=10
            print("Dia",dia,"del mes",mes,"del año",año,"se han fabricado 10 patitos de goma")
            print("En total se han fabricado",total,"patitos de goma")
