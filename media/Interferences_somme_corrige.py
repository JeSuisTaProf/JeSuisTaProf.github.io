
# #######################################################################################################################
# INTERFERENCES : SOMME DE DEUX SIGNAUX SINUSOIDAUX SYNCHRONES (Terminale spécialité)
# VERSION CORRIGÉE
# Déclaration des bibliothèques #########################################################################################

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#Les caractéristiques graphiques du repère xOy ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))                             ## Taille du graphique 10x5 pouce
ax.set(xlim=(0,100),ylim=(-2.2,2.2))                                      ## Valeurs des graduations des abscisses et ordonnées
plt.xlabel("Temps (µs)",fontsize=12, color='green', loc='right')               ## Légende des abscisses
plt.ylabel("Signal (unité arbitraire)",fontsize=12, color='green') ## Légende des ordonnées
ax.spines['bottom'].set_position(('data',0))                        ## Pour centrer les axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_minor_locator(MultipleLocator(5))                     ## Valeurs des sous graduations
ax.yaxis.set_minor_locator(MultipleLocator(0.1))


for tickLabel in plt.gca().xaxis.get_ticklabels():                  ## Taille des caracteres des abscisses
    tickLabel.set_fontsize(14)
for tickLabel in plt.gca().yaxis.get_ticklabels():
    tickLabel.set_fontsize(14)                                      ## Taille des caracteres des ordonnees

t=np.linspace(0,100,400)       ## linspace permet d'obtenir un tableau 1D (valeur de départ, valeur de fin, nombre d'éléments)

plt.title("Somme de deux signaux sinusoïdaux synchrones", color='r', fontsize=14)
plt.grid(linestyle="--")

# La fonction sinusoïdale -----------------------------------------------------------------------------------------------
## En python dans la bibliothèque numpy :
## π se tape :  np.pi   et l  a fonction cos(t) se tape :   np.cos(t)

A1=1            # amplitude du signal 1
A2=1            # amplitude du signal 2
T=25            # période des deux signaux en µs (même période : signaux synchrones)
phi1=0          # phase à l'origine du signal 1 en rad
phi2=0*np.pi    # déphasage du signal 2 en rad : essayer 0, 1, 2, 3, 4 fois np.pi

y1 = A1*np.cos((2*np.pi/T)*t+phi1)   ## Fonction décrivant l'onde y1
y2 = A2*np.cos((2*np.pi/T)*t+phi2)
s = y1+y2

# Les caractéristiques du tracé -----------------------------------------------------------------------------------------

plt.plot(t, y1, "r:", label='signal 1')    ## Représentation y1 = f(t), en ligne rouge en pointillés
plt.plot(t, y2, "b--", label='signal 2')
plt.plot(t, s, "g", linewidth=2, label='somme s = s1 + s2')
print("Amplitude du signal somme :", round(max(s), 2))
plt.legend()
plt.show()

