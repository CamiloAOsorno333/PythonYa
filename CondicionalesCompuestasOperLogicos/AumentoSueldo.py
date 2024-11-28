"""De un operario se conoce su sueldo y los años de antigüedad.
Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle
un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios."""

sueldo=int(input("Por favor ingrese el sueldo= " + '\n'))
antiguedad=int(input("Por favor ingrese los años de antiguedad= " + '\n'))


if sueldo<= 500 and antiguedad>=10:
    print("20% de aumento y su sueldo quedaría en= ", sueldo +(sueldo * .020) )
else:
    if sueldo<=500 and antiguedad<=10:
        print("5% de aumento y su sueldo quedaría en= ", sueldo +(sueldo * .05))
    else:
        print("No amerita aumento, sigue trabajando y quedate en la empresa")