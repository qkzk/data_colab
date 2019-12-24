# TSP - Le voyageur de commerce 

Le problème du voyageur de commerce - _Traveling Salesman Problem_
TSP -, étudié depuis le 19e siècle, est l’un des plus connus dans le domaine de la recherche opérationnelle. William Rowan Hamilton a posé pour la première fois ce problème sous forme de jeu dès 1859.

## Problème

Le problème du TSP sous sa forme la plus classique est le suivant : « Un voyageur de commerce doit visiter une et une seule fois un nombre fini de villes et revenir à son point d’origine. Trouvez l’ordre de visite des villes qui minimise la distance totale parcourue par le voyageur ». Ce problème d’optimisation combinatoire appartient à la classe des problèmes NP-Complets.

Les domaines d’application sont nombreux : problèmes de logistique, de transport aussi bien de marchandises que de personnes, et plus largement toutes sortes de problèmes d’ordonnancement. Certains problèmes rencontrés dans l’industrie se modélisent sous la forme d’un problème de voyageur de commerce, comme l’optimisation de trajectoires de machines outils : comment percer plusieurs points sur une carte électronique le plus vite possible ?

Pour un ensemble de $`n`$ points, il existe au total $`n!`$ chemins
possibles. Le point de départ ne changeant pas la longueur du chemin,
on peut choisir celui-ci de façon arbitraire, on a ainsi $`(n-1)!`$
chemins différents. Enfin, chaque chemin pouvant être parcouru dans
deux sens et les deux possibilités ayant la même longueur, on peut
diviser ce nombre par deux. Par exemple, si on nomme les points, $`a,
b, c, d`$, les chemins $`abcd, bcda, cdab, dabc, adcb, dcba, cbad,
badc`$ ont tous la même longueur, seul le point de départ et le sens
de parcours change. On a donc $`\frac{1}{2}(n-1)`$ chemins candidats
à considérer. \
Par exemple, pour $`71`$ villes, le nombre de chemins candidats est
supérieur à $`5 × 10^{80}`$ qui est environ le nombre d'atomes dans l'univers
connu. \
([Page wikipedia _Problème du voyageur de commerce_](https://fr.wikipedia.org/wiki/Problème_du_voyageur_de_commerce)).

![img](http://helios.mi.parisdescartes.fr/~moisan/gtnum/data/recuit/car54.jpg)

## Heuristique gloutone

L'objectif de ce TP est de réaliser un algorithme glouton pour résoudre le TSP. 

Pour cela vous avez à votre disposition :

- un jeu de données [exemple.txt](exemple.txt)  contenant les
  coordonnées de différentes villes à raison d'une par ligne sous la
  forme `nom_de_la_ville latitude longitude`, vous pouvez bien sur
  l'étendre ou en générer un nouveau avec vos propres villes. 

  Par exemple

  ```
    Annecy	6,082499981	45,8782196
    Auxerre	3,537309885	 47,76720047
    Bastia	9,434300423	42,66175842
  ```

- Un fichier [TSP_biblio.py](TSP_biblio.py) contenant un ensemble de fonctions permettant la lecture des données et la visualisation d'un tour réalisé par le voyageur (ici pour le moment dans l'ordre d'apparition). Voici les principales fonctions

    ```python
    def get_tour_fichier(f):
        """
        Lit le fichier de villes format ville, latitude, longitude
        Renvoie un tour contenant les villes dans l ordre du fichier
        : param f: nom de fichier
        : return : (list)
        """
    ```

    ```python
    def distance (tour, i, j) :
        """
        Distance euclidienne entre deux villes i et j
        : param tour: sequence de ville
        : param i: numero de la ville de départ
        : param j: numero de la ville d arrivee
        : return: float
        CU: i et j dans le tour
        """
    ```

    ```python
    def longueur_tour (tour) :
        """
        Longueur totale d une tournée de la ville de départ et retourne à la ville de départ
        : param tour: tournee de ville n villes = n segments
        : return: float distance totale
        """
    ```

    ```python
    def trace (tour) :
        """
        Trace la tournée realisée
        : param tour: liste de ville
        """
    ```


![Tournée Annecy (plus proche voisin)](tournee_Annecy_ppv.png)

Afin de créer l'algorithme glouton pour résoudre le problème du TSP, nous allons réaliser certaines étapes.

1. Définir l'heuristique de choix de la solution optimale locale
2. Réaliser un programme Python utilisant les fonctions définies pour la lecture et l'affichage permettant de mettre en œuvre l'heuristique. Pour cela vous pouvez :
   1. réaliser une fonction qui génère une matrice qui stocke les distances 2 à 2 entre toutes les villes afin de ne faire le calcul de distance qu'une seule fois.
   2. réaliser une fonction qui retourne l'indice de la ville la plus proche étant donnée une ville, une liste de ville sous forme d'indice, une matrice de distance.
   3. réaliser l'heuristique gloutonne donnant le tour parcouru par le voyageur de commerce à partir d'une ville donnée en paramètre, la liste des villes et la matrice de distance ville à ville (on passera par un système d'indice).
