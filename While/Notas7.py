"""Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores
o iguales a 7 y cuántos menores."""

print("Por favor ingrese 10 notas correspondientes al semestre")

x=0
mayores=0
menores=0

while x<10:
    notas=int(input("Por favor ingrese la Nota Nro. " + str(x) + '=' ))
    if notas>=7:
        mayores= mayores +1
    else:
        menores= menores + 1

    x=x+1

print("El total de notas mayores e iguales a 7 es= " + str(mayores))
print("El total de notas menores a 7 es= " + str(menores))