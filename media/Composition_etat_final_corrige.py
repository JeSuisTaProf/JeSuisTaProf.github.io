
# #######################################################################################################################
# COMPOSITION ETAT FINAL D"UNE TRANSFORMATION CHIMIQUE
# VERSION CORRIGÉE
# Déclaration des bibliothèques #########################################################################################

import matplotlib.pyplot as plt         #bibliothèque maths

# On considère un système comprenant deux réactifs R1 et R2 et deux produits P1 et P2
# Déclaration des coefficients stoechiométriques 'cs' des réactifs et des produits --------------------------------------

cs_R1=1         ## rentrer la valeur du coefficient stoechiométrique de R1
cs_R2=1         ## rentrer la valeur du coefficient stoechiométrique de R2
cs_P1=1         ## rentrer la valeur du coefficient stoechiométrique de P1
cs_P2=1         ## rentrer la valeur du coefficient stoechiométrique de P2

# Déclaration des quantités de matière 'ni' (en mol) à l'état initial des réactifs et des produits ----------------------

ni_R1=1e-1        ## rentrer la valeur calculée de ni_R1
ni_R2=1e-1        ## rentrer la valeur calculée de ni_R2
ni_P1=0           ## rentrer la valeur de ni_P1 d'après l'énoncé
ni_P2=0           ## rentrer la valeur de ni_P2 d'après lénoncé

# Calcul de l'avancement maximal et du réactif limitant -----------------------------------------------------------------

x1_max_R1=ni_R1/cs_R1          ## compléter la formule permettant de calculer l'avancement maximal si R1 réactif limitant
x2_max_R2=ni_R2/cs_R2          ## compléter la formule permettant de calculer l'avancement maximal si R2 réactif limitant

if x1_max_R1<x2_max_R2:        ## compléter par <   >   ou  =   à la place des ...
    x_max=x1_max_R1
    print("Le réactif limitant est R1 et l'avancement maximal est : x_max = ",round(x_max,3),'mol')

elif x1_max_R1>x2_max_R2:      ## compléter par <   >   ou  =   à la place des ...
    x_max=x2_max_R2
    print("Le réactif limitant est R2 et l'avancement maximal est : x_max = ",round(x_max,3),'mol')

else:
    x_max=x1_max_R1
    print("La réaction a lieu dans les proportions stoechiométriques")  ## compléter par la phrase adaptée à la situation
    print("L'avancement maximal x_max = ",round(x_max,3),'mol')

# Affichage dans la console des quantités de matière à l'état final ------------------------------------------------------

print('quantité finale de R1 nf =',round(ni_R1-cs_R1*x_max,2),'mol')
print('quantité finale de R2 nf =',round(ni_R2-cs_R2*x_max,2),'mol')
print('quantité finale de P1 nf =',round(ni_P1+cs_P1*x_max,2),'mol')
print('quantité finale de P2 nf =',round(ni_P2+cs_P2*x_max,2),'mol')

# Tracer le graphe représentant l'évolution des quantités de matière en fonction de l'avancement
# Créer une liste x qui contient 2 valeurs: 0 et x_max
# Créer une liste qui contiendra les valeurs des quantités de matière des réactifs et des produits

x=[0,x_max]
n_R1=[(ni_R1-cs_R1*valeur)for valeur in x]
n_R2=[(ni_R2-cs_R2*valeur)for valeur in x]
n_P1=[(ni_P1+cs_P1*valeur)for valeur in x]
n_P2=[(ni_P2+cs_P2*valeur)for valeur in x]

# Créer le graphique qui permettra d'observer les 4 quantités de matières ------------------------------------------------

plt.plot(x,n_R1,"b",label='Réactif R1')          #Donne l'étiquette sur les axes (couleur/trait plein/pointillés ...)
plt.plot(x,n_R2,"g--",label='Réactif R2')
plt.plot(x,n_P1,"r-.",label='P1')
plt.plot(x,n_P2,"c:",label='P2')

# Réglages des échelles des axes (min et max), tracer une grille et écrire les légendes sur les axes

liste_des_n_max=[max(n_R1),max(n_R2),max(n_P1),max(n_P2)]
n_max=max(liste_des_n_max)
plt.xlabel("Avancement(mol)",fontsize=14)
plt.ylabel("Quantité de matière(mol)",fontsize=14)
plt.title("Evolution de la quantité de matière en fonction de x_max",fontsize=14)
plt.legend(loc='upper right')
plt.axis([0,x_max,0,n_max])
plt.grid()
plt.show()