from collections import namedtuple

# on crée un type
Vehicule = namedtuple('Vehicule', ['nom', 'roues', 'couleur'])


# on crée un objet Vehicule
ferrari = Vehicule('Voiture rouge', 4, 'rouge')


# on peut afficher son contenu facilement
# print(ferrari)


# Vehicule(nom='Voiture rouge', roues=4, couleur='rouge')


# on peut aussi en créer un avec des mots clés
camion = Vehicule(nom='Camion', roues=18, couleur='bleu')

# notation positionnelle
# for vehicule in [camion, ferrari]:
#     print(vehicule[0], "avec", vehicule[1],
#           'roues de couleur', vehicule[2])

#
# Camion avec 18 roues de couleur bleu
# Voiture rouge avec 4 roues de couleur rouge


# notation pointée
for vehicule in [camion, ferrari]:
    # print(vehicule.nom, "avec", vehicule.roues,
    #       'roues de couleur', vehicule.couleur)

    print("{0} de couleur {1}".format(vehicule.nom, vehicule.couleur))


print()

# découpler

nom, roues, camion = ferrari

print(nom, roues, camion)
