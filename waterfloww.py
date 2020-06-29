#-*-coding:utf-8 -*-
import time
from time import sleep
from firebase import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(18, GPIO.IN) 
pulsos_min = 0 #pulsos por minuto
total_pulsos = 0 #total de pulsos
const= 0.10      #constante
novo_tempo = 0.0

URL_Firebase = 'https://waterenergy-iot-app.firebaseio.com/'

WATERFLOW = 0.0


#'firebase' e o objeto que permite interagir com o Firebase Realtime.
firebase = firebase.FirebaseApplication(URL_Firebase, None)
def envia_ID_WATERFLOW_firebase(tag_lida):
     global firebase
     data_hora = datetime.datetime.now()
     data_firebase = {"TAG": tag_lida,"Data_Hora":data_hora}
     firebase.post('/WATER/id', data_firebase)
     print ('TAG '+tag_lida+' enviada para o Firebase.')
     return

while (True):
    novo_tempo = time.time()+60
    pulsos_min = 0
    while time.time() <= novo_tempo:
        if(GPIO.input(18)!= 0):
             pulsos_min += 1
             total_pulsos += 1
        print("Litros por minuto",round(pulsos_min * const,2)) 
        print("Total de Litros",round(total_pulsos * const,2))
        print("Média:  ",(total_pulsos + pulsos_min)/60)
        print("Tempo:  ",novo_tempo)
        
    envia_ID_WATERFLOW_firebase(total_pulsos)

