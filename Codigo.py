# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:17:52 2023

@author: Sebastián Marín Ruiz
"""
# Librerías
#import ProcesamientoImg.CamaraRB as Pros
import serial
import time
from tkinter import *
import os

# Configuración arduino
arduino =  serial.Serial("COM3", baudrate = 9600, timeout = 1)
time.sleep(2)

# Variables globales
root = Tk()
ult_pos_x = 0
ult_pos_y = 0
ult_pos_z = 0
x = None
y = None
z = None
max_x = 1000000
max_y = max_x
max_z = 10
min_x = -max_x
min_y = -max_y
min_z = 0
laser = False
color_base = "#72cae2"
color_letra = "#000000"
color_entrada = "#ffffff"
color_frame = "#4d2db3"
color_ventana2 = "#b2e1fa"

#---------------------------------------
#-   Configuración ventana principal   -
#---------------------------------------
def config_principal():
    # Título de ventana
    root.title("Reconocimiento de usuario") 

    # Dimensiones de ventana
    root.geometry("750x500")

    # Poniendo ícono de la ventana
    ruta_abs_img = os.path.dirname(os.path.abspath(__file__))
    img_ico = os.path.join(ruta_abs_img, "Interfaz/taylorm.png")
    img = PhotoImage(file = img_ico)
    root.iconphoto(True, img)

    # Limitando las dimensiones de ventana
    root.resizable(0, 0)

    # Configuraciones color y forma del cursor
    root.config(bg = color_base, cursor = "dot")

# Ejecución del código principal
config_principal()


nombre = StringVar()
apellido = StringVar()
correo = StringVar()

visibilidadBoton = BooleanVar()
visibilidadBoton.set(True)

# Segunda ventana
def ingresar():
    motorX = StringVar()
    motorY = StringVar()
    motorZ = StringVar()
    varOpciones = ["Seleccione memoria", "Memoria 1", "Memoria 2"]
    SeleccionMemoria = StringVar()
    SeleccionMemoria.set(varOpciones[0])

    # Configuración segunda ventana
    interfazPrincipal = Toplevel()
    interfazPrincipal.title("Configuración microscopio")
    interfazPrincipal.geometry("750x500")
    interfazPrincipal.resizable(0, 0)
    interfazPrincipal.config(bg = color_ventana2, cursor = "dot")
    root.withdraw()

    # Etiquetas, botones y entradas
    # Etiquetas
    mensajeBienvenida = Label(interfazPrincipal, 
                              text = "Bienvenido, " + entradaNombre.get() + " " + entradaApellido.get(),
                              font = "TimesNewRoman 20 italic", bg = color_ventana2)
    mensajeBienvenida.place(x = 150, y = 50)

    def Advertencia():
        mensajeAdvertencia = Label(interfazPrincipal, text = "Ingresar un dato numérico",
                                       font = "TimesNewRoman 15 italic", 
                                       bg = color_ventana2, fg = "red")
        mensajeAdvertencia.place(x = 250, y = 150)

    #---------------------------------------------
    #-  Funciones de almacenamiento de posición  -
    #---------------------------------------------
    # Guardar coordenadas en archivo .txt
    def guardarCoordenadas(x, y, z):
        with open("coordenadas.txt", "w") as file:
            file.write(f"{x},{y},{z}")

    # Leer coordenadas del archivo .txt
    def leerCoordenadas():
        try:
            with open("coordenadas.txt", "r") as file:
                line = file.readline()

                if line:
                    return tuple(map(int, line.split(',')))
        except FileNotFoundError:
            return None
        
    # Función que se ejecuta al cerrar la ventana
    def cerrarVentana():

        # Guardar las coordenadas antes de cerrar
        guardarCoordenadas(entradaMotor_X.get(), entradaMotor_Y.get(), entradaMotor_Z.get())
        root.destroy()

    # Sustitución últimas posiciones en las entradas X, Y, Z
    def visualizacionUltPos():
        event = None
        
        entradaMotor_X.delete(0, END)
        entradaMotor_X.insert(0, str(ult_pos_x))

        entradaMotor_Y.delete(0, END)
        entradaMotor_Y.insert(0, str(ult_pos_y))

        entradaMotor_Z.delete(0, END)
        entradaMotor_Z.insert(0, str(ult_pos_z))

        # Ejecuta posiciones
        mov_X(event)
        mov_Y(event)
        mov_Z(event)


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

            # Dirección anti-horaria X
            while x < ult_pos_x:
                arduino.write(b'2')
                ult_pos_x -= 1
    
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

            # Ejecuta los pasos en el archivo .ino
            # Dirección horaria Y
            while y > ult_pos_y:
                arduino.write(b'3')
                ult_pos_y += 1
            
            # Dirección anti-horaria Y
            while y < ult_pos_y:
                arduino.write(b'4')
                ult_pos_y -= 1
    
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

            # Dirección anti-horaria Z
            while z < ult_pos_z:
                arduino.write(b'6')
                ult_pos_z -= 1
    
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
#     def tomarCaptura():
#         ruta = os.path.dirname(__file__)
#         Pros.tomarFoto(ruta)

    # Medición automática de los motores
    def automatizacion():
        event = None
        global ult_pos_z, ult_pos_y, ult_pos_x, max_x, max_y, max_z
        for k in range(ult_pos_z, max_z):
            entradaMotor_Z()
            #tomarCaptura()
            for j in range(ult_pos_y, max_y):
                entradaMotor_Y()
                #tomarCaptura()
                for i in range(ult_pos_x, max_x):
                    entradaMotor_X.delete(0, END)
                    entradaMotor_X.insert()
                    #tomarCaptura()


    # Etiquetas motores
    infoPosMotores = Label(interfazPrincipal, text = "Posición motores:", bg = color_ventana2,
                           font = "TimesnewRoman 12")
    infoPosMotores.place(x = 140, y = 200)


    infoPosMotor_X = Label(interfazPrincipal, text = "X", bg = color_ventana2,
                           font = "TimesnewRoman 12")
    infoPosMotor_X.place(x = 285, y = 180)


    infoPosMotor_Y = Label(interfazPrincipal, text = "Y", bg = color_ventana2,
                           font = "TimesnewRoman 12")
    infoPosMotor_Y.place(x = 355, y = 180)


    infoPosMotor_Z = Label(interfazPrincipal, text = "Z", bg = color_ventana2,
                           font = "TimesnewRoman 12")
    infoPosMotor_Z.place(x = 425, y = 180)
    

    # Entradas motores
    entradaMotor_X = Entry(interfazPrincipal, bd = 2, textvariable = motorX, width = 5)
    entradaMotor_X.insert(0, "0")
    entradaMotor_X.place(x = 270, y = 200)
    entradaMotor_X.bind("<Return>", mov_X)
    

    entradaMotor_Y = Entry(interfazPrincipal, textvariable = motorY, bd = 2, width = 5)
    entradaMotor_Y.insert(0, "0")
    entradaMotor_Y.place(x = 340, y = 200)
    entradaMotor_Y.bind("<Return>", mov_Y)
    

    entradaMotor_Z = Entry(interfazPrincipal, textvariable = motorZ, bd = 2, width = 5)
    entradaMotor_Z.insert(0, "0")
    entradaMotor_Z.place(x = 410, y = 200)
    entradaMotor_Z.bind("<Return>", mov_Z)

    # Lectura de últimas coordenadas en el archivo .txt
    ultimasCoordenadas = leerCoordenadas()
    if ultimasCoordenadas:
        global x, y, z, ult_pos_x, ult_pos_y, ult_pos_z
        ult_pos_x, ult_pos_y, ult_pos_z = ultimasCoordenadas[0], ultimasCoordenadas[1], ultimasCoordenadas[2]
        x, y, z = ult_pos_x, ult_pos_y, ult_pos_z
        visualizacionUltPos()

    # Botones
    botonSalir2 = Button(interfazPrincipal, text = "Salir", 
                    command = cerrarVentana, bg = "#bb9778")
    botonSalir2.place(x = 335, y = 400)


    botonPosOrigen = Button(interfazPrincipal, text = "Mover motores al origen", bg = "#e1e7eb",
                            command = reinicioPosiciones)
    botonPosOrigen.place(x = 270, y = 240)


    botonLaserOn = Button(interfazPrincipal, text = "Encender/Apagar Láser", bg = "#e1e7eb", 
                          command = controlLaser)
    botonLaserOn.place(x = 100, y = 400)


#     botonCaptura = Button(interfazPrincipal, text = "Tomar foto", bg = "#e1e7eb", 
#                           command = lambda: tomarCaptura())
#     botonCaptura.place(x = 200, y = 400)

    botonIniciarMedicion = Button(interfazPrincipal, text = "Iniciar medición", 
                                  bg = "#e1e7eb", command = automatizacion)

    # Menu desplegable para opciones de almacenamiento de imágenes
    infoAlmacenamiento = Label(interfazPrincipal, text = "Almacenamiento \n USB", bg = color_ventana2,
                               font = "TimesNewRoman 12")
    infoAlmacenamiento.place(x = 140, y = 295)
    

    infoAlmacenamiento2 = Label(interfazPrincipal, text = ":", bg = color_ventana2,
                               font = "TimesNewRoman 15")
    infoAlmacenamiento2.place(x = 252, y = 300)


    menuOpciones = OptionMenu(interfazPrincipal, SeleccionMemoria, *varOpciones)
    menuOpciones.config(width = 18)
    menuOpciones.place(x = 270, y = 300)

    


# Función que elimina el texto de las entradas nombre y apellido
def borrar_texto(entrada):
    return lambda evento: entrada.delete(0, END)


# Función que traslada a una nueva pantalla al hacer click en "Usuario frecuente"
def usuarioFrecuente():
    if visibilidadBoton.get():
        botonUsuarioFrecuente.place_forget()
        botonIngresar.place_forget()
        botonSalir.place_forget()
        tituloBienvenida.place_forget()
        entradaNombre.place_forget()
        entradaApellido.place_forget()
        entradaCorreo.place_forget()
        infoNombre.place_forget()
        infoApellido.place_forget()
        infoCorreo.place_forget()
        botonAtras.place(x = 140, y = 400)
        infoNoUF.place(x = 190, y = 180)
        visibilidadBoton.set(False)
    else:
        tituloBienvenida.place(x = 100, y = 50)
        botonUsuarioFrecuente.place(x = 100, y = 400)
        botonIngresar.place(x = 350, y = 330)
        botonSalir.place(x = 600, y = 400)
        entradaNombre.place(x = 315, y = 202)
        entradaApellido.place(x = 315, y = 242)
        entradaCorreo.place(x = 315, y = 282)
        infoNombre.place(x = 220, y = 200)
        infoApellido.place(x = 220, y = 240)
        infoCorreo.place(x = 220, y = 280)
        botonAtras.place_forget()
        infoNoUF.place_forget()
        visibilidadBoton.set(True)

#-----------------------------------------------------
#               Etiquetas y entradas                 -
#-----------------------------------------------------
# Titulo
tituloBienvenida = Label(root, text = "¡Bienvenido al laboratorio de Acusto-óptica\n y Radiometría!", 
                 bd = 14, bg = color_base, 
                 fg = color_letra, font = "TimesNewRoman 23 italic")
tituloBienvenida.place(x = 100, y = 50)


# Nombres, apellidos y correo

# Nombre
infoNombre = Label(root, text = "Nombre(s): ", bg = color_base,
                  font = "TimesNewRoman 13", fg = color_letra)
infoNombre.place(x = 180, y = 200)

entradaNombre = Entry(root, bd = 1, bg = color_entrada, width = 30, textvariable = nombre)
entradaNombre.insert(0, "Investigador")
entradaNombre.bind("<Button-1>", borrar_texto(entradaNombre))
entradaNombre.place(x = 275, y = 202)


# Apellido
infoApellido = Label(root, text = "Apellido(s):", bg = color_base,
                  font = "TimesNewRoman 13", fg = color_letra)
infoApellido.place(x = 180, y = 240)

entradaApellido = Entry(root, bd = 1, bg = color_entrada, width = 30, textvariable = apellido)
entradaApellido.insert(0, "Anónimo")
entradaApellido.bind("<Button-1>", borrar_texto(entradaApellido))
entradaApellido.place(x = 275, y = 242)


# Correo
infoCorreo = Label(root, text = "Correo:", bg = color_base,
                   font = "TimesNewRoman 13", fg = color_letra)
infoCorreo.place(x = 180, y = 280)

entradaCorreo = Entry(root, bd = 1, bg = color_entrada, width = 30, textvariable = correo)
entradaCorreo.insert(0, "Escriba aquí su correo")
entradaCorreo.bind("<Button-1>", borrar_texto(entradaCorreo))
entradaCorreo.place(x = 275, y = 282)

# Botones
botonSalir = Button(root, text = "Salir", 
                    command = root.destroy, bg = "#bb9778")
botonSalir.place(x = 610, y = 420)


botonUsuarioFrecuente = Button(root, text = "Usuario frecuente", 
                               bg = "#c4c4c4", state = "normal",
                               command = usuarioFrecuente)
botonUsuarioFrecuente.place(x = 325, y = 375)


botonIngresar = Button(root, text = "Ingresar", bg = "#c4c4c4",
                       command = ingresar)
botonIngresar.place(x = 355, y = 330)


botonAtras = Button(root, text = "Atrás", command = usuarioFrecuente, bg = "#3a85f7")


infoNoUF = Label(root, text = "Actualmente no hay ningún\n usuario frecuente", bd = 14, bg = color_base, 
                 fg = color_letra, font = "TimesNewRoman 23")

root.mainloop()