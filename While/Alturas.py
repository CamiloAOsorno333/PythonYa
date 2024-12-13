"""Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas"""

print("Por favor ingrese las alturas para poder ser procesadas ")
x=1
n=int(input("Por favor indique cuantas alturas se van a analizar"))
promedio=0
suma=0

while x<n:
    alturas=float(input("Por favor ingrese la altura Nro. " + str(x) +'='))
    suma=suma + 1
    x=x+1

promedio= suma/n
print("El promedio de las alturas es  " + str(promedio))
