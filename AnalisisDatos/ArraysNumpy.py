import numpy as np

##Matriz unidimensional
a=np.array([1,2,3])
print(a)

##Matriz bidimensional
b=np.array([[1,2],[4,3]])
print(b)

##Matriz vacio multidimensional (filas por columnas)
c=np.empty([3,2])
print(c)

d=np.zeros([3,2])
print(d)

e=np.ones([3,2])
print(e)

##Matriz o Array Identity(diagonal principal repleta de un número pero tiene que se cuadrado)
f=np.identity(5)
print(f)

##Matriz o Arrays para consecutivos largos (inicio, limite, salto)
consecutivo=np.arange(1,11,0.5)
print(consecutivo)

## Arrays para consecutivos (inicio, cuantos numeros, fin), hace un vector de una sola fila
consecutivoII=np.linspace(1,10,5)
print(consecutivoII)

##Array aleatorio
aleatorio=np.random.random([3,2])
print(aleatorio)