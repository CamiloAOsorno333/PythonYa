"""Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un
espacio en blanco es igual a " ", en cambio una cadena vacía es "" """

oracion=input("Por favor ingrese una oración or sentences para analizarla" + "\n")
x=0
espacios=0

while x<len(oracion):
    if oracion[x]==" ":
        espacios=espacios + 1
    x= x + 1
print("La oración tiene  " + str(espacios) + " espacios en blaco")

