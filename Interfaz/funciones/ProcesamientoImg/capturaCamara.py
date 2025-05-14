import numpy as np
#from picamera2 import Picamera2
from PIL import Image
import time

#picam2 = Picamera2()

# Configuración cámara
def configuracionCamara():
    stillConfig = picam2.create_still_configuration(main = {"size": (640, 480)})
    picam2.configure(stillConfig)
    picam2.framerate = 32


def capturaImagen(num_imagenes, array_imagen, nombre_imagen, ruta):
    # Captura
    picam2.start()

    for i in range(num_imagenes):
        array_imagen = picam2.capture_array()
        imagen = Image.fromarray(array_imagen)
        imagen.save(nombre_imagen + "_%d", i)
        print(f"Imagen guardada en {ruta}")
        time.sleep(0.1)
    
    picam2.stop()
    

# Libera la cámara
def liberarCamara(camara):
    camara.close()