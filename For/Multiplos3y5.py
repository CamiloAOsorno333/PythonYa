"""Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3
y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez."""

input("Vamos a analizar 10 números")

n=10
m3=0
m5=0

for x in range (n):
    ns=int(input("Por favor ingrese el Nro. " + str(x) + '='))
    if ns%3==0:
        m3= m3 +1
    if ns%5==0:
        m5= m5+1
input("La cantidad de números multiplos de 3 en el listado que acabamos de analizar es  " + str(m3))
input("La cantidad de números multiplos de 5 en el listado que acabamos de analizar es  " + str(m5))





