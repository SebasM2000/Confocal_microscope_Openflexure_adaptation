import subprocess
import time
from datetime import datetime
import os


def capturar_foto(ruta_carpeta, nombre_base = "muestra", x=0, y=0, z=0):
    try:
        # Asegura que la carpeta existe
        os.makedirs(ruta_carpeta, exist_ok = True)

        # Crea nombre de archivo con coordenadas y timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"{nombre_base}_X{x}_Y{y}_Z{z}_{timestamp}.jpg"
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

        # Captura foto
        comando = [
            "libcamera-still",
            "-o", ruta_completa,
            "--width", "3280", # Máxima resolución
            "--height", "2464",
            "--quality", "95", # Calidad JPEG
            "--nopreview",
            "--timeout", "1000",
            "--denoise", "cdn_off"
        ]

        resultado = subprocess.run(comando, capture_output = True, text = True,
        timeout = 15)

        if resultado.returncode == 0:
            print(f"Foto capturada: {nombre_archivo}")
            return True
        else:
            print(f"Error capturando foto: {resultado.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("Se excedió el tiempo estimado de respuesta.")
        return False
    except Exception as e:
        print(f"Error al capturar la foto: {e}")
        return False


# Comprobación de correcto funcionamiento de la cámara
def probar_camara():

    print("Probando cámara Raspberry...")
    resultado = capturar_foto("/tmp", "test_camara")

    if resultado:
        print("Cámara lista para usar :)")
    else:
        print("Error. Verifica que la cámara esté correctamente conectada.")

    return resultado


# Ejecución rápida de cámara
if __name__ == "__main__":
    probar_camara()