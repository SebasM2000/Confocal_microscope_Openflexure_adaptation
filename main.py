# Librerías
from ControlArduino import automatizacion
from Interfaz.VentanaBienvenida import VentanaRegistro
from Interfaz.VentanaPrincipal import VentanaControlMicroscopio
import ProcesamientoImg.CamaraRB
import ProcesamientoImg.capturaCamara


def abrir_ventana_principal(nombre, apellido, correo):
    automatizacion.almacenar_datos_usuario(nombre, apellido, correo)

    movimiento_motores = automatizacion.movimiento_motores
    estado_laser = automatizacion.estado_laser
    lectura_ultimas_coordenadas = automatizacion.lectura_ultimas_coordenadas()
    arduino, puerto_arduino = automatizacion.deteccion_arduino()

    ventana_principal = VentanaControlMicroscopio(nombre, arduino, puerto_arduino, movimiento_motores, 
                                                  estado_laser, lectura_ultimas_coordenadas)
    ventana_principal.mainloop()


if __name__=="__main__":
    app_bienvenida = VentanaRegistro(abrir_ventana_principal("Investigador", "Anónimo", "Anonimous@correo.com"))
    app_bienvenida.mainloop()