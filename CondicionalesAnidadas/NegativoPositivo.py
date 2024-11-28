"""Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
el número es positivo, negativo o nulo (es decir cero"""

n=int(input("Por favor ingrese el número a analizar= " + '\n'))

if n >= 1:
    print("Positivo")
else:
    if n == 0:
        print("Nulo")
    else:
        print("Negativo")