"""Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar
un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)"""


n1=int(input("Por favor ingrese un número del 1 al 99= "))

if n1 > 9 and n1 <99:
    print("Se trata de un número de dos digitos ")
else:
    print("Se trata de un menor de un solo digito ")


