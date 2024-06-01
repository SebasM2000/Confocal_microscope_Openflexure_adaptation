import numpy as np
import picamera
from PIL import Image

def capture_image_to_array():
    # Inicializar la cámara
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        
        # Crear un array para almacenar la imagen
        image_array = np.empty((480, 640, 3), dtype=np.uint8)
        
        # Capturar la imagen
        camera.capture(image_array, 'rgb')
        
    return image_array

def save_array_as_image(image_array, output_path):
    # Convertir el array en una imagen usando PIL
    image = Image.fromarray(image_array)
    
    # Guardar la imagen
    image.save(output_path)

def main():
    # Capturar la imagen y guardarla en un array
    image_array = capture_image_to_array()
    
    # Guardar el array como una imagen
    output_path = "captured_image.jpg"
    save_array_as_image(image_array, output_path)
    print(f"Imagen guardada en {output_path}")

if __name__ == "__main__":
    main()
