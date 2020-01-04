# Analyse en temps des algorithmes de tri

Les objectifs de ce TP sont de :
* mesurer le temps d'exécution des différents algorithmes de tri envisagés lors de la séance précédente :
  * tri sélection
  * tri insertion
  * tri rapide
  * tri fusion
* produire des courbes de temps en fonction de la taille des listes à trier
* observer ces courbes et tirer des conclusions sur la vitesse d'exécution des différents tris 


## Mener une campagne d'expérimentation

Pour réaliser le TP, nous allons mener une campagne d'expérimentations
qui va consister à générer des listes de nombres et mesurer
l'exécution de chacun des tris pour ces listes.

Afin de mesurer l'évolution du temps d'exécution en fonction de la
longueur des listes à trier, nous allons procéder à des
expérimentations pour des listes de taille différentes, et observer
l'évolution du temps d'exécution. 

Des questions se posent sur la manière de mener cette campagne :
* sur quel intervalle faut-il faire varier la taille des listes ?
* faut-il varier leur contenu : soit des listes déjà triées dans l'ordre ou dans l'ordre inverse, soit des listes mélangées (i.e. une liste triée dont on a mélangé les éléments) ?
* faut-il se contenter d'un essai ou moyenner le temps sur plusieurs essais ?
* pour une méthode donnée, faut-il toujours trier la même liste ou bien peut-on changer de liste à chaque essai ?
* lorsqu'on compare plusieurs méthodes, faut-il mesurer sur le même jeu de données ?

## Matériel fourni

* Récupérer [tris.py](./tris.py) et [listes.py](./listes.py)

### Module avec les tris

Le module `tris` propose un prédicat 
* `est_trie`
quatre fonctions de tri
* `tri_select`
* `tri_insert`
* `tri_rapide`
* `tri_fusion`
et une fonction
* `compare`
de comparaison utilisée par les fonctions de tri.

### Générateur de listes

Le module `listes` propose quatre fonctions de création de listes d'entiers :
* `cree_liste_croissante`
* `cree_liste_decroissante`
* `cree_liste_melangee`
* `cree_liste_melangee2`

Lire la documentation de ces fonctions et expérimenter dans Thonny.

## Première partie : mesurer le temps du tri sélection pour des listes mélangées

On s'intéresse dans cette partie exclusivement au tri par sélection et au calcul du temps d'exécution sur des listes mélangées.

### Mesure du temps : le module `timeit`

Le module `timeit` de Python permet de prendre une mesure du temps
d'exécution d'une fonction, en secondes. Ce module fournit une
fonction `timeit` qui accepte en entrée trois paramètres :
* `setup` permet de préciser à `timeit` les modules à charger pour
  permettre l'exécution correcte de la fonction (y compris donc le
  module qui contient la fonction à mesurer),
* `stmt` – pour _statement_, instruction en anglais – est l'appel de
  fonction qui sera mesurée (donc avec ses paramètres), 
* `number` est le nombre de fois où l'instruction `stmt` sera
  exécutée. Le temps mesuré sera le temps cumulé pour toutes ces
  exécutions. 

Remarquez que le code Python des deux parmaètres `setup`et `stmt` sont
donnés sous forme d'une chaîne de caractères. 


Par exemple, après avoir importé le module `timeit` :
```python
from timeit import timeit
```

on peut mesurer le temps d'exécution du tri par sélection sur une liste mélangée de taille 10 :
```python
timeit(setup='from tris import tri_select; from listes import cree_liste_melangee',
       stmt='tri_select(cree_liste_melangee(10))',
       number=100)
```

Le résultat obtenu représente le temps total mis pour exécuter 100 fois `tri_select(cree_liste_melangee(10))`.

### Calcul des temps pour un ensemble de longueurs de listes

* Écrire le code d'une fonction Python à un paramètre, une longeur de
  liste donnée, qui renvoie la mesure de temps pour des listes de
  cette longueur.

* Modifier cette fonction pour qu'elle accepte maintenant comme
  paramètre une longeur maximale de liste, et renvoie la
  mesure de temps pour des listes de toutes les longueurs comprises
  entre 1 et cette valeur maximale. Le premier élément est le temps
  pour des listes de taille 1, le deuxième pour des listes de taille
  2, etc. 

### Tracer des courbes

Étant donné un ensemble de valeurs dans une liste `l`, on peut utiliser le module `pylab` de matplotlib pour tracer une courbe où chaque valeur de la liste `l` à l'indice `i` est comprise comme le point de coordonnées `i`,`l[i]`.

Par exemple :
```python
import pylab
```
puis :
```python
l = [1,2,4,8,16]
pylab.plot(l)
pylab.show()
```

*Remarque :* en général, la méthode `show` de `pylab` ouvre une fenêtre pour présenter le graphique obtenu, et elle est bloquante, i.e. elle ne permet plus de dialoguer 
avec l'interpréteur Python. Il faut fermer cette fenêtre pour pouvoir poursuivre le dialogue. Avant la fermeture de cette fenêtre, certaines actions sont possibles sur 
le graphique. L'une d'elles est la sauvegarde du graphique dans un fichier image.


Si on veut que les abscisses soient différents, alors on fournit deux
listes : celles des abscisses et celle des ordonnées :
```python
x = [1,2,3,4,5]
y = [1,2,4,8,16]
pylab.plot(x,y)
pylab.show()
```

On peut améliorer la qualité du graphique produit en spécifiant des titres, et même une grille qui facilite la lecture  :
```python
NBRE_ESSAIS = 100
pylab.title('Temps du tri par sélection (pour {:d} essais)'.format(NBRE_ESSAIS))
pylab.xlabel('taille des listes')
pylab.ylabel('temps en secondes')
pylab.grid()
pylab.show()
```

### Courbe du tri par sélection sur des listes mélangées

* Écrire une fonction, à un paramètre, qui produit une courbe du temps d'exécution du tri sélection pour des listes mélangées dont la taille varie de 1 à la valeur du paramètre donné.

## Deuxième partie : mesurer le temps des autres tris pour des listes mélangées

* Afin d'automatiser un peu la campagne d'expérimentation, on propose d'écrire une fonction à deux paramètres : le premier correspond au nom du tri à exécuter, sous forme d'une chaîne de caractères, le second correspond à la taille maximale de la liste. La fonction a pour effet de produire la courbe. Il peut être opportun de modifier la fonction qui produit la liste des temps d'exécution pour y ajouter un paramètre.

On est maintenant en capacité de produire une courbe pour chaque tri.

* Produire une courbe du temps d'exécution du tri sélection, la sauvegarder.
* Produire une courbe du temps d'exécution du tri insertion, la sauvegarder.
* Produire une courbe du temps d'exécution du tri fusion, la sauvegarder.
* Produire une courbe du temps d'exécution du tri rapide, la sauvegarder.
* Observer les courbes obtenues et discuter des différences entre celles-ci.


# Pour la prochaine fois (17 juin)

L'objectif est de produire le matériel permettant la préparation d'une séance sur l'analyse des temps d'exécution des différents tris. 

## Courbes de temps pour les listes triées dans l'ordre croissant

* Produire les courbes pour les quatre tris.

## Courbes de temps pour les listes triées dans l'ordre décroissant

* Produire les courbes pour les quatre tris.

## Méthode `sort` de Python

* Produire les mêmes courbes pour la méthode `sort` de Python.
* En comparant les courbes obtenues avec celles obtenues pour les quatre algorithmes étudiés, le(s)quel(s) pourrai(en)t être celui implantant la méthode `sort` ?

## Séance sur les temps d'exécution des tris

* Réfléchir au déroulement d'une séance face aux élèves pour introduire la notion de temps d'exécution de différents algorithmes avec illustration sur les algorithmes de tri.















