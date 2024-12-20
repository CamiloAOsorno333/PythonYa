"""Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de
las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo."""

print("Por favor ingrese los números en las dos listas")

x=0
l2=0
l3=0
suma1=0
suma2=0
promedio=0



while x<15:

    lista1=int(input("Lista 1 🤔" + "Por favor ingrese el valor Nro. " + str(x) + '='))
    l1=lista1+1
    suma1=suma1 + lista1
    lista2=int(input("Lista 2 🤔" +"Por favor ingrese el valor Nro. " + str(x) + '='))
    l2=lista2+1
    suma2 = suma2 + lista1
    x=x+1

if l1>l2:
    input("Lista 1 mayor, con un total de=  " + str(suma1))
else:
    if l2>l1:
        input("Lista 2 mayor, con un totar de=  " + str(suma2) )
    else:
        input("Listas iguales")


