#########################################################
#####   Definimos las librerías y leemos los datos  #####                    
#########################################################
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

datos=pd.read_csv("C:/Users/alber/Escritorio/Manual/bases de corneas/Cd-M1-Epitelio 10um.csv",sep=";")

#########################################################
#####             Agrupamos y promediamos           #####                    
#########################################################
agrupados=datos.groupby("Indentacion").mean()
agrupados.reset_index(inplace=True,drop=True)

#########################################################
#####   Se definen las ecuaciones de los modelos    #####                    
#########################################################
def Hertz(F,R,D):
    return (3*F*0.75)/(4*(R**(1/2))*(D**(3/2)))
# Modelo de Sneddon
def Sneddon(F,theta1,D):
    return (F*0.75*math.pi)/(2*(D**2)*(math.tan(theta1)))
# Modelo de Rico
def regular(F,theta,D):
    return (F*0.75*math.sqrt(2))/(math.tan(theta)*(D**2 ))

#########################################################
#####       Módulos de Young para cada modelo       #####                    
#########################################################
lista1=[]
lista2=[]
lista3=[]
MY1=0
MY2=0
MY3=0

anguloSneddon=30*math.pi/180
anguloRico=35*math.pi/180

for i in range(0,100):
    MY1=Hertz(agrupados.iloc[i,0],8E-9,agrupados.iloc[i,1])
    lista1.append(MY1)

for i in range(0,100):
    MY2=Sneddon(agrupados.iloc[i,0],anguloSneddon,agrupados.iloc[i,1])
    lista2.append(MY2)

for i in range(0,100):
    MY3=regular(agrupados.iloc[i,0],anguloRico,agrupados.iloc[i,1])
    lista3.append(MY3)

#########################################################
#####         Gráficas del módulo de Young          #####                    
#########################################################
plt.figure(figsize=(10,7))
plt.plot(lista1,color="red",label="Modelo de Hertz")
plt.legend()
plt.plot(lista2,color="blue",label="Modelo de Sneddon")
plt.legend()
plt.plot(lista3,color="green",label="Modelo de Rico ; b=0")
plt.legend()
plt.xlabel("Punto de la rejilla")
plt.ylabel(" $\sigma$  [Pa]")
plt.show()

#########################################################
##### Promedio de módulo de Young para cada modelo  #####                    
#########################################################
lista1a=pd.DataFrame(lista1)
lista1a.dropna()
print(f" El Modulo de Young promedio para el modelo de Hertz es: {lista1a[0].mean():.4f}")
print(f" El Modulo de Young promedio para el modelo de Sneddon es: {np.mean(lista2):.4f}")
print(f" El Modulo de Young promedio para el modelo de Rico es: {np.mean(lista3):.4f}")