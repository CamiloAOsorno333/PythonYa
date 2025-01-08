"""Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se
pide que se ingrese la cantidad de puntos a procesar."""

input("Vamos a ver las coordenadas del plano carteciano")

c1=0
c2=0
c3=0
c4=0

x=0
y=0

np=int(input("Por favor ingresa el número de puntos a procesar= "))

for f in range (np):
    x=int(input("Por favor ingrese el valor de 'X' del punto Nro. " + str(f)))
    y=int(input("Por favor ingrese el valor de 'Y' del punto Nro. " + str(f)))
    if x>=0 and y>=0:
        c1=c1 + 1
    if x<=0 and y>=0:
        c2=c2 +1
    if x<=0 and y<= 0:
        c3=c3 +1
    else:
        c4=c4 +1

input("La cantidad de puntos en el cuadrante Nro.1 = " + str(c1) )
input("La cantidad de puntos en el cuadrante Nro.2 = " + str(c2) )
input("La cantidad de puntos en el cuadrante Nro.3 = " + str(c3) )
input("La cantidad de puntos en el cuadrante Nro.4 = " + str(c4) )

