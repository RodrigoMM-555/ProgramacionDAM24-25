import datetime as fecha

hoy=fecha.date(2025,9,11)
print(hoy)

print(hoy.year)
print(hoy.month)
print(hoy.day)

diadelasemana=hoy.weekday()
print("\n",diadelasemana)

diadelasemana=hoy.isoweekday()
print("\n",diadelasemana)