"""Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3
y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez"""



input("Por favor ingrese los números a procesar")

x=0
m3=0
m5=0

for x in range (10):
    num=int(input("Por favor ingrese el número Nro." + str(x) + '=' ))
    if num%3==0:
        m3= m3 + 1
    else:
        if m5%5==0:
            input("Se trata de un multiplo de 5")
            m5 = m5 + 1

input("El total de los multiplos a de 5 son= " + str(m3))
input("El total de los multiplos a de 3 son= " + str(m5))