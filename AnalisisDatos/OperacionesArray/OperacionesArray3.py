import numpy as np
import numpy.linalg

## Funciones de algebra lineal

a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])

## Producto punto
np.dot(a,b)
print("el producto punto es ", np.dot)

## Producto Cruz (un producto de dos vectores)
np.cross(a,b)
print("El producto cruz", np.cross(a,b))

m=np.array([a,b,c])
print(m)

##Sublibreria linalg (para trabajar con arrays)

"""##calcular la inversa
np.linalg.inv(m)
print("La inversa", np.linalg.inv(m))"""


##calcular los autovalores
np.linalg.eigvals(m)
print("los autovalores", np.linalg.eigvals(m))

##Calcular la traza (es la suma de la diagonal principal) de la matriz
np.trace(m)
print("La traza de la matriz es ", np.trace(m))

##transponer la matriz (cambiar filas por columnas)
np.transpose(m)
print("Transponer filas por columnas", np.transpose)

"""##Para resolver el problema
    x + 2y= 3
    5x + 4y=4
"""
A=np.array([[1,3],[5,4]])
B=np.array([3,4])
np.linalg.solve(A,B)
print("La forma resolver esta ecuación es= ", np.linalg.solve(A,B))