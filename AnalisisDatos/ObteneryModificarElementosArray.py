import numpy as np

## Colum Index número de la columna desde 0

## Row Index número de la fila desde 0

a=np.array([[1,2,3] , [4,5,6], [7,8,9]])
print(a)

print(a[2,2]) ## recuerda que siempre empieza desde el cero

print(a[2,0])

## Para modificar el array
a[2,0]=24
print(a)

## Puedo acceder a rango de elementos o submatrices [:desde el inicio hasta antes del número]
a[:2,:2]
print(a[:2,:2])

## Por ejemplo para conocer desde la columna dos a la tres y fila uno a la dos
a[:2,1:3]
print(a[:2,1:3])