# Librerías
import tkinter as tk
from tkinter import PhotoImage
import os
import time

# variables globales
color_ventana2 = "#b2e1fa"
color_frame = "#4d2db3"

class VentanaControlMicroscopio:
    def __init__(self, master, nombre, apellido, correo):
        self.master = master
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

        # Configuración
        self.master.title("Control microscopio")
        self.master.geometry("750x500")

        self.master.resizable(0, 0)
        self.master.config(bg = color_ventana2, cursor = "dot")


        # Etiquetas, botones y entradas

        # Etiquetas
        self.mensaje_bienvenida = tk.Label(self.master, 
                                  text = "Bienvenido, " + self.nombre + " " + self.apellido,
                                  font = "TimesNewRoman 20 italic", bg = color_ventana2)
        self.mensaje_bienvenida.place(x = 150, y = 50)

        # Etiquetas
        self.infoPosMotores = tk.Label(self.master, text = "Posición motores:", bg = color_ventana2,
                            font = "TimesnewRoman 12")
        self.infoPosMotores.place(x = 140, y = 170)


        self.infoPosMotor_X = tk.Label(self.master, text = "X", bg = color_ventana2,
                               font = "TimesnewRoman 12")
        self.infoPosMotor_X.place(x = 290, y = 150)


        self.infoPosMotor_Y = tk.Label(self.master, text = "Y", bg = color_ventana2,
                               font = "TimesnewRoman 12")
        self.infoPosMotor_Y.place(x = 350, y = 150)


        self.infoPosMotor_Z = tk.Label(self.master, text = "Z", bg = color_ventana2,
                               font = "TimesnewRoman 12")
        self.infoPosMotor_Z.place(x = 410, y = 150)


        self.infoAlmacenamiento = tk.Label(self.master, text = "Almacenamiento \n USB", bg = color_ventana2,
                                   font = "TimesNewRoman 12")
        self.infoAlmacenamiento.place(x = 140, y = 285)
    

        self.infoAlmacenamiento2 = tk.Label(self.master, text = ":", bg = color_ventana2,
                                   font = "TimesNewRoman 15")
        self.infoAlmacenamiento2.place(x = 260, y = 290)


        self.infoMedidasMuestra = tk.Label(self.master, text = "Área de medición: ", bg = color_ventana2, font = "TimesNewRoman 12")
        self.infoMedidasMuestra.place(x = 140, y = 230)


        self.infoMedida_X = tk.Label(self.master, text = "X", bg = color_ventana2,
                               font = "TimesnewRoman 12")
        self.infoMedida_X.place(x = 290, y = 210)


        self.infoMedida_Y = tk.Label(self.master, text = "Y", bg = color_ventana2,
                            font = "TimesnewRoman 12")
        self.infoMedida_Y.place(x = 350, y = 210)


        self.infoMedida_Z = tk.Label(self.master, text = "Z", bg = color_ventana2,
                               font = "TimesnewRoman 12")
        self.infoMedida_Z.place(x = 410, y = 210)


        # Entradas

        # Motores
        self.entradaMotor_X = tk.Entry(self.master, bd = 2, textvariable = motorX, width = 5)
        self.entradaMotor_X.insert(0, "0")
        self.entradaMotor_X.place(x = 280, y = 172)
        self.entradaMotor_X.bind("<Return>", mov_X)
    
        self.entradaMotor_Y = tk.Entry(self.master, textvariable = motorY, bd = 2, width = 5)
        self.entradaMotor_Y.insert(0, "0")
        self.entradaMotor_Y.place(x = 340, y = 172)
        self.entradaMotor_Y.bind("<Return>", mov_Y)
    
        self.entradaMotor_Z = tk.Entry(self.master, textvariable = motorZ, bd = 2, width = 5)
        self.entradaMotor_Z.insert(0, "0")
        self.entradaMotor_Z.place(x = 400, y = 172)
        self.entradaMotor_Z.bind("<Return>", mov_Z)


        # Medidas
        self.entradaMedida_X = tk.Entry(self.master, bd = 2, textvariable = medida_X, width = 5)
        self.entradaMedida_X.insert(0, "0")
        self.entradaMedida_X.place(x = 280, y = 232)

        self.entradaMedida_Y = tk.Entry(self.master, bd = 2, textvariable = medida_Y, width = 5)
        self.entradaMedida_Y.insert(0, "0")
        self.entradaMedida_Y.place(x = 340, y = 232)

        self.entradaMedida_Z = tk.Entry(self.master, bd = 2, textvariable = medida_Z, width = 5)
        self.entradaMedida_Z.insert(0, "0")
        self.entradaMedida_Z.place(x = 400, y = 232)


        # Botones
        self.botonSalir2 = tk.Button(self.master, text = "Salir", command = cerrarVentana, bg = "#bb9778")
        self.botonSalir2.place(x = 570, y = 410)


        self.botonPosOrigen = tk.Button(self.master, text = "Mover motores al origen", bg = "#e1e7eb",
                                command = reinicioPosiciones)
        self.botonPosOrigen.place(x = 485, y = 168)


        self.botonLaserOn = tk.Button(self.master, text = "Encender/Apagar Láser", bg = "#e1e7eb", 
                              command = controlLaser)
        self.botonLaserOn.place(x = 135, y = 410)


        self.botonCaptura = tk.Button(self.master, text = "Tomar foto", bg = "#e1e7eb", 
                              command = tomarCaptura)
        self.botonCaptura.place(x = 365, y = 410)


        self.botonIniciarMedicion = tk.Button(self.master, text = "Iniciar medición", 
                                      bg = "#AFF3B2", command = automatizacion)
        self.botonIniciarMedicion.place(x = 350, y = 360)

        # Menu desplegable para opciones de almacenamiento de imágenes
        self.menuOpciones = OptionMenu(self.master, SeleccionMemoria, *varOpciones)
        self.menuOpciones.config(width = 18)
        self.menuOpciones.place(x = 280, y = 290)


        def Advertencia(self):
            self.mensajeAdvertencia = tk.Label(self.master, text = "Ingresar un dato numérico",
                                           font = "TimesNewRoman 15 italic", 
                                           bg = color_ventana2, fg = "red")
            self.mensajeAdvertencia.place(x = 250, y = 150)

            # Situar temporizador para que desaparezca esta alerta

        #-------------------------------------------
        #     Funciones de control del arduino     -
        #-------------------------------------------
        
        # Motor en X
        def mov_X(event):
            global x, ult_pos_x, max_x, min_x
            x = entradaMotor_X.get()
        
            # Advertencia por si el valor ingresado no es entero
            try:
                x = int(x)
            except:
                Advertencia()
            else:

                # Límite mínimo
                if x < min_x:
                    x = min_x
            
                # Límite máximo
                elif x > max_x:
                    x = max_x

                # Ejecuta los pasos en el archivo .ino
                # Dirección horaria X
                while x > ult_pos_x:
                    arduino.write(b'1')
                    ult_pos_x += 1
                    time.sleep(t)

                # Dirección anti-horaria X
                while x < ult_pos_x:
                    arduino.write(b'2')
                    ult_pos_x -= 1
                    time.sleep(t)
    
        # Motor en Y
        def mov_Y(event):
            global y, ult_pos_y, max_y, min_y
            y = entradaMotor_Y.get()
        
            # Advertencia por si el valor ingresado no es entero
            try:
                y = int(y)
            except:
                Advertencia()
            else:
                # Límite mínimo
                if y < min_y:
                    y = min_y

                # Límite máximo
                elif y > max_y:
                    y = max_y
            
                pasos = ult_pos_y - y
                tiempoInicial = time.time()

                # Ejecuta los pasos en el archivo .ino
                # Dirección horaria Y
                while y > ult_pos_y:
                    arduino.write(b'3')
                    ult_pos_y += 1
                    time.sleep(t)
            
                # Dirección anti-horaria Y
                while y < ult_pos_y:
                    arduino.write(b'4')
                    ult_pos_y -= 1
                    time.sleep(t)
                
                tiempoFinal = time.time()
                tiempoEjecucion = tiempoFinal - tiempoInicial
                velocidad_y = pasos / tiempoEjecucion
            
                print(f"Datos de ejecución: \n - {pasos} pasos.\
                \n - Tiempo: {tiempoEjecucion:.2f} segundos. \n \
                - Velocidad: {velocidad_y:.2f} pasos/segundo. \n")
    
        # Motor en Z
        def mov_Z(event):
            global z, ult_pos_z, max_z, min_z
            z = entradaMotor_Z.get()

            # Advertencia por si el valor ingresado no es entero
            try:
                z = int(z)
            except:
                Advertencia()
            else:
                # Límite mínimo
                if z < min_z:
                    z = min_z

                # Límite máximo
                elif z > max_z:
                    z = max_z

                # Ejecuta los pasos en el archivo .ino
                # Dirección horaria Z
                while z > ult_pos_z:
                    arduino.write(b'5')
                    ult_pos_z += 1
                    time.sleep(t)

                # Dirección anti-horaria Z
                while z < ult_pos_z:
                    arduino.write(b'6')
                    ult_pos_z -= 1
                    time.sleep(t)
    
        # Regreso al origen de los motores
        def reinicioPosiciones():
            event = None

            entradaMotor_X.delete(0, END)
            entradaMotor_X.insert(0, "0")

            entradaMotor_Y.delete(0, END)
            entradaMotor_Y.insert(0, "0")

            entradaMotor_Z.delete(0, END)
            entradaMotor_Z.insert(0, "0")

            # Ejecuta la posición de origen en cada motor
            mov_X(event)
            mov_Y(event)
            mov_Z(event)


        # Control del láser
        def controlLaser():
            global laser

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
            

if __name__ == "__main__":
    root = tk.Tk()
    VentanaControlMicroscopio(root, "Usuario", "Prueba", "@gmail.com")
    root.mainloop()