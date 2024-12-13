"""Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud
de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir
por pantalla la cantidad de piezas aptas que hay en el lote."""

print("Bienvenido a la fabrica de perfiles 'Doña Brava'")

x=0
rango=0
piezas = int(input("Por favor ingrese la cantidad de piezas a procesar= " + '\n'))
while x<piezas:
    longitud=float(input("Ingrese la longitud de la pieza Nro. " + str(x) + '='))
    if longitud>=1.20 and longitud<=1.30:
        rango=rango+1
    x=x+1
print("La cantidad de piezas aptas es = " + str(rango))