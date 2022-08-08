# Importing Libraries
import serial
import time
from Recognition import recognition

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(x.encode("utf-8"))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    value = write_read("Bonjour")
    print("Venant de l'arduino", value)  # printing the value
