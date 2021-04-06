import numpy as np
import matplotlib.pyplot as plt
# variation du temps en entre tous les points
dt = 0.04
x = np.array([0.003,0.141,0.275,0.410,
            0.554,0.686,0.820,0.958,
            1.089,1.227,1.359,1.490
            ,1.599,1.705,1.801])

y = np.array([0.746,0.990,1.175,1.336,1.432,
            1.505,1.528,1.505,1.454,
            1.355,1.207,1.018,0.797,
            0.544,0.266])

# Calculs de composantes Vx et Vy des vecteurs vitesses
N = len(x)
# Initialisation de v0 
vx = np.zeros(N)
vy = np.zeros(N)
# Calcul du vecteur vitesse sur les axe x et y pour chacuqe points du mouvement via la formule : vi = mi+1-mi-1/ti+1-ti-1
for i in range(1,N-1):
    vx[i]=(x[i+1]-x[i-1])/(2*dt)
    vy[i]=(y[i+1]-y[i-1])/(2*dt)
#  Calcul des vitesses par la formule : v = R(vx²+vy²)
v = np.sqrt(vx**2+vy**2)

# Tracage des vecteurs 
plt.plot(x,y,'.',color='blue')
plt.xlabel('x (m)')
plt.xlim(0,2)
plt.ylabel('y (m)')
plt.ylim(0,2)
plt.title("Trajectoire du système")
# Affichage des vecteurs en chaque point (sauf 0 et 14 puisque le vecteur vitesse est nul)
plt.quiver(x,y,vx,vy,angles='xy',scale_units='xy',scale=10,color='red', width=0.005)
# Affichages des numéros des points et du calcul de la vitesse dans la console
for i in range(1,N-1):
    plt.annotate(i,(x[i]-0.05,y[i]-0.15))
    print(f"Points n°{i} |t=>|t V = {round(v[i],2)}, m/s")
# Affichage du graphique
plt.show()