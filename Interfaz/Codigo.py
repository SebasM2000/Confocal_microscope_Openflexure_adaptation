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
root.iconbitmap("D:/SEBASTIAN/UNIVERSIDAD/TRABAJO_GRADO_REPO/Interfaz/TM.ico")

# Limitando las dimensiones de ventana
root.resizable(0, 0)

# Configuraciones color y forma del cursor
root.config(bg = "#898f8e", cursor = "dot")

# Etiquetas
etiqueta = Label(root, text = "Etiqueta")
etiqueta.grid(row = 0, column = 0)

# Botones
boton1 = Button(root, text = "Cerrar", command = root.destroy, bg = "red")
boton1.grid(row = 2, column = 1)

def imprimir():
    label1 = Label(root, text = "Imprimiendo algo xd")
    label1.pack()

boton2 = Button(root, text = "Imprimir", command = imprimir, bg = "blue")
boton2.place(x = 30, y = 40)



root.mainloop()