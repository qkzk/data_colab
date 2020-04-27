from collections import namedtuple

# on crée un type
Vehicule = namedtuple('Vehicule', ['nom', 'roues', 'couleur'])

# on crée un objet Vehicule
ferrari = Vehicule('Ferrari', 4, 'rouge')

# on peut afficher son contenu facilement
print(ferrari)

# on peut aussi en créer un avec des mots clés
camion = Vehicule('Camion', roues=18, couleur='bleu')

# notation positionnelle
for vehicule in [camion, ferrari]:
    print(vehicule[0], "avec", vehicule[1],
          'roues de couleur', vehicule[2])

print()

# notation pointée
for vehicule in [camion, ferrari]:
    print(vehicule.nom, "avec", vehicule.roues,
          'roues de couleur', vehicule.couleur)


print()

# découpler

nom, roues, camion = ferrari

print(nom, roues, camion)
