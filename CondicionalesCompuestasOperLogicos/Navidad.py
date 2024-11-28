"""Realizar un programa que pida cargar una fecha cualquiera,
luego verificar si dicha fecha corresponde a Navidad."""

dia= int(input("Ingrese el día= " + '\n'))
mes= int(input("Ingrese el mes= " + '\n'))
ano= int(input("Ingrese el año= " + '\n'))

if dia==25 and mes==12 or mes==3:
    print("Es Navidad ha nacido Dios")
else:
    print("No es Navidad")