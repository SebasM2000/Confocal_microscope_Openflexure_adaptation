# Librerías control arduino
import serial
import time
import threading
import os
import sys

# Obtiene la ruta absoluta del archivo actual
ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_carpeta_planificador = os.path.join(ruta_base, "..", "ProcesamientoImg")

# Agrega la ruta del archivo planificador al Path
sys.path.append(ruta_carpeta_planificador)

import planificador_capturas as pc


# Variables globales
arduino = None
baudRate = 115200
puertoSerial = "/dev/ttyACM0"
t = 2                                         # Tiempo en segundos de descanso entre cada paso
max_x, max_y, max_z = 5000, 5000, 5000        # Límites microscopio
Captura_n = 10 # Captura cada 10 pasos


# Arduino
def deteccion_arduino():
    try:
        arduino = serial.Serial(puertoSerial, baudRate, timeout=1)
        time.sleep(2)
        arduino.flushInput()

        # Espera mensaje de inicialización
        inicio = time.time()
        while time.time() - inicio < t:
            if arduino.in_waiting > 0:
                line = arduino.readline().decode.strip()
                if "ARDUINO_READY" in line:
                    return arduino
        return None

    except Exception as e:
        print(f"Error conectando Arduino: {e}")
        return None


# Movimiento motores
def movimiento_motores(x_i, y_i, z_i, x_f, y_f, z_f):
    global max_x, max_y, max_z, arduino

    if not arduino:
        arduino = deteccion_arduino()
        if not arduino:
            print("Arduino no conectado.")
            return False

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

    # Calcula pasos necesarios
    pasos_x = x_f - x_i
    pasos_y = y_f - y_i
    pasos_z = z_f - z_i

    try:
        # Envía comando
        comando = f"M{pasos_x}, {pasos_y}, {pasos_z}\n"
        arduino.write(comando.encode())

        # Espera confirmación
        inicio = time.time()
        while time.time() - inicio < t:
            if arduino.in_waiting > 0:
                respuesta = arduino.readline().decode().strip()
                if respuesta == "OK":
                    almacenar_coordenadas(x_f, y_f, z_f)
                    return True
                elif respuesta != "":
                    print(f"Respuesta inesperada: {respuesta}")

        print("Esperando respuesta Arduino")
        return False

    except Exception as e:
        print(f"Error en movimiento: {e}")
        return False
        

# Control del láser
def estado_laser(encender):
    global arduino

    try:
        comando = "LASER_ON\n" if encender else "LASER_OFF\n"
        arduino.write(comando.encode())
        
        # Espera confirmación
        respuesta_esperada = "LASER_ON_OK" if encender else "LASER_OFF_OK"
        inicio = time.time()
        while time.time() - inicio < t:
            if arduino.in_waiting > 0:
                respuesta = arduino.readline().decode().strip()
                if respuesta == respuesta_esperada:
                    return True
        
        print("Timeout control láser")
        return False
        
    except Exception as e:
        print(f"Error control láser: {e}")
        return False


# Función asíncrona
def movimiento_motores_async(x_i, y_i, z_i, x_f, y_f, z_f):
    thread = threading.Thread(target=movimiento_motores, 
                             args=(x_i, y_i, z_i, x_f, y_f, z_f))
    thread.daemon = True
    thread.start()


# Datos usuario
def almacenar_datos_usuario(nombre, apellido, correo):
    datos_usuario = []
    datos_usuario.append(nombre)
    datos_usuario.append(apellido)
    datos_usuario.append(correo)

    # Guardar datos del usuario en archivo .txt
    with open("datosUsuario.txt", "w") as file:
        file.write(" ".join(datos_usuario))


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