#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
import subprocess
#from art import *

points = 12 #mettre l'estimation de points
pts = str(points)+"pts"
#pts = text2art(pts,font='block')
list_commands = [["echo", "\"Commande 1\""], ["echo", "\"Commande 2\""]]  # mettre les commandes (liste de listes)
print(pts)


def hall_sensor_callback(channel):
    print("#######################################")
    print("Lancement de la procédure de démarrage:")
    for i in list_commands:
        subprocess.run(i)
    print(pts)
    GPIO.cleanup()



hall_sensor = 21 # mettre pin digital du hall sensor

GPIO.setmode(GPIO.BOARD)
GPIO.setup(hall_sensor, GPIO.IN)

GPIO.add_event_detect(hall_sensor, GPIO.BOTH, callback=hall_sensor_callback)  # detection lancement

while True:
    print(GPIO.input(21))
