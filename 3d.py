import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
matplotlib.use('TkAgg')

def moinsdix(tab):
    z = tab
    for i in range(len(z)):
        z[i]-=10
        if z[i]<0:
            z[i]=0

    return z_pos

def f1(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=-10*i+(150-t*10)
        if tab[i]<0:
            tab[i]=0
    return current_tab

def f2(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=10*i+(-150+t*10)
        if tab[i]<0:
            tab[i]=0
    return current_tab

def f2bis(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=10*i-(t*10)
        if tab[i]<0:
            tab[i]=0
    return current_tab

def f3(t,tab,t_total):
    current_tab = tab
    for i in range(len(tab)):
        tab[i]=abs(10*i-70)-70+t*10
        if tab[i]<0:
            tab[i]=0
    return current_tab
# Génération de données aléatoires pour l'histogramme
data = np.random.rand(15)

# Création du figure et du plan 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_ylim(0,15)
ax.set_zlim(0,150)
# Paramètres pour la position des barres
x_pos = np.arange(len(data))
y_pos = np.zeros(len(data))
z_pos = np.zeros(len(data))

# Paramètres pour les dimensions des barres
dx = np.ones(len(data))
dy = np.ones(len(data))
dz = data

x = [i for i in range(15)]
y= [1 for i in range(15)]
z = [0 for i in range(15)]

functions = [f1, f2, f2bis, f3]
for func in functions:
    for i in range(15):
        z = func(i,z,15)
        y = z
        ax.cla()
        ax.set_ylim(0,15)
        ax.set_zlim(0,150)
        for j in range(16):
            ax.bar3d(x_pos, y_pos+j, z_pos, dx, dy,z,color='blue')
        plt.pause(0.5)

# Affichage de l'histogramme
plt.show()
