# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:17:52 2023

@author: s
"""

from tkinter import *
import os

# Variables globales
root = Tk()
color_base = "#2d0b68"
color_letra = "#a5f1f7"
color_entrada = "#8a6ac2"
color_frame = "#4d2db3"

def config_principal():
    # Título de ventana
    root.title("Reconocimiento de usuario") 

    # Dimensiones de ventana
    root.geometry("750x500")

    # Poniendo ícono de la ventana
    ruta_abs_img = os.path.dirname(os.path.abspath(__file__))
    img_ico = os.path.join(ruta_abs_img, "taylorm.png")
    img = PhotoImage(file = img_ico)
    root.iconphoto(True, img)

    # Limitando las dimensiones de ventana
    root.resizable(0, 0)

    # Configuraciones color y forma del cursor
    root.config(bg = color_base, cursor = "dot")


config_principal()

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

def ingresar():
    # Cpnfiguración segunda ventana
    interfazPrincipal = Toplevel()
    interfazPrincipal.title("Configuración microscopio")
    interfazPrincipal.geometry("750x500")


def borrar_texto(entrada):
    return lambda evento: entrada.delete(0, END)

nombre.set("Escribe aquí tu nombre")
apellido.set("Escribe aquí tu apellido")

#-----------------------------------------------------
#               Etiquetas y entradas                 |
#-----------------------------------------------------
tituloBienvenida = Label(root, text = "¡Bienvenido al laboratorio de Acusto-óptica\n y Radiometría!", 
                 bd = 14, bg = color_base, 
                 fg = color_letra, font = "TimesNewRoman 23 italic").place(x = 100, y = 50)

# Nombres, apellidos y correo
infoNombre = Label(root, text = "Nombre(s): ", bg = color_base,
                  font = "TimesNewRoman 13", fg = color_letra).place(x = 220, y = 200)

entradaNombre = Entry(root, bd = 1, bg = color_entrada)
entradaNombre.insert(0, "Escriba aquí su nombre")
entradaNombre.bind("<Button-1>", borrar_texto(entradaNombre))
entradaNombre.place(x = 315, y = 202)

infoApellido = Label(root, text = "Apellido(s):", bg = color_base,
                  font = "TimesNewRoman 13", fg = color_letra).place(x = 220, y = 240)

entradaApellido = Entry(root, bd = 1, bg = color_entrada)
entradaApellido.insert(0, "Escriba aquí su apellido")
entradaApellido.bind("<Button-1>", borrar_texto(entradaApellido))
entradaApellido.place(x = 315, y = 242)

infoCorreo = Label(root, text = "Correo:", bg = color_base,
                   font = "TimesNewRoman 13", fg = color_letra).place(x = 220, y = 280)

entradaCorreo = Entry(root, bd = 1, bg = color_entrada)
entradaCorreo.insert(0, "Escriba aquí su correo")
entradaCorreo.bind("<Button-1>", borrar_texto(entradaCorreo))
entradaCorreo.place(x = 315, y = 282)

# Botones
botonSalir = Button(root, text = "Salir", 
                    command = root.destroy, bg = "red").place(x = 600, y = 400)

botonUsuarioFrecuente = Button(root, text = "Usuario frecuente", 
                               bg = "#3a85f7").place(x = 100, y = 400)

botonIngresar = Button(root, text = "Ingresar", bg = "#48c128",
                       command = ingresar).place(x = 350, y = 330)

root.mainloop()