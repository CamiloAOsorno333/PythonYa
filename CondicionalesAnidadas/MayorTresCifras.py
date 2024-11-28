"""Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
 y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si
 el número de cifras es mayor."""

n=int(input("Por favor ingrese el número a analizar= "+ '\n'))

if n <=9:
    print("Una cifra")
else:
    if n> 9 and n <= 99:
        print("Dos cifras")
    else:
        print("Error se trata de un número de mayor cantidad de cifras")
