import Time
import Competitor
import csv
from pprint import pprint

FICHIERS_INSCRITS = '../data/small_inscrits.csv'
FICHIERS_PERFORMANCES = '../data/small_performances.csv'


def read_competitors():
    inscrits = {}
    numero_dossard = 1
    with open(FICHIERS_INSCRITS) as fichier_csv:
        csv_lecteur = csv.reader(fichier_csv, delimiter=';')
        next(csv_lecteur)
        for line in csv_lecteur:
            competitor = Competitor.create(line[0], line[1], line[2],
                                           line[3], numero_dossard)
            inscrits[numero_dossard] = competitor
            numero_dossard += 1
    # pprint(inscrits)
    return inscrits


def afficher_competiteurs(liste_competiteurs):
    for competiteur in liste_competiteurs:
        print(Competitor.to_string(competiteur))


def select_competitor_by_bib(inscrits, no_dossard):
    return inscrits.get(no_dossard)


def select_competitor_by_birth_year(inscrits, annee_naissance):
    '''liste'''
    nes_cette_annee = []
    annee_naissance = str(annee_naissance)
    for competiteur in inscrits.values():
        if annee_naissance in competiteur["birth_date"]:
            nes_cette_annee.append(competiteur)
    return nes_cette_annee


def select_competitor_by_name(inscrits, name):
    '''liste'''
    portent_le_nom = []
    for competiteur in inscrits.values():
        if name in competiteur["last_name"]:
            portent_le_nom.append(competiteur)
    return portent_le_nom


def read_performances():
    performances = {}
    with open(FICHIERS_PERFORMANCES) as fichier_csv:
        csv_lecteur = csv.reader(fichier_csv, delimiter=';')
        next(csv_lecteur)
        for line in csv_lecteur:
            no_dossard = int(line[0])
            heures = int(line[1])
            minutes = int(line[2])
            secondes = int(line[3])

            perf = Time.create(heures, minutes, secondes)

            performances[no_dossard] = perf
    return performances


def set_performances(inscrits, performances):
    # association
    for no_dossard in inscrits:
        inscrits[no_dossard]['performance'] = performances.get(no_dossard)


def main():
    inscrits = read_competitors()  # dictionnaire
    afficher_competiteurs(inscrits.values())
    premier_inscrit = select_competitor_by_bib(inscrits, 1)
    nes_1980 = select_competitor_by_birth_year(inscrits, 1980)
    bob = select_competitor_by_name(inscrits, 'Robert')
    performances = read_performances()
    pprint(performances)
    set_performances(inscrits, performances)
    pprint(inscrits)

    return inscrits, performances


if __name__ == '__main__':
    inscrits, performances = main()
