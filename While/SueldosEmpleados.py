"""En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea
los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
Además el programa deberá informar el importe que gasta la empresa en sueldos al personal."""

print("Sueldos de los empleados")

x=0
n=int(input("Por favor ingrese la cantidad de empleados que a los que se les va a analizar lso sueldos "))
m=0
min=0
suma=0

while x<n:
    sueldo=int(input("Por favor ingrese el sueldo del empleado Nro.  " + str(x) + '='))
    suma=suma+sueldo
    if sueldo>=100 and sueldo<=300:
        m=m+1
    else:
        min=min +1
    x=x+1

print("La cantidad de empleados que ganas entre 100 y 300 es= " + str(m))
print("La cantidad de empleados que ganas entre 100 y 300 es= " + str(min))
print("El total de sueldos que debe pagar la empresa= " + str(suma))