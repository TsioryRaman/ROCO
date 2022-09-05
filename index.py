# Importing Libraries
import serial
import time
import pyttsx3
from Recognition import recognition

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

engine = pyttsx3.init()

def write_read(x):
    arduino.write(x.encode("utf-8"))
    time.sleep(5)


start = "Bonjour"

code = recognition()

print(code)


if (start == code):
    engine.say("Bonjour maitre, que puis-je faire pour vous?")
    engine.runAndWait()
    while True:
        try:
            
            commande = recognition()
            print(commande)
            
            value = write_read("avancer")
        except:
            engine.say("Desole, je ne reconnais pas votre commande")
            engine.runAndWait()
