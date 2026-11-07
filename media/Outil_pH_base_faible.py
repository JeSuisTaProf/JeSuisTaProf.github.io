
# #######################################################################################################################
# OUTIL : pH D’UNE SOLUTION DE MONOBASE FAIBLE A- (Terminale spécialité)
# Réaction avec l'eau :  A- + H2O ⇌ AH + HO-          Ke = [H3O+] × [HO-] = 1,0×10^-14 à 25 °C
# Il suffit de modifier les deux valeurs ci-dessous, puis d'exécuter le programme.
# #######################################################################################################################

import math

c = 1.0e-2          ## concentration apportée en monobase A- (mol/L) : à modifier
pKa = 9.2           ## pKa du couple AH / A-                        : à modifier

Ka = 10 ** (-pKa)
Ke = 1.0e-14
Kb = Ke / Ka         ## constante de la réaction de la base avec l'eau

# On note x = [HO-] = [AH] à l'équilibre ; alors [A-] = c - x
# Kb = x² / (c - x)  conduit à l'équation du second degré :  x² + Kb × x - Kb × c = 0
x = (-Kb + math.sqrt(Kb ** 2 + 4 * Kb * c)) / 2

H3O = Ke / x         ## [H3O+] déduit du produit ionique de l'eau
pH = -math.log10(H3O)
tau = x / c          ## taux d'avancement final

print("pH de la solution :", round(pH, 2))
print("[HO-] = [AH] =", "{:.2e}".format(x), "mol/L")
print("[A-] =", "{:.2e}".format(c - x), "mol/L")
print("[H3O+] =", "{:.2e}".format(H3O), "mol/L")
print("Taux d'avancement final :", round(tau * 100, 1), "%")
