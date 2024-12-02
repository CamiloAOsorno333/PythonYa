import numpy as np

a=np.array([[1,7,3,4],[2,12,4,1] , [2,9,7,8]])
print(a)

## Para filtrar [condicion concatenada con operadores logicos  & |]
a[a%2==0] ## para filtrar los números pares y los números mayores que 4
print(a[(a%2==0) & (a>4)])

print(a[(a%2==0) | (a%3==0)]) ##Para filtrar los números pares y los multiplos de 3


b=np.array([[[1,2,3,4], [3,6,9,12],[9,36,81,144]]])
b[b%2==1]
print(b[b%2==1])

f1=[1,2,3,4]
m=np.array([f1,[3*k for k in f1],[(3*k)**2 for k in f1]])
print(m)
print("El número de elementos impares es= " , m[m%2!=0].size)