import numpy as np
import pandas as pd
sep = ("/"*15) + "\n"

#aqui creamos una serie con sus valores iniciales
notas=pd.Series([87,100,85,60,78])
#print(type(notas))
#print(notas)
#print(sep)

#creamos una serie con 6 elementos con el mismo valor
#igual=pd.Series(100,range(6))
#print(type(igual))
#print(igual)
#print(sep)

#estadisticas descriptivas para una serie
print("Notas :")
print(f"{notas}")
print(f"Cantidad = {notas.count()}")
print(f"Media = {notas.mean()}")
print(f"Minimo = {notas.min()}")
print(f"Maximo = {notas.max()}")
print(f"Desviacion estandar = {notas.std()}")
print("Sumarizacion descriptiva: ")
print(notas.describe())
print(sep)

#serie con indices personalizados
print("Series con indices personalizados: ")
notas_asig =pd.Series([87,100,85,60,78], index=["Crescencio","Domitila","Rutilio","Panfilo","Ruben"])
print(notas_asig)
print(sep)

print("Serie generada a partir de un diccionario: ")
notas_asig_dic = pd.Series({"Crescencio":87,"Domitila":100,"Rutilio":85,"Panfilo":60,"Ruben":78})
print(notas_asig_dic)
print(sep)

#Acceso a elementos es una serie por valor de Indice
print(f"La calificacion de Rutilio es {notas_asig_dic}[Rutilio])")
print(f"La calificacion de Rutilio es de {notas_asig_dic.Rutilio}")