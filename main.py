# Librerías
from Interfaz.VentanaBienvenida import VentanaRegistro
#from Interfaz.VentanaPrincipal import VentanaControlMicroscopio
from Interfaz.funciones.ControlArduino import automatizacion


def abrir_ventana_principal(nombre, apellido, correo):
    automatizacion.almacenar_datos_usuario(nombre, apellido, correo)

    #movimiento_motores = automatizacion.movimiento_motores
    #estado_laser = automatizacion.estado_laser
    #lectura_ultimas_coordenadas = automatizacion.lectura_ultimas_coordenadas()
    #arduino = automatizacion.deteccion_arduino()
  #  foto_camara = capturaCamara.capturaImagen
   # cerrar_camara = capturaCamara.liberarCamara
    #capturaCamara.configuracionCamara()

    #ventana_principal = VentanaControlMicroscopio(nombre)
    #ventana_principal = VentanaControlMicroscopio(nombre, arduino, movimiento_motores, estado_laser, 
    #                                              lectura_ultimas_coordenadas, foto_camara, cerrar_camara)
    #ventana_principal.mainloop()


if __name__=="__main__":
    app_bienvenida = VentanaRegistro(abrir_ventana_principal("Investigador", "Anónimo", "anonimous@correo.com"))
    app_bienvenida.mainloop()