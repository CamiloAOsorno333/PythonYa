import numpy as np

##Funciones matematicas

## cubo --en los parametros el array y la potencia a la que se va a elevar
m=np.array([1,2,3,4])
np.power(m,3)
print("cubo",np.power(m,3))


## Logaritmo natural
np.log(m)
print("Logaritmo nataural", np.log(m))

## raiz cuadrada de lo elementos de la matriz
np.sqrt(m)
print("raiz cuadrada", np.sqrt(m))

##Funciona trignometricas (los valores estan en radianes)
##seno
np.sin(m)
print("seno", np.sin(m))

## coseno
np.cos(m)
print("coseno", np.cos(m))

##tangente
np.tan(m)
print("tangente", np.tan(m))


print( "\n","🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹","\n")

##Operaciones estadisticas

r=np.random.random([5])

## La media
np.mean(r)
print("La media de los elementos de la matriz o array", np.mean(r))

##La mediana
np.median(r)
print("La mediana", np.median(m))

## La standar
np.std(r)
print("La standar", np.std(r))

## El maximo
np.max(r)
print("El maximo", np.max(r))

## El minimio
np.min(r)
print("El manimo", np.max(r))

