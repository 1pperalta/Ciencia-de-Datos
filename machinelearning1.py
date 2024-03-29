# -*- coding: utf-8 -*-
"""MachineLearning1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KgNj308fQniRHxTu82Ay7Lui3hsjYXE

TRABAJO 1 ML- PABLO PERALTA
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('student_scores.csv')
df.head()

m= len(df)
print(m)

#GRAFICO DE DISPERSION
x = df['Hours']
y = df['Scores']

plt.scatter(x, y)

plt.xlabel('Horas')
plt.ylabel('Notas')

plt.title('Gráfico de Dispersión')
plt.show()

th0a=np.arange(-10,10,0.1)   #Arrglo 1D de th0
th1a=np.arange(-5,5,0.1)

J=np.zeros(shape=[len(th0a),len(th1a)])

i=0
j=0
for th0 in th0a:
    for th1 in th1a:
        h1=th0+th1*df["Hours"]
        J[i,j]=1/(2*m)*sum((h1-df["Scores"])**2)
        #print("th0=",th0," th1=",th1," J=",J)
        j+=1
    i+=1
    j=0

J[J>100]=100
th0m,th1m=np.meshgrid(th0a,th1a)
fig = plt.figure()
ax = Axes3D(fig)
# Crea una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crea la superficie 3D
ax.plot_surface(th0m,th1m,J.T,alpha=0.3)
ax.contour(th0m,th1m,J.T)

ax.contour(th0m, th1m, J.T, levels=20, colors='k')

# Etiqueta los ejes
ax.set_xlabel("Theta 0")
ax.set_ylabel("Theta 1")
ax.set_zlabel("J(Theta 0, Theta 1)")

plt.show()

th0=3
th1=-2
alfa=0.01
theta=np.array([th0,th1])

for i in range(2000):
   theta = theta - alfa * np.array([
        (1/m) * sum(theta[0] + theta[1] * df["Hours"] - df["Scores"]),
        (1/m) * sum((theta[0] + theta[1] * df["Hours"] - df["Scores"]) * df["Hours"])
   ])
theta

th0 = 3
th1 = -2
alfa = 0.01
theta = np.array([th0, th1])

for i in range(2000):
    theta = theta - alfa * np.array([
        (1/m) * sum(theta[0] + theta[1] * df["Hours"] - df["Scores"]),
        (1/m) * sum((theta[0] + theta[1] * df["Hours"] - df["Scores"]) * df["Hours"])
    ])

print(f"Valor final de theta0: {theta[0]}, Valor final de theta1: {theta[1]}")