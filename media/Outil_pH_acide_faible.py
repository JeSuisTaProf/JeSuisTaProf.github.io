
# #######################################################################################################################
# OUTIL : pH D’UNE SOLUTION DE MONOACIDE FAIBLE AH (Terminale spécialité)
# Réaction avec l'eau :  AH + H2O ⇌ A- + H3O+          Ka = [A-] × [H3O+] / [AH]
# Il suffit de modifier les deux valeurs ci-dessous, puis d'exécuter le programme.
# #######################################################################################################################

import math

c = 1.0e-2          ## concentration apportée en monoacide AH (mol/L) : à modifier
pKa = 4.8           ## pKa du couple AH / A-                        : à modifier

Ka = 10 ** (-pKa)

# On note x = [H3O+] = [A-] à l'équilibre ; alors [AH] = c - x
# Ka = x² / (c - x)  conduit à l'équation du second degré :  x² + Ka × x - Ka × c = 0
x = (-Ka + math.sqrt(Ka ** 2 + 4 * Ka * c)) / 2

pH = -math.log10(x)
tau = x / c          ## taux d'avancement final

print("pH de la solution :", round(pH, 2))
print("[H3O+] = [A-] =", "{:.2e}".format(x), "mol/L")
print("[AH] =", "{:.2e}".format(c - x), "mol/L")
print("Taux d'avancement final :", round(tau * 100, 1), "%")
