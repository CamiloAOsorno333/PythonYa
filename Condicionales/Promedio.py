"""Se ingresan tres notas de un alumno, si el promedio es mayor
o igual a siete mostrar un mensaje "Promocionado"."""

n1=int(input("Por favor ingrese el Nro 1" + '\n'))
n2=int(input("Por favor ingrese el Nro 2" + '\n'))
n3=int(input("Por favor ingrese el Nro 3" + '\n'))

suma= n1 + n2 +n3
promedio= suma / 3

if promedio >= 7:
    print("Promocionado")
else:
    print("Reprobado")