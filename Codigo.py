# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:17:52 2023

@author: Sebastián Marín Ruiz
"""
# Librerías
import serial
import time
from tkinter import *
import os

# Configuración arduino
arduino =  serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 1)
time.sleep(2)

# Variables globales
root = Tk()
color_base = "#2d0b68"
color_letra = "#a5f1f7"
color_entrada = "#8a6ac2"
color_frame = "#4d2db3"
color_ventana2 = "#b2e1fa"

#---------------------------------------#
#--  Configuración ventana principal  --#
#---------------------------------------#
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

    #### Funciones de los motores
    # Motor en X
    def mov_X(event):
        x = entradaMotor_X.get()
        
        # Advertencia por si el valor ingresado no es entero
        try:
            x = int(x)
        except:
            mensajeAdvertencia = Label(interfazPrincipal, text = "Ingresar un dato numérico",
                                       font = "TimesNewRoman 20 italic", 
                                       bg = color_ventana2)
            mensajeAdvertencia.place(x = 150, y = 50)
        else:
            # Ejecuta los pasos en el archivo .ino
            # x = int(x)
            for i in range(0, x):
                arduino.write(b'1')
                time.sleep(0.1)
    
    # Motor en Y
    def mov_Y(event):
        y = entradaMotor_Y.get()
        
        # Advertencia por si el valor ingresado no es entero
        try:
            y = int(y)
        except:
            mensajeAdvertencia = Label(interfazPrincipal, text = "Ingresar un dato numérico",
                                       font = "TimesNewRoman 20 italic", 
                                       bg = color_ventana2)
            mensajeAdvertencia.place(x = 150, y = 50)
        else:
            # Ejecuta los pasos en el archivo .ino
            for i in range(0, y):
                arduino.write(b'2')
                time.sleep(0.1)
    
    # Motor en Z
    def mov_Z(event):
        z = entradaMotor_Z.get()
        
        # Advertencia por si el valor ingresado no es entero
        try:
            z = int(z)
        except:
            mensajeAdvertencia = Label(interfazPrincipal, text = "Ingresar un dato numérico",
                                       font = "TimesNewRoman 20 italic", 
                                       bg = color_ventana2)
            mensajeAdvertencia.place(x = 150, y = 50)
        else:
            # Ejecuta los pasos en el archivo .ino
            for i in range(0, z):
                arduino.write(b'3')
                time.sleep(0.1)
    
    def reinicioPosiciones():
        entradaMotor_X.delete(0, END)
        entradaMotor_X.insert(0, "0")

        entradaMotor_Y.delete(0, END)
        entradaMotor_Y.insert(0, "0")

        entradaMotor_Z.delete(0, END)
        entradaMotor_Z.insert(0, "0")


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
    

    # Botones
    botonSalir2 = Button(interfazPrincipal, text = "Salir", 
                    command = root.destroy, bg = "red")
    botonSalir2.place(x = 335, y = 400)


    botonPosOrigen = Button(interfazPrincipal, text = "Mover motores al origen", bg = "#e1e7eb",
                            command = reinicioPosiciones)
    botonPosOrigen.place(x = 270, y = 240)

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
#               Etiquetas y entradas                 |
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
infoNombre.place(x = 220, y = 200)

entradaNombre = Entry(root, bd = 1, bg = color_entrada, width = 30, textvariable = nombre)
entradaNombre.insert(0, "Investigador")
entradaNombre.bind("<Button-1>", borrar_texto(entradaNombre))
entradaNombre.place(x = 315, y = 202)


# Apellido
infoApellido = Label(root, text = "Apellido(s):", bg = color_base,
                  font = "TimesNewRoman 13", fg = color_letra)
infoApellido.place(x = 220, y = 240)

entradaApellido = Entry(root, bd = 1, bg = color_entrada, width = 30, textvariable = apellido)
entradaApellido.insert(0, "Anónimo")
entradaApellido.bind("<Button-1>", borrar_texto(entradaApellido))
entradaApellido.place(x = 315, y = 242)


# Correo
infoCorreo = Label(root, text = "Correo:", bg = color_base,
                   font = "TimesNewRoman 13", fg = color_letra)
infoCorreo.place(x = 220, y = 280)

entradaCorreo = Entry(root, bd = 1, bg = color_entrada, width = 30, textvariable = correo)
entradaCorreo.insert(0, "Escriba aquí su correo")
entradaCorreo.bind("<Button-1>", borrar_texto(entradaCorreo))
entradaCorreo.place(x = 315, y = 282)

# Botones
botonSalir = Button(root, text = "Salir", 
                    command = root.destroy, bg = "red")
botonSalir.place(x = 600, y = 400)


botonUsuarioFrecuente = Button(root, text = "Usuario frecuente", 
                               bg = "#3a85f7", state = "normal",
                               command = usuarioFrecuente)
botonUsuarioFrecuente.place(x = 100, y = 400)


botonIngresar = Button(root, text = "Ingresar", bg = "#48c128",
                       command = ingresar)
botonIngresar.place(x = 390, y = 330)


botonAtras = Button(root, text = "Atrás", command = usuarioFrecuente, bg = "#3a85f7")


infoNoUF = Label(root, text = "Actualmente no hay ningún\n usuario frecuente", bd = 14, bg = color_base, 
                 fg = color_letra, font = "TimesNewRoman 23")

root.mainloop()