#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import urllib
import math
import pylab


def creation_dico_region(nom_fichier, encode='utf-8', sep=';'):
    """
    Création d'un dictionnaire :
    clé = nom de région
    valeur = liste des couples ('NOM_DE_VILLE', NOMBRE_HABITANTS)
    """
    dico = {}
    with open(nom_fichier, 'r') as entree:
        for ligne in entree:
            ligne = ligne.rstrip()
            ligne = ligne.split(sep)
            region = ligne[1]
            ville = ligne[6]
            habitant = int(ligne[9])
            if int(ligne[0]) > 10 :
                if region not in dico:
                    dico[region] = []
                dico[region].append((ville,habitant))
    return dico


def ville_habitant_min(liste):
    """
    Retourne le couple avec le moins d'habitant, parmis la liste des couples 
    ('NOM_DE_VILLE', NOMBRE_HABITANTS)
    """
    id_ville = 0
    id_min = 0
    for id_ville in range(1, len(liste)):
        if liste[id_min][1] > liste[id_ville][1]:
            id_min = id_ville
    return liste[id_min]


def tour_depeuple(dico):
    lst = []
    for region in dico:
        ville = ville_habitant_min(population[region])
        lst.append([region, ville[0], ville[1]])
    return lst


def ville_to_lon_lat(ville):
    """
    Retourne la longitude et la latitude d'une ville
    """
    #print(ville)
    serveur = "https://nominatim.openstreetmap.org/"
    ville_quote = urllib.parse.quote(ville)
    path = "search?city={}&format=json&limit=1".format(ville_quote)
    url = "{}{}".format(serveur, path)
    #print(url)
    #rep = urllib.request.urlopen(url.encode("utf-8").decode('latin1')).read()
    
    rep = urllib.request.urlopen(url).read()
    
    rep = rep.decode('utf-8')
    rep = json.loads(rep)
    #print(rep)
    return (rep[0]['lon'], rep[0]['lat'])


def distance_entre_deux_villes(v1, v2):
    """
    Retourne la distance entre deux villes en considérant la
    surface plane
    
    :param v1: tuple (lon, lat)
    :type v1: tuple
    :param v2: tuple (lon, lat)
    :type v2: tuple
    :return: distance en km
    :rtype: float
    
    :cu: Ne fonctionne que pour un même hémisphére
    """
    
    RT = 6371
    
    lon = RT*(float(v1[0])-float(v2[0]))
    lat = RT*(float(v1[1])-float(v2[1]))
    return int(math.sqrt(lon**2 + lat**2))*math.pi/180

def affiche_matrice_distance(lst):
    """
    Retourne une liste de liste telque
    liste[i][j] = distance entre les villes i et j
    """
    
    taille = len(lst)
    mat = []
    entete = ['{:^8}'.format('')]
    for v in lst:
        entete.append('{:^8}'.format('{:.8}'.format(v[0])))
    mat.append(entete)
    for v in lst:
        (ville, lon, lat) = v
        distance = ['{:^8}'.format('{:.8}'.format(ville))]        
        for v1 in lst:
            #print(v1, v1[1])
            (ville1, lon1, lat1) = v1
            d = distance_entre_deux_villes((lon, lat), (lon1, lat1))
            distance.append("{:^8.2f}".format(d))
        mat.append(distance)
    return mat


def matrice_distance(lst):
    """
    Retourne une liste de liste telque
    liste[i][j] = distance entre les villes i et j
    """
    mat = []
    for v in lst:
        (ville, lon, lat) = v
        distance = []
        for v1 in lst:
            (ville1, lon1, lat1) = v1
            d = distance_entre_deux_villes((lon, lat), (lon1, lat1))
            distance.append(d)
        mat.append(distance)
    return mat


def tour_to_liste_ville_lon_lat(tour, start='Douai') :
    """
    A remplir
    ....
    """
    lst = []
    for destination in tour :
        ville = destination[1]
        coords = ville_to_lon_lat(ville)
        lst.append((ville, float(coords[0]), float(coords[1])))
    
    coords = ville_to_lon_lat(start)
    lst.insert(0, (start, float(coords[0]), float(coords[1])))
    return lst


def demo_affiche_mat(tour):
    tour.insert(0 , ['Hauts-de-France', 'Douai', 40860])
    t = tour_to_liste_ville_lon_lat(tour)
    M = affiche_matrice_distance(t)
    print('\n'.join(['|'.join(l) for l in M]))


def parcours_trace(tour,title="graph"):
    """
    A remplir 
    ....
    
    """
    x = [ t[1] for t in tour ]
    y = [ t[2] for t in tour ] 
    x += [ x [0] ] # on ajoute la dernière ville pour boucler
    y += [ y [0] ] #
    pylab.plot(x, y, linewidth=2)
    for ville, x, y in tour :
        pylab.text(x, y, ville) 
    pylab.title(title)
    pylab.show()


def ville_la_plus_proche(tour, id_depart, id_ville_visite):
    """
    Parmis les villes du tour non visitées, retourne l'indice de la 
    ville la plus proche de la ville depart ayant pour indice id_depart.
    
    :param tour: liste de 3-tuple : ('Ville', lon, lat)
    :type tour: list
    :param id_depart: index de la ville de depart
    :type id_depart: int
    :param id_ville_depart: Liste des indices des villes visitées
    :type id_ville_depart: Liste de int
    :return: indice de la ville la plus proche
    :rtype: int
    """
    
    DST = MAT[id_depart]
    DST[id_depart] = float('inf')
    idmin = id_depart

    for d in range(len(DST)):
        if DST[d] != '0.0' and d not in id_ville_visite:
            if DST[d] < DST[idmin]:
                idmin = d
    return idmin
            
def parcours_min(tour, start=0):
    
    parcour = [start]
    
    while len(parcour) < len(tour):
        depart = parcour[-1]
        laplusproche = ville_la_plus_proche(tour, depart, parcour)
        parcour.append(laplusproche)
    return parcour

print("Lecture du fichier et création du dictionnaire")
population = creation_dico_region('communes.csv')
print("Recherche les villes les moins peuplées")
tour = tour_depeuple(population)
print("Recherche les longitudes et les lattitudes")
villes = tour_to_liste_ville_lon_lat(tour)
print("Calcul des distances inter-villes")
MAT = matrice_distance(villes)
print("Recherche les id des villes pour le parcours le moins long")
id_ville_min = parcours_min(villes)
print("Création du parcours")
tour_min = [villes[v] for v in id_ville_min]
print("Affichage d'un parcours minimales")
parcours_trace(tour_min, "Tour de France d'Alice")
