"""Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar
un mensaje en pantalla indicando que debe abonar impuestos."""

sueldo=int(input("Por favor ingrese el sueldo del empleado" + '\n'))

if sueldo > 3000:
    print("El empleado debe pagar impuestos" + '\n')
