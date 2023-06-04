# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:17:52 2023

@author: s
"""

from tkinter import *

root = Tk()

# Título de ventana
root.title("Mi primera ventana") 

# Dimensiones de ventana
root.geometry("900x500")

# Poniendo ícono de la ventana
root.iconbitmap("D:/SEBASTIAN/UNIVERSIDAD/TRABAJO_GRADO_FINAL/Interfaz/TM.ico")

# Limitando las dimensiones de ventana
root.resizable(0, 0)

# Configuraciones color y forma del cursor
root.config(bg = "#898f8e", cursor = "dot")

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

def saludar():
    saludo.set("Hola " + nombre.get() + " " + apellido.get())

nombre.set("Escribe aquí tu nombre")
apellido.set("Escribe aquí tu apellido")

# Etiquetas
etiqueta = Label(root, text = "Etiqueta", bd = 14, bg = "green", font = "Curier 10")
etiqueta.grid(row = 0, column = 0)

etiqueta2 = Label(root, text = "Escribe aquí tu nombre")
etiqueta2.place(x = 100, y = 2)
entrada1 = Entry(root, textvariable = nombre, bd = 5)
entrada1.place(x = 100, y = 20)

etiqueta3 = Label(root, text = "Escribe aquí tu apellido")
etiqueta3.place(x = 200, y = 2)
entrada2 = Entry(root, textvariable = apellido, bd = 5)
entrada2.place(x = 200, y = 20)

entrada3 = Entry(root, textvariable = saludo, state = "disable")
entrada3.place(x = 200, y = 200)

# Botones
boton1 = Button(root, text = "Cerrar", command = root.destroy, bg = "red")
boton1.grid(row = 2, column = 1)


boton2 = Button(root, text = "Saludar", command = saludar, bg = "blue")
boton2.place(x = 150, y = 100)



root.mainloop()