
# #######################################################################################################################
# VARIATION DU VECTEUR VITESSE ET SOMME DES FORCES (Première spécialité)
# VERSION À COMPLÉTER : remplacer chaque ... par le code qui convient, puis exécuter le programme.
# Relation approchée entre la variation du vecteur vitesse entre deux instants voisins et la somme des forces :
#               m × Δv / Δt ≈ ΣF
# Exemple : balle lancée en l'air, soumise uniquement à son poids (frottements négligés)
# Déclaration des bibliothèques #########################################################################################

import matplotlib.pyplot as plt         # bibliothèque pour tracer les graphiques

# Données du pointage de la vidéo ---------------------------------------------------------------------------------------
## Valeurs d'exemple : remplacer par les valeurs de votre pointage (copier-coller depuis Regressi ou Aviméca)

tau = 0.040        ## durée entre deux images en s
m = 0.0451         ## masse de la balle en kg
g = 9.81           ## intensité de la pesanteur en N/kg

x = [0.0, 0.091, 0.183, 0.274, 0.366, 0.457, 0.549, 0.640, 0.732, 0.823, 0.915, 1.006, 1.098, 1.189, 1.281]   ## en m
y = [0.0, 0.114, 0.211, 0.294, 0.360, 0.411, 0.446, 0.465, 0.469, 0.457, 0.429, 0.386, 0.327, 0.252, 0.161]   ## en m

N = len(x)         ## nombre de points du pointage

# Calcul des coordonnées du vecteur vitesse en chaque point Mi ----------------------------------------------------------
## vx_i = (x_(i+1) - x_(i-1)) / (2 tau)   et   vy_i = (y_(i+1) - y_(i-1)) / (2 tau)
## On ne peut pas calculer la vitesse au premier et au dernier point : on met None (pas de valeur)

vx = [None] * N
vy = [None] * N
for i in range(1, N - 1):
    vx[i] = ...        ## compléter la formule de vx
    vy[i] = ...        ## compléter la formule de vy

# Calcul des coordonnées du vecteur variation de vitesse Δv au point Mi -------------------------------------------------
## Δvx_i = vx_(i+1) - vx_(i-1)   et   Δvy_i = vy_(i+1) - vy_(i-1)   (variation pendant Δt = 2 tau)

dvx = [None] * N
dvy = [None] * N
for i in range(2, N - 2):
    dvx[i] = ...                   ## compléter la formule de Δvx
    dvy[i] = ...                   ## compléter la formule de Δvy

# Comparaison de m × Δv / Δt avec la somme des forces (ici le poids P = m g, vertical vers le bas) ----------------------

print("Somme des forces : poids P = m × g =", round(m * g, 3), "N, vertical vers le bas")
print()
print(" Point   m×Δvx/Δt (N)   m×Δvy/Δt (N)")
for i in range(2, N - 2):
    Fx = m * dvx[i] / (2 * tau)
    Fy = ...                                       ## compléter : composante verticale de m × Δv / Δt
    print("  M" + str(i), "     ", round(Fx, 3) + 0.0, "        ", round(Fy, 3) + 0.0)    ## + 0.0 évite l’affichage « -0.0 »
print()
print("Conclusion : m×Δv/Δt est vertical, vers le bas, et sa valeur est proche de m×g : on retrouve le poids.")

# Tracé de la trajectoire, des vecteurs vitesse (en bleu) et des vecteurs Δv (en rouge) ---------------------------------

echelle_v = 0.05        ## échelle des vecteurs vitesse : 1 m/s est représenté par 0,05 m sur le graphique
echelle_dv = 0.25       ## échelle des vecteurs Δv : 1 m/s est représenté par 0,25 m sur le graphique

plt.figure(figsize=(10, 5))
plt.plot(x, y, "ko", label="positions Mi")       ## les points du pointage

for i in range(1, N - 1):                        ## vecteurs vitesse
    plt.arrow(x[i], y[i], echelle_v * vx[i], echelle_v * vy[i], color="b", width=0.002, head_width=0.012)

for i in range(2, N - 2):                        ## vecteurs variation de vitesse
    plt.arrow(x[i], y[i], echelle_dv * dvx[i], echelle_dv * dvy[i], color="r", width=0.002, head_width=0.012)

plt.plot([], [], "b", label="vecteur vitesse v")             ## lignes vides pour la légende
plt.plot([], [], "r", label="vecteur variation de vitesse Δv")
plt.xlabel("x (m)", fontsize=12)
plt.ylabel("y (m)", fontsize=12)
plt.title("Variation du vecteur vitesse d'une balle soumise à son poids", fontsize=14)
plt.axis("equal")
plt.grid()
plt.legend(loc="lower center")
plt.show()

# Question : les vecteurs Δv ont-ils tous la même direction et le même sens ? Comparer avec le vecteur poids.
