# Librerías
import tkinter as tk
from tkinter import filedialog
import funciones.ControlArduino.automatizacion as auto
import time

# variables globales
color_ventana_principal = "#b2e1fa"
color_frame = "#4d2db3"
fuente = "TimesNewRoman "

# Ultima posición de los motores
motor_xi = None
motor_yi = None
motor_zi = None

# Estado inicial del láser
laser = False

# Estado inicial Cámara Raspberry
camara = True

# Ruta de la carpeta de almacenamiento de las imágenes
ruta_carpeta = None


class VentanaControlMicroscopio(tk.Tk):
    def __init__(self, nombre):
        super().__init__()

        # Configuración
        self.title("Ventana de Control")
        self.geometry("750x500")

        self.resizable(0, 0)
        self.config(bg = color_ventana_principal, cursor = "dot")


        #-----------------------------------------#
        #      Etiquetas, botones y entradas      #
        #-----------------------------------------#

        # Etiquetas
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


        #--------------------#
        #-     Entradas     -#
        #--------------------#

        # Motores
        self.entrada_motor_x = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_x.place(x = 280, y = 172)
        self.entrada_motor_x.bind("<Return>", self.verificacion_valor_motor)
    
        self.entrada_motor_y = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_y.place(x = 340, y = 172)
        self.entrada_motor_y.bind("<Return>", self.verificacion_valor_motor)
    
        self.entrada_motor_z = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_z.place(x = 400, y = 172)
        self.entrada_motor_z.bind("<Return>", self.verificacion_valor_motor)

        # Dimensiones de la muestra
        self.entrada_med_x = tk.Entry(self, bd = 2, width = 5)
        self.entrada_med_x.insert(0, "0")
        self.entrada_med_x.place(x = 280, y = 232)
        self.entrada_med_x.bind("<Return>", self.medicion_muestra)

        self.entrada_med_y = tk.Entry(self, bd = 2, width = 5)
        self.entrada_med_y.insert(0, "0")
        self.entrada_med_y.place(x = 340, y = 232)
        self.entrada_med_y.bind("<Return>", self.medicion_muestra)

        self.entrada_med_z = tk.Entry(self, bd = 2, width = 5)
        self.entrada_med_z.insert(0, "0")
        self.entrada_med_z.place(x = 400, y = 232)
        self.entrada_med_z.bind("<Return>", self.medicion_muestra)

        self.visualizacionUltPos()


        #-------------------#
        #-     Botones     -#
        #-------------------#

        self.boton_retorno_origen = tk.Button(self, text = "Mover motores al origen", bg = "#e1e7eb")
        self.boton_retorno_origen.place(x = 485, y = 168)

        self.boton_examinar = tk.Button(self, text = "Examinar", bg = "#e1e7eb", padx= 50, command = self.examinar_carpeta)
        self.boton_examinar.place(x = 280, y = 290)

        self.boton_iniciar_medicion = tk.Button(self, text = "Iniciar medición", bg = "#AFF3B2", command = self.medicion_muestra)
        self.boton_iniciar_medicion.place(x = 350, y = 360)

        self.boton_estado_laser = tk.Button(self, text = "Encender Láser", bg = "red", command = self.estado_laser)
        self.boton_estado_laser.place(x = 135, y = 410)

        self.boton_captura = tk.Button(self, text = "Tomar foto de prueba", bg = "#e1e7eb")
        self.boton_captura.place(x = 491, y = 230)

        self.boton_encender_camara = tk.Button(self, text = "Encender cámara", bg = "red", command = self.estado_camara)
        self.boton_encender_camara.place(x = 348, y = 410)

        self.boton_salir = tk.Button(self, text = "Salir", bg = "#bb9778", command = self.salir)
        self.boton_salir.place(x = 570, y = 410)

    #-----------------------------#
    #-          METODOS          -#
    #-----------------------------#

    # Sustitución últimas posiciones en las entradas X, Y, Z
    def visualizacionUltPos(self):
        global motor_xi, motor_yi, motor_zi

        # Lectura de últimas coordenadas en el archivo .txt
        ultimas_coordenadas = auto.lectura_ultimas_coordenadas()
        print(ultimas_coordenadas)

        motor_xi = ultimas_coordenadas[0]
        motor_yi = ultimas_coordenadas[1]
        motor_zi = ultimas_coordenadas[2]

        self.entrada_motor_x.delete(0, tk.END)
        self.entrada_motor_x.insert(0, motor_xi)

        self.entrada_motor_y.delete(0, tk.END)
        self.entrada_motor_y.insert(0, motor_yi)

        self.entrada_motor_z.delete(0, tk.END)
        self.entrada_motor_z.insert(0, motor_zi)

        motor_xi, motor_yi, motor_zi = int(motor_xi), int(motor_yi), int(motor_zi)


    def advertencia(self):
        self.mensaje_advertencia = tk.Label(self, text = "Ingresar un dato numérico",
                                        font = "TimesNewRoman 15 italic", bg = color_ventana_principal, fg = "red")
        self.mensaje_advertencia.place(x = 250, y = 150)

        time.sleep(2)

        self.mensaje_advertencia.place_forget()

    #--------------------------------------------#
    #      Funciones de control del arduino      #
    #--------------------------------------------#

    # Ingresado en entradas
    def verificacion_valor_motor(self, event=None):
        global motor_xi, motor_yi, motor_zi

        motor_xf = self.entrada_motor_x.get()
        motor_yf = self.entrada_motor_y.get()
        motor_zf = self.entrada_motor_z.get()
        
        try:
            motor_xf = int(motor_xf)
            motor_yf = int(motor_yf)
            motor_zf = int(motor_zf)
            
        except:
            self.advertencia()
        else:
            auto.movimiento_motores(motor_xi, motor_yi, motor_zi, motor_xf, motor_yf, motor_zf)
            motor_xi = motor_xf
            motor_yi = motor_yf
            motor_zi = motor_zf
    
    
    # Regreso al origen de los motores
    def reinicio_posicion_motores(self):
        global motor_xi, motor_yi, motor_zi

        motor_xf = self.entrada_motor_x.get()
        motor_yf = self.entrada_motor_y.get()
        motor_zf = self.entrada_motor_z.get()

        motor_xf.delete(0, tk.END)
        motor_xf.insert(0, "0")

        motor_yf.delete(0, tk.END)
        motor_yf.insert(0, "0")

        motor_zf.delete(0, tk.END)
        motor_zf.insert(0, "0")

        auto.movimiento_motores(int(motor_xi), int(motor_yi), int(motor_zi), 
                                int(motor_xf), int(motor_yf), int(motor_zf))
        motor_xi = motor_xf
        motor_yi = motor_yf
        motor_zi = motor_zf

    
    # Examinar carpeta
    def examinar_carpeta(self):
        global ruta_carpeta

        ruta_carpeta = filedialog.askdirectory()

        if ruta_carpeta:
            self.etiqueta_carpeta = tk.Label(self, text = f"{ruta_carpeta}", font = fuente + "8", bg = color_ventana_principal)
            self.etiqueta_carpeta.place(x = 270, y = 320)

    
    def estado_laser(self):
        global laser
        self.boton_estado_laser.place_forget()

        if laser == False:
            auto.estado_laser(laser)
            self.boton_estado_laser = tk.Button(self, text = "Apagar Láser", bg = "green", command = self.estado_laser)
            self.boton_estado_laser.place(x = 135, y = 410)
            laser = True
        else:
            auto.estado_laser(laser)
            self.boton_estado_laser = tk.Button(self, text = "Encender Láser", bg = "red", command = self.estado_laser)
            self.boton_estado_laser.place(x = 135, y = 410)
            laser = False

    
    def estado_camara(self):
        global camara
        self.boton_encender_camara.place_forget()

        if camara == True:
            self.boton_encender_camara = tk.Button(self, text = "Apagar cámara", bg = "green", command = self.estado_camara)
            self.boton_encender_camara.place(x = 353, y = 410)
            camara = False
        else:
            self.boton_encender_camara = tk.Button(self, text = "Encender cámara", bg = "red", command = self.estado_camara)
            self.boton_encender_camara.place(x = 348, y = 410)
            camara = True

    
    # Medición automática de la muestra
    def medicion_muestra(self):
        global laser

        try:
            ruta_carpeta.upper()

            dim_x = self.entrada_med_x.get()
            dim_y = self.entrada_med_y.get()
            dim_z = self.entrada_med_z.get()

            motor_xi = self.entrada_motor_x.get()
            motor_yi = self.entrada_motor_y.get()
            motor_zi = self.entrada_motor_z.get()

            if (int(dim_x) == 0) or (int(dim_y) == 0) or (int(dim_z) == 0):
                self.etiqueta_carpeta = tk.Label(self, text = "Las dimensiones de la muestra no pueden ser cero", 
                                             font = fuente + "10", bg = color_ventana_principal)
                self.etiqueta_carpeta.place(x = 270, y = 320)
            else:
                if laser == True:
                    laser = False
                    #self.estado_laser()
                auto.medicion_automatica(int(motor_xi), int(motor_yi), int(motor_zi), int(dim_x), int(dim_y), int(dim_z))
            
        except AttributeError:
            self.etiqueta_carpeta = tk.Label(self, text = "Por favor seleccionar una carpeta para almacenar las imágenes", 
                                             font = fuente + "8", bg = color_ventana_principal)
            self.etiqueta_carpeta.place(x = 270, y = 320)

            self.after(2000, lambda: self.etiqueta_carpeta.place_forget())


    def salir(self):
        auto.cerrar_arduino()
        self.destroy()

            
if __name__ == "__main__":
    ventanaMicroscopio = VentanaControlMicroscopio("Usuario")
    ventanaMicroscopio.mainloop()