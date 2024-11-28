"""Se ingresan por teclado tres números, si todos los valores ingresados son
menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a diez"."""

n1= int(input("Ingrese el  Nro. 1= " + '\n'))
n2= int(input("Ingrese el  Nro. 2= " + '\n'))
n3= int(input("Ingrese el  Nro. 2= " + '\n'))

if n1==10 and n2==10 and n3==10:
    print("Los tres números son iguales a 10")
else:
   print("Son diferentes de 10")