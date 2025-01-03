"""Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales),
 o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo."""

input("Hoy veremos que tipo de triangulo te gustan....")

l1=0
l2=0
l3=0
equilatero=0
isosceles=0
escaleno=0

n=int(input("Por favor ingresa la cantidad de triangulos que se vas a analizar= "))

for x in range (n):

    l1=int(input("Por favor ingrese el valor del primer lado  del triangulo Nro. " + str(x) + '='))
    l2=int(input("Por favor ingrese el valor del segundo lado  del triangulo Nro. " + str(x) + '='))
    l3=int(input("Por favor ingrese el valor del tercer lado  del triangulo Nro. " + str(x) + '='))

    if l1 == l2 and l1 == l3 and l2 == l3:
        equilatero= equilatero + 1
    if l1 != l2 and l1 == l3 or l1 != l3 and l3==l2 and l2 != l3:
        isosceles=isosceles+1
    if l1 != l2 and l1 != l3 and l2 != l3:
        escaleno=escaleno +1
    

input("La cantidad de triangulos equilateros es= " + str(equilatero))
input("La cantidad de triangulos isosceles es= " + str(isosceles))
input("La cantidad de triangulos escaleno es= " + str(escaleno))