# VERSION CORRIGÉE : exemple du couple acide éthanoïque / ion éthanoate (pKa = 4,8)
# #######################################################################################################################
# DIAGRAMME DE DISTRIBUTION D'UN COUPLE MONOACIDE / BASE CONJUGUÉE : AH / A-
# Déclaration des bibliothèques #########################################################################################

import numpy as np                      #bibliothèque maths
import matplotlib.pyplot as plt         #bibliothèque graphique

# Déclaration du pKa du couple AH / A- ----------------------------------------------------------------------------------

pKa=4.8                 ## rentrer la valeur du pKa du couple (attention : point décimal, pas de virgule)

# Valeurs du pH ---------------------------------------------------------------------------------------------------------
# linspace permet d'obtenir un tableau 1D (valeur de départ, valeur de fin, nombre d'éléments)

pH=np.linspace(0,14,200)

# Calcul des pourcentages de la forme acide AH et de la forme basique A- ------------------------------------------------
# En Python, 10 puissance x s'écrit 10**x

P_AH=100/(1+10**(pH-pKa))          ## compléter la formule permettant de calculer le pourcentage de la forme acide AH
P_A=100-P_AH                       ## compléter la formule permettant de calculer le pourcentage de la forme basique A-

# Créer le graphique qui permettra d'observer les 2 pourcentages ---------------------------------------------------------

plt.plot(pH,P_AH,"r",label='% de AH')          #Donne l'étiquette sur les axes (couleur/trait plein/pointillés ...)
plt.plot(pH,P_A,"b--",label='% de A-')

# Réglages des axes, tracer une grille et écrire les légendes sur les axes

plt.xlabel("pH",fontsize=14)
plt.ylabel("Pourcentage (%)",fontsize=14)
plt.title("Diagramme de distribution du couple AH / A-",fontsize=14)
plt.xticks(range(15))                   ## graduations de 1 en 1 sur l'axe des pH
plt.legend(loc='center right')
plt.axis([0,14,0,100])
plt.grid()
plt.show()
