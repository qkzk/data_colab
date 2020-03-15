__title__='''Présenter les données des reptiles contenues dans crocos.csv'''
__author__='''qkzk'''
__date__='''2020/03/15'''
__doc__='''
titre:   {0}
author:  {1}
date:    {2}

Ce module construit simplement un affichage des données présentes.

'''.format(__title__, __author__, __date__)

import csv
import pylab
from generer_donnees import *


def charger_donnees(fichier=None):
    '''
    Charge les données depuis un fichier csv
    @param fichier: (str) le chemin vers un fichier csv
    @return: (list of dict) les données, converties en flottants si possible
    '''
    animaux = []
    if fichier is None:
        fichier = FICHIER
    with open(fichier, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        for animal in csvreader:
            for key, value in animal.items():
                try:
                    animal[key] = float(value)
                except ValueError as e:
                    pass
            animaux.append(animal)
    return animaux


def presenter_donnees(animaux):
    '''
    Construit un graphique des données de départ, pour illustrer
    @param animaux: (list of dict) les reptiles
    @SE: dessine un graphique
    '''
    crocos = [animal for animal in animaux
              if animal['espece'] == "crocodile"]
    alligators = [animal for animal in animaux
                  if animal['espece'] == "alligator"]

    crocos_x = [croco["taille"] for croco in crocos]
    crocos_y = [croco["gueule"] for croco in crocos]

    alligator_x = [alligator["taille"] for alligator in alligators]
    alligator_y = [alligator["gueule"] for alligator in alligators]

    pylab.scatter(crocos_x, crocos_y, c='red', marker='x',
                  label='Crocodiles')
    pylab.scatter(alligator_x, alligator_y, c='green', marker='o',
                  label='Alligators')

    pylab.title("Crocodiles vs Alligator")
    pylab.legend(loc='upper left')
    pylab.grid(True)

    pylab.show()


def main():
    '''
    Pilote le chargement
    '''
    animaux = charger_donnees()
    presenter_donnees(animaux)

if __name__ == '__main__':
    main()
