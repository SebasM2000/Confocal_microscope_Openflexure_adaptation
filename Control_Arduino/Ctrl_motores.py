# Librerías
import serial
import time

# Configuración arduino
arduino =  serial.Serial("No shé", baudrate = 9600, timeoout = 1)
time.sleep(2)