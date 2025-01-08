"""Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor."""

input("Vamosa a ver como estan nuestros estudiantes")

edmanana=0
edtarde=0
ednoche=0
sumaman=0
sumatar=0
sumanoch=0
promedioman=0
promediotar=0
promedionoch=0

for x in range (1):
    input("Ingrese las edades de los alumnos de la mañana")
    for f in range (5):
        edmanana=int(input("Por favor ingrese la edad del alumno Nro. " + str(f) + "= "))
        sumaman=sumaman + edmanana
    input("Ingrese las edades de los alumnos de la tarde")
    for g in range (6):
        edtarde=int(input("Por favor ingrese la edad del alumno Nro. " + str(g) + "= "))
        sumatar=sumatar + edtarde
    input("Ingrese las edades de los alumnos de la noche")
    for h in range (11):
        ednoche=int(input("Por ingrese la edad del alumuno Nro. " + str(h) + "= "))
        sumanoch= sumanoch + ednoche



promedioman= sumaman / 5
promediotar= sumatar / 6
promedionoch= sumanoch / 11

input("El promedio de las edades de los alumnos de la mañana es= " + str(promedioman))
input("El promedio de las edades de los alumnos de la tarde es= " + str(promediotar))
input("El promedio de las edades de los alumnos de la noche es= " + str(promedionoch))

if promedioman > promediotar and promedioman > promedionoch:
    input("La jornada con mayor promedio es la de la mañana con= " + str(promedioman) )
elif promediotar > promedioman and promediotar > promedionoch:
    input("La jornada con mayor promedio es la de la tarde con= " + str(promediotar))
else:
    input("La jornada con mayor promedio es la de la noche con= " + str(promedionoch))