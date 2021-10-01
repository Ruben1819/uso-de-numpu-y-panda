import numpy as np
import random
separador =("/"*10) + "\n"
#comprobacion que una lista y un array no tiene  el mismo comportamiento
#una lista puede contener elementos de diferentes tipos de datos
#un array de numpy rosoa los elementos son del mismo dato
lista=[10,'abc',20]
print(list)
print([type(elemento)for elemento in lista])
print(separador)
#si se agrega un elemento de un dato diferente numpy integrara los elementos a neutro
arreglo=np.array([10,'abc',20])
print(arreglo)
print([type(elemento)for elemento in arreglo])
print(separador)
#una lista no ofrece operaciones de algebra matricial
lista=[20,15,20,25]
print(lista)
print(lista*2)
print(separador)

arreglo= np.array([10,15,20,25])
print(arreglo)
print(arreglo*2)
print(separador)

matriz_A=np.array([[random.randrange(300)for valor in range(10)]for valor in range (5)])
matriz_B=np.array([[random.randrange(300)for valor in range(10)]for valor in range (5)])
print(f"Matriz A \n{matriz_A}")
print("\nX\n")
print(f"Matriz B \n{matriz_B}")
print("\n=\n")
print(matriz_A*matriz_B)