# Librerías
import tkinter as tk
from tkinter import filedialog
import os
import time

# variables globales
color_ventana_principal = "#b2e1fa"
color_frame = "#4d2db3"
fuente = "TimesNewRoman "

# Control del láser
laser = False

class VentanaControlMicroscopio(tk.Tk):
    def __init__(self, nombre, automatizacion, foto_camara, cerrar_camara):
        super().__init__()
        #self.arduino = arduino
        #self.datos_retorno_arduino = movimiento_motores
        #self.estado_laser = estado_laser
        #self.ultimas_coordenadas = lectura_ultimas_coordenadas
        self.automatizacion = automatizacion
        self.foto_camara = foto_camara
        self.cerrar_camara = cerrar_camara
        #self.automatizacion.saludo()

        # Configuración
        self.title("Ventana de Control")
        self.geometry("750x500")

        self.resizable(0, 0)
        self.config(bg = color_ventana_principal, cursor = "dot")


        #------Etiquetas, botones y entradas------#

        self.mensaje_bienvenida = tk.Label(self, text = "Bienvenido, " + nombre, 
                                           font = "TimesNewRoman 20 italic", bg = color_ventana_principal)
        self.mensaje_bienvenida.place(x = 150, y = 50)

        # Motores
        self.etiqueta_posicion_motores = tk.Label(self, text = "Posición motores:", 
                                                  bg = color_ventana_principal, font = fuente + "12")
        self.etiqueta_posicion_motores.place(x = 120, y = 170)

        self.etiqueta_posicion_x = tk.Label(self, text = "X", bg = color_ventana_principal, font = fuente + "10")
        self.etiqueta_posicion_x.place(x = 290, y = 150)

        self.etiqueta_posicion_y = tk.Label(self, text = "Y", bg = color_ventana_principal, font = fuente + "10")
        self.etiqueta_posicion_y.place(x = 350, y = 150)

        self.etiqueta_posicion_z = tk.Label(self, text = "Z", bg = color_ventana_principal, font = fuente + "10")
        self.etiqueta_posicion_z.place(x = 410, y = 150)

        # Puertos de almacenamiento
        self.etiqueta_almacenamiento = tk.Label(self, text = "Selecciona una carpeta \n de almacenamiento:", 
                                                bg = color_ventana_principal, font = fuente + "10")
        self.etiqueta_almacenamiento.place(x = 118, y = 285)

        # Dimensiones de la muestra
        self.etiqueta_medida_muestra = tk.Label(self, text = "Área de medición: ", 
                                                     bg = color_ventana_principal, font = fuente + "12")
        self.etiqueta_medida_muestra.place(x = 120, y = 230)

        self.etiqueta_medida_muestra_x = tk.Label(self, text = "Largo", bg = color_ventana_principal, font = fuente + "9")
        self.etiqueta_medida_muestra_x.place(x = 278, y = 210)

        self.etiqueta_medida_muestra_y = tk.Label(self, text = "Ancho", bg = color_ventana_principal, font = fuente + "9")
        self.etiqueta_medida_muestra_y.place(x = 335, y = 210)

        self.etiqueta_medida_muestra_z = tk.Label(self, text = "Alto", bg = color_ventana_principal, font = fuente + "9")
        self.etiqueta_medida_muestra_z.place(x = 400, y = 210)


        #------Entradas------#

        # Motores
        self.entrada_motor_x = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_x.insert(0, "0")
        self.entrada_motor_x.place(x = 280, y = 172)
        #self.entrada_motor_x.bind("<Return>", self.verificacion_valor_motor)
    
        self.entrada_motor_y = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_y.insert(0, "0")
        self.entrada_motor_y.place(x = 340, y = 172)
        #self.entrada_motor_y.bind("<Return>", self.verificacion_valor_motor)
    
        self.entrada_motor_z = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_z.insert(0, "0")
        self.entrada_motor_z.place(x = 400, y = 172)
        #self.entrada_motor_z.bind("<Return>", self.verificacion_valor_motor)

        # Dimensiones de la muestra
        self.entrada_medida_x = tk.Entry(self, bd = 2, width = 5)
        self.entrada_medida_x.insert(0, "0")
        self.entrada_medida_x.place(x = 280, y = 232)

        self.entrada_medida_y = tk.Entry(self, bd = 2, width = 5)
        self.entrada_medida_y.insert(0, "0")
        self.entrada_medida_y.place(x = 340, y = 232)

        self.entrada_medida_z = tk.Entry(self, bd = 2, width = 5)
        self.entrada_medida_z.insert(0, "0")
        self.entrada_medida_z.place(x = 400, y = 232)


        # -----Botones-----#

        self.boton_retorno_origen = tk.Button(self, text = "Mover motores al origen", bg = "#e1e7eb")
        self.boton_retorno_origen.place(x = 485, y = 168)

        self.boton_examinar = tk.Button(self, text = "Examinar", bg = "#e1e7eb", padx= 50, command = self.examinar_carpeta)
        self.boton_examinar.place(x = 280, y = 290)

        self.boton_iniciar_medicion = tk.Button(self, text = "Iniciar medición", bg = "#AFF3B2")
        self.boton_iniciar_medicion.place(x = 350, y = 360)

        self.boton_estado_laser = tk.Button(self, text = "Encender/Apagar Láser", bg = "#e1e7eb")
        self.boton_estado_laser.place(x = 135, y = 410)

        self.boton_captura = tk.Button(self, text = "Tomar foto", bg = "#e1e7eb")
        self.boton_captura.place(x = 365, y = 410)

        self.boton_salir = tk.Button(self, text = "Salir", bg = "#bb9778", command = self.destroy)
        self.boton_salir.place(x = 570, y = 410)


    # Sustitución últimas posiciones en las entradas X, Y, Z
    def visualizacionUltPos(self):
        # Lectura de últimas coordenadas en el archivo .txt
        self.entrada_motor_x.delete(0, tk.END)
        self.entrada_motor_x.insert(0, str(self.ultimas_coordenadas[0]))

        self.entrada_motor_y.delete(0, tk.END)
        self.entrada_motor_y.insert(0, str(self.ultimas_coordenadas[1]))

        self.entrada_motor_z.delete(0, tk.END)
        self.entrada_motor_z.insert(0, str(self.ultimas_coordenadas[2]))



    def advertencia(self):
        self.mensajeAdvertencia = tk.Label(self, text = "Ingresar un dato numérico",
                                        font = "TimesNewRoman 15 italic", bg = color_ventana_principal, fg = "red")
        self.mensajeAdvertencia.place(x = 250, y = 150)

        # Situar temporizador para que desaparezca esta alerta


    #-----Funciones de control del arduino-----#

    # Ingresado en entradas
    def verificacion_valor_motor(self):
        motor_x = self.entrada_motor_x.get()
        motor_y = self.entrada_motor_y.get()
        motor_z = self.entrada_motor_z.get()
        
        try:
            motor_x = int(motor_x)
            motor_y = int(motor_y)
            motor_z = int(motor_z)
            
        except:
            self.advertencia()
        else:
            self.datos_retorno_arduino(self.arduino, motor_x, motor_y, motor_z)
    
    
    # Regreso al origen de los motores
    def reinicio_posicion_motores(self):
        motor_x = self.entrada_motor_x.get()
        motor_y = self.entrada_motor_y.get()
        motor_z = self.entrada_motor_z.get()

        motor_x.delete(0, tk.END)
        motor_x.insert(0, "0")

        motor_y.delete(0, tk.END)
        motor_y.insert(0, "0")

        motor_z.delete(0, tk.END)
        motor_z.insert(0, "0")

        self.datos_retorno_arduino(self.arduino, motor_x, motor_y, motor_z)

    
    # Examinar carpeta
    def examinar_carpeta(self):
        rutaCarpeta = filedialog.askdirectory()

        if rutaCarpeta:
            self.etiqueta_carpeta = tk.Label(self, text = f"{rutaCarpeta}", font = fuente + "8", bg = color_ventana_principal)
            self.etiqueta_carpeta.place(x = 270, y = 320)

            
if __name__ == "__main__":
    ventanaMicroscopio = VentanaControlMicroscopio("Usuario", None, None, None)
    ventanaMicroscopio.mainloop()