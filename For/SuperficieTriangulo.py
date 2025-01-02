"""Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura
 de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12."""

#Área = (base × altura) / 2

base=0
altura=0
superficie=0
smy12=0
smen12=0

n=int(input("Cuantos datos vamos a ver=  "))

for x in range (n):
    base=int(input("Por favor ingrese el valor de la base del triangulo Nro. " + str(x) + '='))
    altura=int(input("Por favor ingrese el valor de la base del triangulos Nro. " + str(x) + '='))
    superficie= (base * altura) /2
    input(" Con respecto al Triangulo Nro. " + str(x) + '\n' + "La base es " + str(base) + '\n' +
          "La altura " + str(altura) + '\n' +
          "La superfice del Triangulo Nro. " + str(superficie))
    if superficie>12:
        smy12= smy12 +1
    if superficie<12:
        smen12= smen12 + 1

input("Los triangulos con superficie mayor a 12 son= " + str(smy12))
input("Los triangulos con superficie menores a 12 son= " + str(smen12))









