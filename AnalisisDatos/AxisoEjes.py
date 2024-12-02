import numpy as np
from numpy.testing.print_coercion_tables import print_new_cast_table

##Esto no sirve para poder eliminar y añadir elementos
# 1 D array = un eje o Axis
# 2 D array = dos ejes o Axis
# 3 D array = tres ejes o Axis

##Array unidimensional
a=np.array([1,2,3,4])
print(a)

print('🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹')


##Array bidimensional
b=np.array([[4,5,6],[7,8,9]])
print(b)

###Eliminar elementos
np.delete(a,1) ## De esta manera me crea otro elemento donde no aparezca ese elemento
print(a)

c=np.delete(a,1) ## En esta variable aparece el cambio en el array
print("a quedaría de la siguiente manera= ",c)