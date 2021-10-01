import numpy as np
separador = ("/"*15)+ "\n"

arreglo=np.array([1,2,3,4,5,6,7,8,9])
print(arreglo)
print(separador)

menores_5=arreglo[arreglo <5]
print(menores_5)
print(separador)

mayores5=arreglo[arreglo >5]
print(mayores5)
print(separador)