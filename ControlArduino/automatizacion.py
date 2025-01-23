# Librerías control arduino
import serial
import time 


# Variables globales
ultima_posicion_x, ult_posicion_y, ult_posicion_z = 0, 0, 0  # Última posicion
max_x, max_y, max_z = 5000, 5000, 5000                       # Límite superior
t = 0.05                                                     # Tiempo en segundos de descanso entre cada paso
laser = None

def saludo():
    print("Hola")

# Datos usuario
def almacenar_datos_usuario(nombre, apellido, correo):
    datos_usuario = {}
    datos_usuario['nombre'] = nombre
    datos_usuario['apellido'] = apellido
    datos_usuario['correo'] = correo

    # Guardar datos del usuario en archivo .txt
    with open("datosUsuario.txt", "w") as file:
        file.write(datos_usuario)

# Arduino
def deteccion_arduino():
    puertos = serial.tools.list_ports_comports()
    for puerto in puertos:
        if 'Arduino' in puerto.description:
            # Configuración arduino
            arduino =  serial.Serial(puerto.device, baudrate = 9600, timeout = 1)
            time.sleep(2)
            return arduino
        
    return None


# Coordenadas motores
def almacenar_coordenadas(x, y, z):
    with open("coordenadas.txt", "w") as file:
        file.write(f"{x}, {y}, {z}")

def lectura_ultimas_coordenadas():
    try:
        with open("coordenadas.txt", "r") as file:
            line = file.readline()

            if line:
                return tuple(map(int, line.split(',')))
                    
    except FileNotFoundError:
        return None
    
    
# Movimiento motores
def movimiento_motores(arduino, x_i, y_i, z_i, x_f, y_f, z_f):
    global max_x, max_y, max_z

    # Límites de movimiento
    if x_i < -max_x:
        x_i = -max_x

    elif x_i > max_x:
        x_i = max_x

    if y_i < -max_y:
        y_i = -max_y

    elif y_i > max_y:
        y_i = max_y

    if z_i < -max_z:
        z_i = -max_z

    elif z_i > max_z:
        z_i = max_z
            

    # Ejecuta los pasos en el archivo .ino
    # Dirección horaria X
    while x_i > x_f:
        arduino.write(b'1')
        x_f += 1
        time.sleep(t)

    # Dirección anti-horaria X
    while x_i < x_f:
        arduino.write(b'2')
        x_f -= 1
        time.sleep(t)

    # Dirección horaria Y
    while y_i > y_f:
        arduino.write(b'3')
        y_f += 1
        time.sleep(t)
            
    # Dirección anti-horaria Y
    while y_i < y_f:
        arduino.write(b'4')
        y_f -= 1
        time.sleep(t)


    # Dirección horaria Z
    while z_i > z_f:
        arduino.write(b'5')
        z_f += 1
        time.sleep(t)
            
    # Dirección anti-horaria Z
    while z_i < z_f:
        arduino.write(b'6')
        z_f -= 1
        time.sleep(t)


# Control del láser
def estado_laser(arduino):
    global laser

    if (laser == False) | (laser == None):
        laser = True
        arduino.write(b'7')
    else:
        laser = False
        arduino.write(b'8')