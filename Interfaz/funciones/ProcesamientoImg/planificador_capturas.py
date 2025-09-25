import threading
import time
from queue import Queue
import sys
import os

# Añadir ruta para importar capturaCamara
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ControlArduino"))
import capturaCamara as camara

class PlanificadorCapturas:
    def __init__(self):
        self.cola_capturas = Queue()
        self.en_ejecucion = False
        self.hilo_capturas = None
        self.capturas_exitosas = 0
        self.capturas_fallidas = 0

    def programar_capturas(self, x, y, z, ruta_carpeta):
        # Añade una captura a la cola de procesamiento
        self.cola_capturas.put({
            "x": x,
            "y": y,
            "z": z,
            "ruta_carpeta": ruta_carpeta,
            "timestamp": time.time()
        })
        print(f"Captura tomada en X:{x}, Y:{y}, Z:{z}")

    def iniciar(self):
        # Iniciar el hilo de procesamiento de capturas
        if not self.en_ejecucion:
            self.en_ejecucion = True
            self.hilo_capturas = threading.Thread(target = self._procesar_cola)
            self.hilo_capturas.daemon = True
            self.hilo_capturas.start()
            print("Planificador de capturas iniciado")

    def detener(self):
        # Detiene planificador de capturas
        self.en_ejecucion = False
        if self.hilo_capturas:
            self.hilo_capturas.join(timeout = 10)
        
        print(f"Planificador detenido. Capturas: {self.capturas_exitosas}\n Fallidas: {self.capturas_fallidas}")

    def estadisticas(self):
        # Estadísticas de capturas
        return {
            "exitosas": self.capturas_exitosas,
            "fallidas": self.capturas_fallidas,
            "en_cola": self.cola_capturas.qsize()
        }

    def _procesar_cola(self):
        # Procesa la cola de capturas en segundo plano
        print("Iniciando procesamiento de cola de capturas...")

        while self.en_ejecucion or not self.cola_capturas.empty():
            try:
                if not self.cola_capturas.empty():
                    captura = self.cola_capturas.get_nowait()

                    # Verificar que la carpeta existe
                    os.makedirs(captura["ruta_carpeta"], exist_ok = True)

                    # Ejecutar captura
                    exito = camara.capturar_foto(
                        captura["ruta_carpeta"],
                        "muestra",
                        captura["x"],
                        captura["y"],
                        captura["z"]
                    )

                    if exito:
                        self.capturas_exitosas += 1
                    else:
                        self.capturas_fallidas += 1

                    self.cola_capturas.task_done()
                    time.sleep(0.5) # Pausa entre capturas
                else:
                    time.sleep(0.1) # Pequeña pausa si la cola está vacía

            except Exception as e:
                print(f"Error procesando cola: {e}")


# Instancia global del planificador
planificador = PlanificadorCapturas()