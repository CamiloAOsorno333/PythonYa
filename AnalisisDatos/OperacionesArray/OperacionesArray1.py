import numpy as np

## Cambiar Forma

a=np.linspace(1,36,36)
aII=a.reshape(6,6)
print(a)
print(aII)

##Operaciones aritmeticas (suma, resta, multiplicación, división)

a1=np.array([2,3,6])
a2=np.array([4,7,9])

##suma
a1+a2
np.add(a1,a2)

##resta
a1-a2
np.subtract(a1,a2)

##multiplicacion
a1*a2
np.multiply(a1,a2)

## division
a1-a2
np.divide(a1,a2)