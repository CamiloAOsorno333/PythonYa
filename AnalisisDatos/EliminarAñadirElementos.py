import  numpy as np

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

d=np.delete(b,0)
print("El array b quedaría así= ",d , "mira que lo convierte en un unidemensional")

d=np.delete(b,0,axis=0)
print("El array b quedaría así= ",d , "mira que le borra toda la primera fila")

d=np.delete(b,0, axis=1)
print("El array b quedaría así= ",d , "mira borra toda la primera columna ")

print('🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹🎹')

## Para añadir un elemento a un array
np.append(a,[6,7])
e=np.append(a,[6,7])
print(e)

"""## Añadir a un elemento bidireccional o 2D
eII=np.append(b,[6,7])
print(eII, "en este caso lo trae unidereccional")"""

e=np.append(b,[[10],[11]],axis=1)
print(e,"en el eje 1", "en este caso lo trae unidereccional")

