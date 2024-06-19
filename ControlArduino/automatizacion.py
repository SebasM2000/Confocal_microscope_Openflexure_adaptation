# Librerías control arduino
import serial
import time 


# Movimiento motores
ult_pos_x, ult_pos_y, ult_pos_z = 0, 0, 0      # Última posicion
x, y, z = None, None, None                     # Posición actual (empezando en un valor nulo)
max_x, max_y, max_z = 5000, 5000, 5000         # Límite superior
min_x, min_y, min_z = -max_x, -max_y, -max_z   # Límite inferior
t = 0.05                                       # Tiempo en segundos de descanso entre cada paso


class ControlMaster:

    def __init__(self, dispositivo_maestro):
        self.dispositivo_maestro = dispositivo_maestro

    # Configuración arduino
        self.master =  serial.Serial("/dev/ttyACM0"dispositivo_maestro, baudrate = 9600, timeout = 1)
        time.sleep(2)

