
# #######################################################################################################################
# REPRÉSENTER UN SIGNAL PÉRIODIQUE : INFLUENCE DE L'AMPLITUDE A ET DE LA PÉRIODE T (Première spécialité)
# VERSION CORRIGÉE
# Signal sinusoïdal : y(t) = A × cos(2π t / T)
# Déclaration des bibliothèques #########################################################################################

import matplotlib.pyplot as plt
import numpy as np

# Durée observée et liste des dates -------------------------------------------------------------------------------------

t = np.linspace(0, 2, 400)      ## linspace donne 400 dates régulièrement réparties entre 0 s et 2 s

## En python dans la bibliothèque numpy :  π se tape  np.pi   et la fonction cos se tape  np.cos

# Signal de référence ---------------------------------------------------------------------------------------------------

A1 = 0.5        ## amplitude en m
T1 = 0.5        ## période en s
y1 = A1 * np.cos(2 * np.pi * t / T1)

# Même période, amplitude deux fois plus grande -------------------------------------------------------------------------

A2 = 1.0
T2 = 0.5
y2 = A2 * np.cos(2 * np.pi * t / T2)

# Même amplitude, période deux fois plus grande -------------------------------------------------------------------------

A3 = 0.5
T3 = 1.0
y3 = A3 * np.cos(2 * np.pi * t / T3)

# Affichage dans la console ---------------------------------------------------------------------------------------------

print("Signal 1 : A =", A1, "m ; T =", T1, "s ; f =", 1 / T1, "Hz")
print("Signal 2 : A =", A2, "m ; T =", T2, "s ; f =", 1 / T2, "Hz")
print("Signal 3 : A =", A3, "m ; T =", T3, "s ; f =", 1 / T3, "Hz")

# Tracé des trois signaux -----------------------------------------------------------------------------------------------

plt.figure(figsize=(10, 5))
plt.plot(t, y1, "r", label="signal 1 : A = 0,5 m ; T = 0,5 s")
plt.plot(t, y2, "b--", label="signal 2 : A = 1,0 m ; T = 0,5 s")
plt.plot(t, y3, "g:", label="signal 3 : A = 0,5 m ; T = 1,0 s")
plt.xlabel("Temps (s)", fontsize=12)
plt.ylabel("Élongation y (m)", fontsize=12)
plt.title("Influence de l'amplitude et de la période sur un signal sinusoïdal", fontsize=14)
plt.ylim(-1.3, 1.6)
plt.grid(linestyle="--")
plt.legend(loc="upper right", ncol=3, fontsize=9)
plt.show()

# Questions : quel signal a la plus grande amplitude ? la plus grande période ? la plus grande fréquence ?
#             Lire graphiquement la période de chaque signal et vérifier qu'elle correspond à la valeur choisie.
