import numpy as np

##los arrays tienen unas dimesnsiones y un tipo de datos (entero y flotante)

## Estos datos nos sirven para conocer los arrays y los datos para poder iterarlos

a=np.random.random([3,2])
print(a)

##saber al dimension
a.ndim
print(a.ndim)

##saber la forma
a.shape
print(a.shape)

##Saber el tamaño
a.size
print(a.size)

## saber el tipo de dato
a.dtype
print(a.dtype)