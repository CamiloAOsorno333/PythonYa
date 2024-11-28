"""Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos."""

n1=int(input("Por favor ingrese el número 1" + '\n'))
n2=int(input("Por favor ingrese el número 2" + '\n'))
n3=int(input("Por favor ingrese el número 3" +'\n'))

if n1 > n2 and n1>n3:
    print("El número 1 es el mayor" , n1)
else:
    if n2 > n1 and n2 > n3:
        print("El número 2 es el mayor" , n2)
    else:
        print("El número 3 es el mayor" , n3)