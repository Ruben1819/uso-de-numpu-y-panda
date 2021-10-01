import numpy as np
separador=("/"*12) + "\n"
a=np.array([[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]])
print(a) 
print(type(a))
print(separador)

a[:,1] =15 
print(a)
print(separador)

a[:,1]=30
print(a)
print(separador)

#inicializacion de arreglos
print("arreglo2: 2 renglones , 4 columna")
arreglo=np.zeros(shape=(2,4),dtype=int)
print(arreglo)
print(arreglo.shape)
print(separador)

#cifras espaciadas de dos en dos
dos=np.arange(100,25,2)
print(dos)
print(dos.shape)
pass