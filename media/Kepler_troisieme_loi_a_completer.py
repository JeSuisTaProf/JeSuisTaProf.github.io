
# #######################################################################################################################
# TROISIÈME LOI DE KEPLER ET DONNÉES ASTRONOMIQUES (Terminale spécialité)
# VERSION À COMPLÉTER : remplacer les ... par ce qui convient, puis exécuter le programme.
# D'après le sujet de baccalauréat 2023, Métropole septembre, jour 2, exercice 3 « Mars vue sous l'œil de Kepler »
# Déclaration des bibliothèques #########################################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constantes : 1 unité astronomique, notée au (en m) et 1 année, notée an (en s) -----------------------------------------

au = 1.496*10**11
an = ...                         ## compléter : durée d'une année en secondes

# Données : Mercure, Vénus, Terre, Jupiter, Saturne, Uranus, Neptune (Mars exclue) -------------------------------------

a = np.array([0.38, 0.72, 1, 5.20, 9.54, 19.2, 30.1])            # a : demi-grand axe, exprimé en au
T = np.array([0.241, 0.615, 1, 11.86, 29.46, 84.02, 165])       # T : période de révolution, exprimée en années
am = a*au                        ## demi-grand axe en m
Ts = T*an                        ## période de révolution en s

acube = ...                      ## compléter : a³ en m³
Tcarre = ...                     ## compléter : T² en s²

# Modélisation par une fonction linéaire : T² = k × a³ ------------------------------------------------------------------

def modele(x, k):
    return k*x

k = curve_fit(modele, acube, Tcarre)[0][0]
print("Coefficient directeur k =", "{:.3e}".format(k), "s².m⁻³")

# Mars : période de révolution TMars = 687 jours ------------------------------------------------------------------------

TMars = 687*24*3600              ## période de révolution de Mars en s
aMars = ...                      ## compléter : demi-grand axe de Mars en m (T² = k × a³)
print("Demi-grand axe de Mars =", "{:.3e}".format(aMars), "m, soit", round(aMars/au, 2), "au")

# Graphique T² = f(a³) --------------------------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))      ## nouveau graphique à chaque exécution (évite une légende en double)
plt.plot(acube, Tcarre, "b+", markersize=12, label="planètes (sauf Mars)")
plt.plot(acube, modele(acube, k), "r-", label="modèle linéaire T² = k × a³")
plt.plot(aMars**3, TMars**2, "go", label="Mars")
plt.xlabel("a³ (m³)", color='green')
plt.ylabel("T² (s²)", color='green')
plt.title("Troisième loi de Kepler", color='r', fontsize=14)
plt.grid(linestyle="--")
plt.legend()
plt.show()
