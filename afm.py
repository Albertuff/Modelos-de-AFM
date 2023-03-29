#########################################################
#####Definimos las librerias y leemos los datos #####
#########################################################
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
columnas=["Distancia","Indentacion","Fuerza"]


########/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-
###  NOTA: En la ubicacion del archvo se recomienda que sea en la carpeta donde tengan las bases de datos,
###        asi solamente tendrian que cambiar el nombre del archivo "archivo".csv.
###        Tambien deben revisar si su archivo esta separado por comma "," o punto y comma ";" y cambiarlo en sep="separador"
#####/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-
datos=pd.read_csv("Epitelio-10um.csv",sep=";",names=columnas)


#########################################################
#####   Agrupamos y promediamos #####
#########################################################
agrupados=datos.groupby("Indentacion").max()
agrupados.reset_index(inplace=True,drop=True)
#########################################################
#####   Se definen las ecuaciones de los modelos #####
#########################################################
# Modelo de Hertz
def Hertz(F,R,D):
    return (3*F*0.75)/(4*(R**(1/2))*(D**(3/2)))
# Modelo de Sneddon
def Sneddon(F,theta1,D):
    return (F*0.75*math.pi)/(2*(D**2)*(math.tan(theta1)))
# Modelo de Rico
def regular(F,theta,D):
    return (F*0.75*math.sqrt(2))/(math.tan(theta)*(D**2 ))
#########################################################
#####   Modulos de Young para cada modelo #####
#########################################################
lista1=[]
lista2=[]
lista3=[]
MY1=0
MY2=0
MY3=0
anguloSneddon=30*math.pi/180
anguloRico=35*math.pi/180


for i in range(0,len(agrupados)):
    MY1=Hertz(agrupados.iloc[i,1],8E-9,agrupados.iloc[i,0])
    lista1.append(MY1)
for i in range(0,len(agrupados)):
    MY2=Sneddon(agrupados.iloc[i,1],anguloSneddon,agrupados.iloc[i,0])
    lista2.append(MY2)
for i in range(0,len(agrupados)):
    MY3=regular(agrupados.iloc[i,1],anguloRico,agrupados.iloc[i,0])
    lista3.append(MY3)
#########################################################
#####   Graficas del modulo de Young #####
#########################################################
plt.figure(figsize=(10,7))
plt.plot(lista1,color="blue",linewidth=1,label="Modelo de Hertz")

plt.grid(visible=True,)
plt.legend()
# plt.plot(lista2,color="blue",label="Modelo de Sneddon")
# plt.legend()
# plt.plot(lista3,color="green",label="Modelo de Rico ; b=0")
# plt.legend()
plt.xlabel("Punto de la rejilla")
plt.ylabel(" $\sigma$ [Pa]")
plt.show()
#########################################################
##### Promedio de modulo de Young para cada modelo #####
#########################################################
lista1=pd.DataFrame(lista1)
lista1.dropna()
lista2=pd.DataFrame(lista2)
lista2.dropna()
lista3=pd.DataFrame(lista3)
lista3.dropna()

print(f"Modulo de Young promedio, modelo de Hertz: {lista1[0].mean():.4E}")
print(f"Modulo de Young promedio, modelo de Sneddon: {lista2[0].mean():.4E}")
print(f"Modulo de Young promedio, modelo de Rico: {lista3[0].mean():.4E}")