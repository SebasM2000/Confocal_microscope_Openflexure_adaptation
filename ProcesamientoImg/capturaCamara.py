import numpy as np
from picamera2 import Picamera2
from PIL import Image
import time

def configuracionCamara():
    # Configuración cámara
    picam2 = Picamera2()
    stillConfig = picam2.create_still_configuration(main = {"size": (640, 480)})
    picam2.configure(stillConfig)
    picam2.framerate = 32

def capturaImagen():
    # Tiempo de inicio de cámara
    time.sleep(0.1)

    # Captura
    picam2.start()
    arrayImagen = picam2.capture_array()
    picam2.stop()
    
    return arrayImagen


# Transformar array en imagen y guardar
def guardarArrayComoImagen(arrayImagen, nombreImagen, ruta):
    imagen = Image.fromarray(arrayImagen)
    imagen.save(nombreImagen)
    print(f"Imagen guardada en {ruta}")


# Libera la cámara
def liberarCamara(camara):
    camara.close()