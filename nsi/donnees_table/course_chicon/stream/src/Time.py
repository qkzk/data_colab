from collections import namedtuple

# on crée un type
Time = namedtuple('Time', ['hours', 'minutes', 'seconds'])


def create(hours, minutes, seconds):
    # types (entier)
    for param in (hours, minutes, seconds):
        assert isinstance(param, int), "les paramètres sont des entiers"

    # valeurs possibles
    assert 0 <= minutes <= 59, "minutes entre 0 et 59"
    assert 0 <= seconds <= 59, "seconds entre 0 et 59"

    return Time(hours, minutes, seconds)


def duree(t):
    return t[0] * 3600 + t[1] * 60 + t[2]


def compare(t1, t2):
    "negatif si t1 < t2"
    return duree(t1) - duree(t2)


def to_string(t):
    return "{0} heures {1} minutes et {2} secondes".format(t[0], t[1], t[2])


if __name__ == '__main__':

    t1 = create(1, 2, 3)
    t2 = create(2, 3, 4)
