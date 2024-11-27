"""
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor
al segundo informar su suma y diferencia, en caso contrario informar el producto y la división
del primero respecto al segundo.
"""
n1=int(input("Por favor ingresar el Nro. 1" + '\n'))
n2=int(input("Por favor ingresar el Nro. 2" + '\n'))

if n1 > n2:
    suma= n1 + n2
    resta= n1 - n2
    print("El total de la suma es= " , suma, '\n', "El total de la resta es= " , resta)
else:
    division= n1 // n2
    print("La divisiion del primero por el segundo es= " , division)
