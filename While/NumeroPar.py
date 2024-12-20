"""Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares
y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división
de dos valores, por ejemplo 11%2 retorna un 1):"""

n=int(input("Por favor ingrese la cantidad de números a analizar= " + '\n'))
x=0
par=0
impar=0
while x<n:
    numero=(int(input("Por favor ingrese el Nro." + str(x) + '=')))

    if numero%2==0:
        input("Se trata de un número par" + '\n')
        par=par + 1
    else:
        input("Se trata de un número impar" + '\n')
        impar= impar + 1
    x = x + 1
input("El total de los números pares=  " + str(par))
input("El total de los números impares=  " + str(impar))
