"""Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados."""

input("Por favor ingrese 10 valores para analizar" + '\n')
suma=0

for x in range (10):
    ns=int(input("Por favor ingrese el Nro. " + str(x) + '='))
    if x>=5:
        suma=suma + ns

input("El resultado de la suma de los cinco últimos números ingresados es= " + str(suma))