# Librería
import capturaCamara as cc
import numpy as np
import datetime as dt
import time
import os
import psutil

# Matriz que almacena la imagen del plano xy
matriz_imagen = np.zeros((480, 640), dtype = np.uint8)

# Detección dispositivos USB
def deteccionUSB():
    dispositivosActuales = set(partition.device for partition in psutil.disk_partitions())
    

# Construccion imagen 2D
def construccionImg2D():
    camara.capture(raw_capture, format = "rgb")
    imagen = raw_capture.array
    imagenGris = np.dot(imagen[..., :3], [0.2989, 0.5870, 0.1140])
    intensidadMedia = np.mean(imagenGris)
    raw_capture.truncate(0)
    return intensidadMedia

# Tomar foto
def nombreImagenZ(nombreInterfaz, z):
    zMicras = int(z * 1000) # Conversión de milímetros a micras para eliminar decimales
    nombreCaptura = f"{nombreInterfaz}_Z{zMicras}.jpg"
    rutaCaptura = os.path.join(ruta, nombreCaptura)

# Iniciar/Detener video
def iniciarVideo(ruta):
    nombreVideo = os.path.join(ruta, dt.datetime.now().strfname("%Y-%m-%d_%M.%S.h264"))
    camara.start_recording(nombreVideo)