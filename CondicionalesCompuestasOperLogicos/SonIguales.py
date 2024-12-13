"""Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero
con el segundo y a este resultado se lo multiplica por el tercero."""

n1=int(input("Ingrese el primer número" + '\n'))
n2=int(input("Ingrese el segundo número" + '\n'))
n3=int(input("Ingrese el tercer número" + '\n'))

if n1==n2 and n2==n3:
    sum=(n1+n2) * n3
    print(sum)
else:
    print("Lo sentimos los números no son iguales" + '\n')