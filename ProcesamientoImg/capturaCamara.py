import numpy as np
from picamera2 import Picamera2
from PIL import Image
import time

def configuracionCapturaImagen():
    # Configuración cámara
    picam2 = Picamera2()
    stillConfig = picam2.create_still_configuration(main = {"size": (640, 480)})
    picam2.configure(stillConfig)
    picam2.framerate = 32

    # Tiempo de inicio de cámara
    time.sleep(0.1)

    # Captura
    picam2.start()
    arrayImagen = picam2.capture_array()
    picam2.stop()
    
    return arrayImagen

def save_array_as_image(arrayImagen, nombreImagen):
    image = Image.fromarray(arrayImagen)
    image.save(nombreImagen)
    
def main():
    image_array = configuracionCapturaImagen()
    
    nombreImagen = "hola.jpg"
    save_array_as_image(image_array, nombreImagen)
    print(f"Imagen guardada en {nombreImagen}")
    
if __name__ == "__main__":
    main()
        
