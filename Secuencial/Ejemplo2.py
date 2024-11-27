"""Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se
 debe pagar (se ingresa un valor entero en el precio del producto)"""

producto= int(input("Por favor ingrese el precio del producto" + '\n' + '🤔'))

cantidad=int(input("Por favor ingrese la cantidad del producto" + '\n' + '🤦‍♂️'))

total=producto * cantidad

print("El total a pagar es= " , total)