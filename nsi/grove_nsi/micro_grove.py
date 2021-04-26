############################################
#   Librairie pour utilisation des modules #
#   Grove avec micro-bit dans Mu editor    #
#  		par Philippe LECLERC			   #
#			DANE NORMANDIE       		   #
############################################
from microbit import *
from machine import time_pulse_us
from math import log
from music import play
from time import sleep_ms
from math import ceil


analogiq_in = [pin0, pin1, pin2, pin3, pin4, pin10]

# Module Grove - Temperature Sensor
# Retourne la température en degrés Celcius
# Paramètres :   nom de la broche utilisée
#               version du modèle de capteur : 0, 1 ou 2

def mesure_temperature(broche = pin2, model = 0):
    if broche in analogiq_in:
	    # each of the sensor revisions use different thermistors, each with their own B value constant
        if model == 2:
            bValue = 4250  # sensor v1.2 uses thermistor ??? (assuming NCP18WF104F03RC until SeeedStudio clarifies)
        elif model == 1:
            bValue = 4250  # sensor v1.1 uses thermistor NCP18WF104F03RC
        else:
            bValue = 3975  # sensor v1.0 uses thermistor TTC3A103*39H
        a = broche.read_analog()
        resistance = (float)(1023 - a) * 10000 / a
        temperature = (float)(1 / (log(resistance / 10000) / bValue + 1 / 298.15) - 273.15)
        return temperature
    else:
        return 'Erreur de broche'
# ###

# Module Grove - Ultrasonic Ranger
# Retourne la durée d'un aller/retour des ultra_sons en microsecondes
# Paramètre : Nom de la broche utilisée

def mesure_temps_A_R(broche = pin1):
    broche.write_digital(0)
    sleep_ms(2)
    broche.write_digital(1)
    sleep_ms(10)
    broche.write_digital(0)
    broche.read_digital()
    dt = time_pulse_us(broche, 1)
    return dt

# ###

# Module Grove - Speaker
# Emet un beep
# Paramètre : Nom de la broche utilisée

def bip(broche = pin0):
    play(['e5:3'], broche)
    return 'Erreur de broche'
# ###

# Module Grove - ligth-sensor
# its_dark retourne True si la luminosité < 10 lux ~
# Paramètre : Nom de la broche utilisée

def it_s_dark(broche = pin0):
    if broche in analogiq_in:
        return (broche.read_analog() < 50)
    else:
        return 'Erreur de broche'
# ###

# Module Grove - ligth-sensor
# retourne un entier (0 -> 100%) ( 100% correspond à ~ 60 lux)
# Paramètre : Nom de la broche utilisée

def luminosite(broche = pin0):
    if broche in analogiq_in:
        return int(broche.read_analog() / 612 *100) -1
    else:
        return 'Erreur de broche'
# ###

# Module Grove - Rotary angle sensor
# retourne la position du bouton ( 0 -> 100% )
# Paramètre : Nom de la broche utilisée

def position_curseur(broche = pin0):
    if broche in analogiq_in:
        return int(broche.read_analog() / 1021 *100)
    else:
        return 'Erreur de broche'

# Affiche une valeur sous forme de jauge (bargraph) sur la matrice à leds
# Paramètres : val -> valeur à afficher , val_max -> la plus grande valeur que peut prendre val

def affiche_jauge(val,val_max=100):
    display.clear()
    n = ceil(5 * val / val_max)
    nl = min(5, n)
    if nl >= 0 and nl <= 5:
        for i in range(nl):
            for j in range(5):
                display.set_pixel(j, 4-i, 9)

# Module Grove - Grove-Servo
# positionne le servomoteur à un  0 < angle < 180 degrés
# Paramètre : Nom de la broche utilisée, angle

def angle_servomoteur(broche = pin0, angle = 0):
    if broche in analogiq_in:
        broche.write_analog(28 + max(0, min(angle, 180)) * 94 / 180)
    else:
        return 'Erreur de broche'
