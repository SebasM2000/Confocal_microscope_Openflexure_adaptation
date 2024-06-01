# Librería
from picamera import PiCamera
from picamera import PiRGBArray
import numpy as np
import datetime as dt
import time
import os

# Configuración de la cámara
camara = PiCamera()
camara.resolution(640, 480)
camara.framerate(32)
captura_arreglo = PiRGBArray(camara, size = (640, 480))

# Tiempo de inicio de la cámara
time.sleep(0.1)

# Matriz que almacena la imagen del plano xy
matriz_imagen = np.zeros((480, 640), dtype = np.uint8)

# Construccion imagen 2D
def construccionImg2D():
    camara.capture(raw_capture, format = "rgb")
    imagen = raw_capture.array
    imagenGris = np.dot(imagen[..., :3], [0.2989, 0.5870, 0.1140])
    intensidadMedia = np.mean(imagenGris)
    raw_capture.truncate(0)
    return intensidadMedia

# Tomar foto
def nombreFoto(ruta):
    marcaTiempo = int(time.time() * 1000)
    nombreCaptura = f"Captura_{marcaTiempo}.jpg"
    rutaCaptura = os.path.join(ruta, nombreCaptura)
    #camara.capture(rutaCaptura)

# Iniciar/Detener video
def iniciarVideo(ruta):
    nombreVideo = os.path.join(ruta, dt.datetime.now().strfname("%Y-%m-%d_%M.%S.h264"))
    camara.start_recording(nombreVideo)

def detenerVideo(t):
    time.sleep(t)
    camara.stop_recording()