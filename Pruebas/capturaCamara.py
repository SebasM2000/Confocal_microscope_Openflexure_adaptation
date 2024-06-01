import numpy as np
from picamera2 import Picamera2
from PIL import Image

def foto():
    def capture_image_to_array():
        picam2 = Picamera2()
        picam2.configure(picam2.create_still_configuration())
        picam2.start()
    
        image_array = picam2.capture_array()
    
        picam2.stop()
    
        return image_array

    def save_array_as_image(image_array, output_path):
        image = Image.fromarray(image_array)
    
        image.save(output_path)
    
    def main():
        image_array = capture_image_to_array()
    
        output_path = "captured_image.jpg"
        save_array_as_image(image_array, output_path)
        print(f"Imagen guardada en {output_path}")
    
    if __name__ == "__main__":
        main()