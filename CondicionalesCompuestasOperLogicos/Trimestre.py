"""Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde
al primer trimestre del año (enero, febrero o marzo) Cargar por teclado el valor
numérico del día, mes y año.
Ejemplo: dia:10 mes:2 año:2018"""

fecha= int(input("Ingrese el día= " + '\n'))
mes= int(input("Ingrese el mes= " + '\n'))
ano= int(input("Ingrese el año= " + '\n'))

if mes==1 or mes==2 or mes==3:
    print("Primer semestre")
else:
    if mes == 4 or mes == 5 or mes == 6:
        print("Segundo semestre")
    else:
        print("Tercer semestre")






