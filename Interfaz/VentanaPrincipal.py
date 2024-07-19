# Librerías
import tkinter as tk
import os
import time

# variables globales
color_ventana_principal = "#b2e1fa"
color_frame = "#4d2db3"
fuente = "Times New Roman 12"

# Control del láser
laser = False

class VentanaControlMicroscopio(tk.Tk):
    def __init__(self, nombre, arduino, puerto_arduino, movimiento_motores, estado_laser, ultimas_coordenadas):
        super().__init__()
        self.nombre = nombre
        self.arduino = arduino
        self.datos_retorno_arduino = movimiento_motores
        self.estado_laser = estado_laser
        self.ultimas_coordenadas = ultimas_coordenadas

        # Configuración
        self.title("Control microscopio")
        self.geometry("750x500")

        self.resizable(0, 0)
        self.config(bg = color_ventana_principal, cursor = "dot")


        #------Etiquetas, botones y entradas------#

        self.mensaje_bienvenida = tk.Label(self, text = "Bienvenido, " + self.nombre, 
                                           font = "TimesNewRoman 20 italic", bg = color_ventana_principal)
        self.mensaje_bienvenida.place(x = 150, y = 50)

        # Motores
        self.etiqueta_posicion_motores = tk.Label(self, text = "Posición motores:", 
                                                  bg = color_ventana_principal, font = fuente)
        self.etiqueta_posicion_motores.place(x = 140, y = 170)

        self.etiqueta_posicion_x = tk.Label(self, text = "X", bg = color_ventana_principal, font = fuente)
        self.etiqueta_posicion_x.place(x = 290, y = 150)

        self.etiqueta_posicion_y = tk.Label(self, text = "Y", bg = color_ventana_principal, font = fuente)
        self.etiqueta_posicion_y.place(x = 350, y = 150)

        self.etiqueta_posicion_z = tk.Label(self, text = "Z", bg = color_ventana_principal, font = fuente)
        self.etiqueta_posicion_z.place(x = 410, y = 150)

        # Puertos de almacenamiento
        self.etiqueta_almacenamiento = tk.Label(self, text = "Almacenamiento \n USB", 
                                                bg = color_ventana_principal, font = fuente)
        self.etiqueta_almacenamiento.place(x = 140, y = 285)

        self.etiqueta_almacenamiento_2 = tk.Label(self, text = ":", 
                                                  bg = color_ventana_principal, font = "TimesNewRoman 15")
        self.etiqueta_almacenamiento_2.place(x = 260, y = 290)

        # Dimensiones de la muestra
        self.etiqueta_medida_muestra = tk.Label(self, text = "Área de medición: ", 
                                                     bg = color_ventana_principal, font = fuente)
        self.etiqueta_medida_muestra.place(x = 140, y = 230)

        self.etiqueta_medida_muestra_x = tk.Label(self, text = "X", bg = color_ventana_principal, font = fuente)
        self.etiqueta_medida_muestra_x.place(x = 290, y = 210)

        self.etiqueta_medida_muestra_y = tk.Label(self, text = "Y", bg = color_ventana_principal, font = fuente)
        self.etiqueta_medida_muestra_y.place(x = 350, y = 210)

        self.etiqueta_medida_muestra_z = tk.Label(self, text = "Z", bg = color_ventana_principal, font = fuente)
        self.etiqueta_medida_muestra_z.place(x = 410, y = 210)


        #------Entradas------#

        # Motores
        self.entrada_motor_x = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_x.insert(0, "0")
        self.entrada_motor_x.place(x = 280, y = 172)
        self.entrada_motor_x.bind("<Return>", self.verificacion_valor_motor)
    
        self.entrada_motor_y = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_y.insert(0, "0")
        self.entrada_motor_y.place(x = 340, y = 172)
        self.entrada_motor_y.bind("<Return>", self.verificacion_valor_motor)
    
        self.entrada_motor_z = tk.Entry(self, bd = 2, width = 5)
        self.entrada_motor_z.insert(0, "0")
        self.entrada_motor_z.place(x = 400, y = 172)
        self.entrada_motor_z.bind("<Return>", self.verificacion_valor_motor)

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

        self.boton_salir = tk.Button(self, text = "Salir", command = self.destroy(), bg = "#bb9778")
        self.boton_salir.place(x = 570, y = 410)

        self.boton_retorno_origen = tk.Button(self, text = "Mover motores al origen", bg = "#e1e7eb",
                                command = self.reinicio_posicion_motores)
        self.boton_retorno_origen.place(x = 485, y = 168)

        self.boton_estado_laser = tk.Button(self, text = "Encender/Apagar Láser", bg = "#e1e7eb", command = controlLaser)
        self.boton_estado_laser.place(x = 135, y = 410)

        self.boton_captura = tk.Button(self, text = "Tomar foto", bg = "#e1e7eb", command = tomarCaptura)
        self.boton_captura.place(x = 365, y = 410)

        self.boton_iniciar_medicion = tk.Button(self, text = "Iniciar medición", bg = "#AFF3B2", command = automatizacion)
        self.boton_iniciar_medicion.place(x = 350, y = 360)

        # Menu desplegable para opciones de almacenamiento de imágenes
        #self.menu_opciones = tk.OptionMenu(self, SeleccionMemoria, *varOpciones)
        #self.menu_opciones.config(width = 18)
        #self.menu_opciones.place(x = 280, y = 290)

        #varOpciones = ["Seleccione memoria", "Memoria 1", "Memoria 2"]
        #SeleccionMemoria = StringVar()
        #SeleccionMemoria.set(varOpciones[0])


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
            self.movimiento_motores(self.arduino, motor_x, motor_y, motor_z)
    
    
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

        self.movimiento_motores(self.arduino, motor_x, motor_y, motor_z)


    # Control del láser
    def controlLaser():
        if (laser == False) | (laser == None):
            laser = True
            arduino.write(b'7')
        else:
            laser = False
            arduino.write(b'8')

    # Control Cámara
    def tomarCaptura():
        PiCam.main()

    
    # Medición automática de los motores
    def automatizacion():
        event = None
        global ult_pos_x, ult_pos_y, ult_pos_z, max_x, max_y, max_z, min_x, min_y, min_z
        medida_X, medida_Y, medida_Z = entradaMedida_X.get(), entradaMedida_Y.get(), entradaMedida_Z.get()

        #for k in range(ult_pos_z, max_z):
            #entradaMotor_Z()
            #tomarCaptura()

        for j in range(medida_Y):
            entradaMotor_Y()

            for i in range(medida_X):
                #pcrb.construccionImg2D()
                entradaMotor_X.delete(0, END)
                entradaMotor_X.insert(0, str(ult_pos_x + 1))
                mov_X(event)

            entradaMotor_Y.delete(0, END)
            entradaMotor_Y.insert(0, str(ult_pos_y + 1))
            mov_Y(event)
            
            for i in range(medida_X):
                #pcrb.construccionImg2D()
                entradaMotor_X.delete(0, END)
                entradaMotor_X.insert(0, str(ult_pos_x - 1))
                mov_X(event)

            entradaMotor_Y.delete(0, END)
            entradaMotor_Y.insert(0, str(ult_pos_y + 1))
            mov_Y(event)

# Prueba para adaptar
#for i in range(5):
    #for j in range(5):
    #    for k in range(10):
    #        x += 1
    #        print('x: ', x)
    #    y += 1
    #    print('----y----: ', y)
    #    for k in range(10):
    #        x -= 1
    #        print('x: ', x)
        
    #    y += 1
    #    print('----y----: ', y)
    
    #z += 1
    #print('z: ', z)

            
if __name__ == "__main__":
    root = tk.Tk()
    VentanaControlMicroscopio(root, "Usuario", "Prueba", "@gmail.com")
    root.mainloop()