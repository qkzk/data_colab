__title__='Algorithme des k plus proches voisins pour les données de crocos.csv'
__author__='qkzk'
__date__='2020/03/15'
__doc__='''
titre:   {0}
author:  {1}
date:    {2}

Implémentation des k plus proches voisins pour les données des crocodiles

'''.format(__title__, __author__, __date__)


from generer_donnees import *
from presenter_donnees import *
from presenter_resultats import *


PROPORTION_TEST = 1/3


def separer_entrainement_test(animaux, proportion=None):
    '''
    Sépare le jeu de données aléatoirement entre un jeu d'entrainement
    et un jeu de test.

    @param animaux: (list of dict)
    @param proportion: (float)
    @return: (tuple (list of dict, list of dict))
    '''
    if proportion is None:
        proportion = PROPORTION_TEST
    entrainement = []
    test = []
    for animal in animaux:
        if random.random() < proportion:
            test.append(animal)
        else:
            entrainement.append(animal)
    return entrainement, test


def distance_euclidienne(x, y):
    '''
    Calcule la distance Euclidienne entre deux instances.

    On ne tient compte que des données numériques (flottantes)
    @param x, y: (dict) doivent contenir des clés à valeurs réelles
    @return: (float) la distance
    '''
    return sum([(x[champ] - y[champ]) ** 2
                for champ in CHAMPS
                if type(x[champ]) == float]) ** 0.5


def choisir_classe_majoritaire(inconnu, entrainement, k):
    '''
    Choisit la classe majoritaire d'une entrée inconnue

    @param inconnu: (dict) un reptile (crocodile ou alligator ???)
    @param entrainement: (list of dict) les reptiles connus
    @param k: (int) le nombre de voisins participant au vote
    '''
    distances = [(animal['espece'], distance_euclidienne(inconnu, animal))
                 for animal in entrainement]
    distances.sort(key=lambda x:x[1])
    votes = [animal[0] for animal in distances[:k]]
    return vote_majoritaire(votes)


def vote_majoritaire(votes):
    '''
    DOC À COMPLÉTER
    '''
    nb_vote_crocos = sum([1 for vote in votes if vote == "crocodile"])
    nb_vote_alligators = sum([1 for vote in votes if vote == "alligator"])
    if nb_vote_crocos > nb_vote_alligators:
        return "crocodile"
    else:
        return "alligator"

def appliquer_knn(test, entrainement, k):
    '''
    applique l'algorithme des k plus proches voisins à un jeu de données
    déjà séparées entre test et entrainement

    @param test, entrainement: (list of dict)
    @param k: (int) le nb de voisins retenus dans le vote
    @return: (list of dict) le dictionnaire test, enrichi des votes
    '''
    for animal in test:
        animal["vote"] = choisir_classe_majoritaire(animal, entrainement, k)
    return test


def calculer_precision(test):
    '''
    DOC À COMPLÉTER
    '''
    total = len(test)
    bons_votes = sum([1 for animal in test if animal["espece"] == animal["vote"]])
    return bons_votes / total


def main():
    '''
    Pilote l'algorithme des plus proches voisins.
    '''
    animaux = charger_donnees()
    entrainement, test = separer_entrainement_test(animaux)
    test = appliquer_knn(test, entrainement, 3)
    precision = calculer_precision(test)
    print(precision)
    presenter_test(entrainement, test)

if __name__ == '__main__':
    main()
