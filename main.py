# Librerías
from ControlArduino import automatizacion
from Interfaz.VentanaBienvenida import VentanaRegistro
from Interfaz.VentanaPrincipal import VentanaControlMicroscopio
from ProcesamientoImg import capturaCamara


def abrir_ventana_principal(nombre, apellido, correo):
    automatizacion.almacenar_datos_usuario(nombre, apellido, correo)

    #movimiento_motores = automatizacion.movimiento_motores
    #estado_laser = automatizacion.estado_laser
    #lectura_ultimas_coordenadas = automatizacion.lectura_ultimas_coordenadas()
    #arduino = automatizacion.deteccion_arduino()
    foto_camara = capturaCamara.capturaImagen
    cerrar_camara = capturaCamara.liberarCamara
    capturaCamara.configuracionCamara()

    ventana_principal = VentanaControlMicroscopio(nombre, automatizacion, foto_camara, cerrar_camara)
    #ventana_principal = VentanaControlMicroscopio(nombre, arduino, movimiento_motores, estado_laser, 
    #                                              lectura_ultimas_coordenadas, foto_camara, cerrar_camara)
    ventana_principal.mainloop()


if __name__=="__main__":
    app_bienvenida = VentanaRegistro(abrir_ventana_principal("Investigador", "Anónimo", "Anonimous@correo.com"))
    app_bienvenida.mainloop()