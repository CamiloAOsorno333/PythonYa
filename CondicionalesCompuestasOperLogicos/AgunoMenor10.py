"""Se ingresan por teclado tres números, si al menos uno de los valores ingresados es
menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor a diez"."""

n1= int(input("Ingrese el  Nro. 1= " + '\n'))
n2= int(input("Ingrese el  Nro. 2= " + '\n'))
n3= int(input("Ingrese el  Nro. 2= " + '\n'))

if n1==10 or n2==10 or n3==10:
    print("Alguno de los  tres números son iguales a 10")
else:
   print("Ni siquiera hay un número 10")