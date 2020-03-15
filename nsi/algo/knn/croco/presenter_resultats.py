__title__ = 'Résultats de kNN pour les reptiles'
__author__ = 'qkzk'
__date__ = '2020/03/15'
import pylab
__doc__ = '''
titre:   {0}
author:  {1}
date:    {2}

Construction graphique (à base de copier coller)
des résultats du test

'''.format(__title__, __author__, __date__)


def presenter_test(entrainement, test):
    '''
    Présente avec différentes courleurs et symbole le résultat de
    l'algorithme kNN
    '''
    crocos = [animal for animal in entrainement
              if animal['espece'] == "crocodile"]
    alligators = [animal for animal in entrainement
                  if animal['espece'] == "alligator"]

    crocos_x = [croco["taille"] for croco in crocos]
    crocos_y = [croco["gueule"] for croco in crocos]

    alligator_x = [alligator["taille"] for alligator in alligators]
    alligator_y = [alligator["gueule"] for alligator in alligators]

    crocos_bons = [animal for animal in test
                   if animal['espece'] == "crocodile"
                   and animal['espece'] == animal['vote']]
    alligators_bons = [animal for animal in test
                       if animal['espece'] == "alligator"
                       and animal['espece'] == animal['vote']]

    crocos_mauvais = [animal for animal in test
                      if animal['espece'] == "crocodile"
                      and animal['espece'] != animal['vote']]
    alligators_mauvais = [animal for animal in test
                          if animal['espece'] == "alligator"
                          and animal['espece'] != animal['vote']]

    crocos_bons_x = [croco["taille"] for croco in crocos_bons]
    crocos_bons_y = [croco["gueule"] for croco in crocos_bons]

    alligator_bons_x = [alligator["taille"] for alligator in alligators_bons]
    alligator_bons_y = [alligator["gueule"] for alligator in alligators_bons]

    crocos_mauvais_x = [croco["taille"] for croco in crocos_mauvais]
    crocos_mauvais_y = [croco["gueule"] for croco in crocos_mauvais]

    alligator_mauvais_x = [alligator["taille"] for alligator in alligators_mauvais]
    alligator_mauvais_y = [alligator["gueule"] for alligator in alligators_mauvais]

    pylab.scatter(crocos_x, crocos_y, c='red', marker='x',
                  label='Crocodiles')
    pylab.scatter(alligator_x, alligator_y, c='green', marker='o',
                  label='Alligators')

    pylab.scatter(crocos_bons_x, crocos_bons_y, c='orange', marker='x',
                  label='Crocodiles corrects')
    pylab.scatter(alligator_bons_x, alligator_bons_y, c='orange', marker='o',
                  label='Alligators corrects')

    pylab.scatter(crocos_mauvais_x, crocos_mauvais_y, c='blue', marker='x',
                  label='Crocodiles ratés')
    pylab.scatter(alligator_mauvais_x, alligator_mauvais_y, c='blue', marker='o',
                  label='Alligators ratés')

    pylab.title("Crocodiles vs Alligator")
    pylab.legend(loc='upper left')
    pylab.grid(True)

    pylab.show()
