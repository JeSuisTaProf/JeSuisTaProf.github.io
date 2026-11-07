
# #######################################################################################################################
# MODELISER UNE ONDE A 1 DIMENSION
# VERSION CORRIGÉE
# Déclaration des bibliothèques #########################################################################################

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#Les caractéristiques graphiques du repère xOy ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))                             ## Taille du graphique 10x5 pouce
ax.set(xlim=(0,2),ylim=(-1,1))                                      ## Valeurs des graduations des abscisses et ordonnées
plt.xlabel("Temps en (s)",fontsize=12, color='green')               ## Légende des abscisses
plt.ylabel("Amplitude de l'onde en (m)",fontsize=12, color='green') ## Légende des ordonnées
ax.spines['bottom'].set_position(('data',0))                        ## Pour centrer les axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_minor_locator(MultipleLocator(0.05))                   ## Valeurs des sous graduations
ax.yaxis.set_minor_locator(MultipleLocator(0.05))


for tickLabel in plt.gca().xaxis.get_ticklabels():                  ## Taille des caracteres des abscisses
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().yaxis.get_ticklabels():
    tickLabel.set_fontsize(14)                                      ## Taille des caracteres des ordonnees

t=np.linspace(0,2,200)     ## linspace permet d'obtenir un tableau 1D (valeur de départ, valeur de fin, nombre d'éléments)

plt.title("Représentation temporelle d'une onde sinusoïdale", color='r', fontsize=14)
plt.grid(linestyle="--")

# La fonction sinusoïdale -----------------------------------------------------------------------------------------------
## En python dans la bibliothèque numpy :
## π se tape :  np.pi   et l  a fonction cos(t) se tape :   np.cos(t)

A1=0.25         # amplitude de l'onde en m
A2=0.5
T=0.5           # période de l'onde en s
phi1=0          # phase à l"origine en rad
phi2=np.pi

y1 = A1*np.cos((2*np.pi/T)*t+phi1)   ## Fonction décrivant l'onde y1
y2 = A2*np.cos((2*np.pi/T)*t+phi2)
s = y1+y2

# Les caractéristiques du tracé -----------------------------------------------------------------------------------------

plt.plot(t, y1, "r:", label='onde y1')    ## Représentation y1 = f(t), en ligne rouge en pointillés
plt.plot(t, y2, "b:", label='y2')
plt.plot(t, s, "g", label='s')
plt.legend()
plt.show()

