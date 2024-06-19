# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:17:52 2023

@author: Sebastián Marín Ruiz
"""
# Librerías
import ControlArduino.automatizacion as Arpy
import Interfaz.VentanaBienvenida as guipy
#import ProcesamientoImg.CamaraRB as pcrb
import ProcesamientoImg.capturaCamara as PiCam
import serial
import time
import tkinter as tk
import os

# Control láser
laser = False

def main():
    root = tk.Tk()
    guipy.VentanaBienvenida(root)
    root.mainloop()

#-------------------------
#-   Ventana principal   -
#-------------------------

def ingresar():
    motorX = StringVar()
    motorY = StringVar()
    motorZ = StringVar()
    medida_X = StringVar()
    medida_Y = StringVar()
    medida_Z = StringVar()
    varOpciones = ["Seleccione memoria", "Memoria 1", "Memoria 2"]
    SeleccionMemoria = StringVar()
    SeleccionMemoria.set(varOpciones[0])


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


    

    # Lectura de últimas coordenadas en el archivo .txt
    ultimasCoordenadas = leerCoordenadas()
    if ultimasCoordenadas:
        global x, y, z, ult_pos_x, ult_pos_y, ult_pos_z
        ult_pos_x, ult_pos_y, ult_pos_z = ultimasCoordenadas[0], ultimasCoordenadas[1], ultimasCoordenadas[2]
        x, y, z = ult_pos_x, ult_pos_y, ult_pos_z
        visualizacionUltPos()


if __name__=="__main__":
    main()