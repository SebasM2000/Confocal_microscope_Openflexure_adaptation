# Librería
from picamera import PiCamera
import datetime as dt
import time
import os

cam = PiCamera()

# Tomar foto
def tomarFoto(ruta):
    marcaTiempo = int(time.time() * 1000)
    nombreCaptura = f"Captura_{marcaTiempo}.jpg"
    rutaCaptura = os.path.join(ruta, nombreCaptura)
    cam.capture(rutaCaptura)

# Iniciar/Detener video
def iniciarVideo(ruta):
    nombreVideo = os.path.join(ruta, dt.datetime.now().strfname("%Y-%m-%d_%M.%S.h264"))
    cam.start_recording(nombreVideo)

def detenerVideo(t):
    time.sleep(t)
    cam.stop_recording()