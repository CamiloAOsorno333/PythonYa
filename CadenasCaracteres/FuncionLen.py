"""Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras
que lo componen."""

nombre= input("Ingrese un nombre por favor= ")
input("La cantidad de caracteres del nombre ingresado es=  " + str(len(nombre)))
input("El primer caracter del nombre ingresado es= " + str(nombre[0]))


"""Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre."""

nom2=input("Por favor ingrese el nombre en minuculas= ")
if nom2[0] == "a" or nom2[0] == "e" or nom2[0] == "i" or nom2[0] == "u":
    input("Se trata de un nombre que comienza con vocal")
else:
    input("Se trata de un nombre que no comienza con vocal")

"""Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@"."""

email=0
x=0
cantidad=0

email=input("Por favor ingres un nombre para procesarlo")

while x < len(email):
    if email[x]=="@":
        cantidad=cantidad + 1
    x= x +1
if cantidad==1:
    print("El email ingresado es correcto")
else:
   print("Se trata de un email invalido")