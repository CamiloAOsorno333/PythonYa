"""Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o
iguales a 7 y cuántos menores."""

input("Por favor ingrese las notas de los estudiantes")

n=10
x=0
notas=0
mayores=0
menores=0

for x in range (10):
    notas=float(input("Por favor ingrese la nota Nro." + str(x) + '= '))
    if notas>=7:
        mayores=mayores + 1
    else:
        menores= menores + 1

print("El total de las notas iguales o superiores a 7 es= " + str(mayores))
print("El total de las notas menores a 7 es= " + str(menores))

