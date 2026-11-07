
# #######################################################################################################################
# BILAN ÉNERGÉTIQUE D'UN SYSTÈME EN MOUVEMENT (Première spécialité)
# VERSION CORRIGÉE
# Calcul de l'énergie cinétique Ec, de l'énergie potentielle de pesanteur Epp et de l'énergie mécanique Em = Ec + Epp
# Exemple : balle lancée en l'air (pointage d'une vidéo)
# Déclaration des bibliothèques #########################################################################################

import matplotlib.pyplot as plt         # bibliothèque pour tracer les graphiques

# Données du pointage de la vidéo ---------------------------------------------------------------------------------------
## Valeurs d'exemple : remplacer par les valeurs de votre pointage (copier-coller depuis Regressi ou Aviméca)

tau = 0.040        ## durée entre deux images en s
m = 0.0451         ## masse de la balle en kg
g = 9.81           ## intensité de la pesanteur en N/kg

x = [0.0, 0.091, 0.183, 0.274, 0.366, 0.457, 0.549, 0.640, 0.732, 0.823, 0.915, 1.006, 1.098, 1.189, 1.281]   ## en m
y = [0.0, 0.114, 0.211, 0.294, 0.360, 0.411, 0.446, 0.465, 0.469, 0.457, 0.429, 0.386, 0.327, 0.252, 0.161]   ## en m (axe vertical vers le haut)

N = len(x)         ## nombre de points du pointage

# Calcul de la vitesse en chaque point Mi (sauf le premier et le dernier) -----------------------------------------------
## v_i = Mi-1Mi+1 / (2 tau)   avec   Mi-1Mi+1 = racine( (x_(i+1) - x_(i-1))² + (y_(i+1) - y_(i-1))² )

t = []             ## dates en s
v = []             ## vitesses en m/s
z = []             ## altitudes en m
for i in range(1, N - 1):
    distance = ((x[i + 1] - x[i - 1]) ** 2 + (y[i + 1] - y[i - 1]) ** 2) ** 0.5
    t.append(i * tau)
    v.append(distance / (2 * tau))                   ## compléter la formule de la vitesse
    z.append(y[i])

# Calcul des énergies (en J) --------------------------------------------------------------------------------------------
## Ec = 1/2 m v²      Epp = m g z (origine des altitudes au point de départ)      Em = Ec + Epp

Ec = []
Epp = []
Em = []
for i in range(len(t)):
    Ec.append(0.5 * m * v[i] ** 2)                   ## compléter la formule de Ec
    Epp.append(m * g * z[i])                         ## compléter la formule de Epp
    Em.append(Ec[i] + Epp[i])                        ## compléter la formule de Em

# Affichage dans la console ---------------------------------------------------------------------------------------------

print(" t (s)     Ec (J)     Epp (J)    Em (J)")
for i in range(len(t)):
    print(" ", round(t[i], 2), "   ", round(Ec[i], 4), "   ", round(Epp[i], 4), "   ", round(Em[i], 4))

variation = (max(Em) - min(Em)) / max(Em) * 100
print()
print("Variation relative de l'énergie mécanique :", round(variation, 1), "%")
if variation < 5:
    print("L'énergie mécanique se conserve : les frottements sont négligeables.")
else:
    print("L'énergie mécanique diminue : les frottements ne sont pas négligeables.")

# Tracé des trois énergies en fonction du temps -------------------------------------------------------------------------

plt.figure(figsize=(10, 5))
plt.plot(t, Ec, "b-o", label="énergie cinétique Ec")
plt.plot(t, Epp, "g-s", label="énergie potentielle de pesanteur Epp")
plt.plot(t, Em, "r-^", label="énergie mécanique Em")
plt.xlabel("t (s)", fontsize=12)
plt.ylabel("Énergie (J)", fontsize=12)
plt.title("Bilan énergétique de la balle", fontsize=14)
plt.ylim(0, 1.35 * max(Em))
plt.grid()
plt.legend(loc="upper center", ncol=3, fontsize=9)
plt.show()

# Questions : quelle énergie se transforme en quelle autre pendant la montée ? pendant la descente ?
#             Que peut-on dire de l'énergie mécanique ? Conclure sur les frottements.
