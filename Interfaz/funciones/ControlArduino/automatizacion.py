# Librerías control arduino
import serial
import time
import os
#import ProcesamientoImg.capturaCamara


# Variables globales
ultima_posicion_x, ult_posicion_y, ult_posicion_z = 0, 0, 0  # Última posicion
max_x, max_y, max_z = 5000, 5000, 5000                       # Límite superior
t = 0.1                                                     # Tiempo en segundos de descanso entre cada paso
arduino = None


# Datos usuario
def almacenar_datos_usuario(nombre, apellido, correo):
    datos_usuario = []
    datos_usuario.append(nombre)
    datos_usuario.append(apellido)
    datos_usuario.append(correo)

    # Guardar datos del usuario en archivo .txt
    with open("datosUsuario.txt", "w") as file:
        file.write(" ".join(datos_usuario))


# Arduino
def deteccion_arduino():
    #puertos = serial.tools.list_ports.comports()
    #for puerto in puertos:
    #    print(puerto.device, puerto.description, puerto.manufacturer, puerto.product)
    #    if 'Arduino' in puerto.description:
    #        # Configuración arduino
    #        arduino =  serial.Serial(puerto.device, baudrate = 9600, timeout = 1)
    #        time.sleep(2)
    #        return arduino
        
    #return None
    serie = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 1)
    return serie


# Coordenadas motores
def almacenar_coordenadas(x, y, z):
    with open("coordenadas.txt", "w") as file:
        file.write(f"{x}, {y}, {z}")

def lectura_ultimas_coordenadas():
    try:
        print("Buscando archivo en: ", os.path.abspath("coordenadas.txt"))
        with open("coordenadas.txt", "r") as file:
            ultimas_coordenadas = file.read().split(",")

            if ultimas_coordenadas:
                return ultimas_coordenadas
                    
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None
    
    
# Movimiento motores
def movimiento_motores(x_i, y_i, z_i, x_f, y_f, z_f):
    global max_x, max_y, max_z, arduino

    if not arduino:
        arduino = deteccion_arduino()

    if x_i == None:
        x_i = 0

    elif y_i == None:
        y_i = 0

    elif z_i == None:
        z_i = 0


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
def estado_laser(laser):
    global arduino

    if not arduino:
        arduino = deteccion_arduino()

    if (laser == False) | (laser == None):
        arduino.write(b'7')
        print("Láser encendido.")
    else:
        arduino.write(b'8')
        print("Láser apagado.")


def medicion_automatica(x, y, z, dim_x, dim_y, dim_z):
    contador = 0

    x_i = x
    y_i = y

    print(f"Dimensiones registradas: {dim_x} * {dim_y} * {dim_z}")
    for k in range(dim_z):
        y = y_i
        for j in range(dim_y):
            x = x_i
            for i in range(dim_x):
                print(f"Foto tomada en: x = {x}, y = {y}, z = {z}")
                contador += 1
                x += 1

            y += 1

        z += 1

    print(f"Mediciones realizadas: {contador}")


def cerrar_arduino():
    global arduino

    if arduino:
        arduino.close()