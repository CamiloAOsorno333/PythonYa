"""Confeccionar un programa que lea por teclado tres números enteros distintos
y nos muestre el mayor."""

#  and y or

n1=int(input("Por favor ingresar el Nro. 1" + '\n'))
n2=int(input("Por favor ingresar el Nro. 2" + '\n'))
n3=int(input("Por favor ingresar el Nro. 3" + '\n'))


if n1 > n2 and n1 > n3:
    print("El número 1 es mayor= " , n1)
else:
    if n2 > n1 and n2>n3:
        print("El número 2 es el mayor= " , n2)
    else:
        print("El número 3 es el mayor= " , n3)