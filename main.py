# Librerías
from ControlArduino import Automatizacion
from Interfaz.VentanaBienvenida import VentanaRegistro
from Interfaz.VentanaPrincipal import VentanaControlMicroscopio
import ProcesamientoImg.CamaraRB
import ProcesamientoImg.capturaCamara


def abrir_ventana_principal(nombre, apellido, correo):
    Automatizacion.almacenar_datos_usuario(nombre, apellido, correo)

    movimiento_motores = Automatizacion.movimiento_motores
    estado_laser = Automatizacion.estado_laser
    lectura_ultimas_coordenadas = Automatizacion.lectura_ultimas_coordenadas()
    arduino, puerto_arduino = Automatizacion.deteccion_arduino()

    ventana_principal = VentanaControlMicroscopio(nombre, arduino, puerto_arduino, movimiento_motores, 
                                                  estado_laser, lectura_ultimas_coordenadas)
    ventana_principal.mainloop()


if __name__=="__main__":
    app_bienvenida = VentanaRegistro(abrir_ventana_principal)
    app_bienvenida.mainloop()