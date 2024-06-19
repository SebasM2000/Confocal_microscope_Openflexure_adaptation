# Librerías
import tkinter as tk
from tkinter import PhotoImage
import os
from VentanaPrincipal import VentanaControlMicroscopio


# Colores
color_base = "#72cae2"
color_letra = "#000000"
color_entrada = "#ffffff"


class VentanaBienvenida:

    def __init__(self, master):
        self.master = master

        self.visibilidadBoton = tk.BooleanVar()
        self.visibilidadBoton.set(True)

        # Configuración ventana de bienvenida
        self.master.title("Reconocimiento de usuario")
        self.master.geometry("750x500")

        # ícono ventana
        self.ruta_abs_img = os.path.dirname(__file__)
        self.imagen_icono = os.path.join(self.ruta_abs_img, "icono", "taylorm.png")
        self.imagen = PhotoImage(file = self.imagen_icono)
        self.master.iconphoto(True, self.imagen)
        self.master.resizable(0, 0)
        self.master.config(bg = color_base, cursor = "dot")

        #-----------------------------------------------------#
        #               Etiquetas y entradas                  #
        #-----------------------------------------------------#

        # Titulo
        self.mensaje_bienvenida = tk.Label(self.master, text = "¡Bienvenido al laboratorio de Acusto-óptica\n y Radiometría!", 
                        bd = 14, bg = color_base, 
                        fg = color_letra, font = "TimesNewRoman 23 italic")
        self.mensaje_bienvenida.place(x = 100, y = 50)

        # Nombres, apellidos y correo

        # Nombre
        self.info_nombre = tk.Label(self.master, text = "Nombre(s): ", bg = color_base,
                          font = "TimesNewRoman 13", fg = color_letra)
        self.info_nombre.place(x = 180, y = 200)

        self.entrada_nombre = tk.Entry(self.master, bd = 1, bg = color_entrada, width = 30, textvariable = self.registroUsuario)
        self.entrada_nombre.insert(0, "Investigador")
        self.entrada_nombre.place(x = 275, y = 202)


        # Apellido
        self.info_apellido = tk.Label(self.master, text = "Apellido(s):", bg = color_base,
                          font = "TimesNewRoman 13", fg = color_letra)
        self.info_apellido.place(x = 180, y = 240)

        self.entrada_apellido = tk.Entry(self.master, bd = 1, bg = color_entrada, width = 30, textvariable = self.registroUsuario)
        self.entrada_apellido.insert(0, "Anónimo")
        self.entrada_apellido.place(x = 275, y = 242)


        # Correo
        self.info_correo = tk.Label(self.master, text = "Correo:", bg = color_base,
                           font = "TimesNewRoman 13", fg = color_letra)
        self.info_correo.place(x = 180, y = 280)

        self.entrada_correo = tk.Entry(self.master, bd = 1, bg = color_entrada, width = 30, textvariable = self.registroUsuario)
        self.entrada_correo.insert(0, "Escriba aquí su correo")
        self.entrada_correo.place(x = 275, y = 282)

        # Función que elimina texto de las entradas de información del usuario
        self.borrarTextoEntradas()


        # Botones
        self.boton_salir = tk.Button(self.master, text = "Salir", 
                            command = self.master.destroy, bg = "#bb9778")
        self.boton_salir.place(x = 610, y = 420)


        self.boton_usuario_frecuente = tk.Button(self.master, text = "Usuario frecuente", 
                                       bg = "#c4c4c4", state = "normal",
                                       command = self.usuarioFrecuente)
        self.boton_usuario_frecuente.place(x = 325, y = 375)


        self.boton_ingresar = tk.Button(self.master, text = "Ingresar", bg = "#c4c4c4",
                            command = self.registroUsuario)
        self.boton_ingresar.place(x = 355, y = 330)


        self.boton_atras = tk.Button(self.master, text = "Atrás", command = self.usuarioFrecuente, bg = "#3a85f7")


        self.info_no_usuario_frecuente = tk.Label(self.master, text = "Actualmente no hay ningún\n usuario frecuente", bd = 14, bg = color_base, 
                         fg = color_letra, font = "TimesNewRoman 23")
        
    # Función que elimina el texto de las entradas nombre y apellido
    def borrarTextoEntradas(self):

        # Definición de funciones lambda para eliminar texto
        self.borrar_texto_nombre = lambda evento: self.entrada_nombre.delete(0, tk.END)
        self.borrar_texto_apellido = lambda evento: self.entrada_apellido.delete(0, tk.END)
        self.borrar_texto_correo = lambda evento: self.entrada_correo.delete(0, tk.END)

        # Asociación de evento con las entradas correspondientes
        self.entrada_nombre.bind("<Button-1>", self.borrar_texto_nombre)
        self.entrada_nombre.bind("<Button-1>", self.borrar_texto_apellido)
        self.entrada_nombre.bind("<Button-1>", self.borrar_texto_correo)

    # Función que traslada a una nueva pantalla al hacer click en "Usuario frecuente"
    def usuarioFrecuente(self):
        if self.visibilidadBoton.get():
            self.boton_usuario_frecuente.place_forget()
            self.boton_ingresar.place_forget()
            self.boton_salir.place_forget()
            self.mensaje_bienvenida.place_forget()
            self.entrada_nombre.place_forget()
            self.entrada_apellido.place_forget()
            self.entrada_correo.place_forget()
            self.info_nombre.place_forget()
            self.info_apellido.place_forget()
            self.info_correo.place_forget()
            self.boton_atras.place(x = 140, y = 400)
            self.info_no_usuario_frecuente.place(x = 190, y = 180)
            self.visibilidadBoton.set(False)
        else:
            self.mensaje_bienvenida.place(x = 100, y = 50)
            self.boton_usuario_frecuente.place(x = 100, y = 400)
            self.boton_ingresar.place(x = 350, y = 330)
            self.boton_salir.place(x = 600, y = 400)
            self.entrada_nombre.place(x = 315, y = 202)
            self.entrada_apellido.place(x = 315, y = 242)
            self.entrada_correo.place(x = 315, y = 282)
            self.info_nombre.place(x = 220, y = 200)
            self.info_apellido.place(x = 220, y = 240)
            self.info_correo.place(x = 220, y = 280)
            self.boton_atras.place_forget()
            self.info_no_usuario_frecuente.place_forget()
            self.visibilidadBoton.set(True)

    # Función de registro de usuario
    def registroUsuario(self):
        self.nombre = self.entrada_nombre.get().strip()
        self.apellido = self.entrada_apellido.get().strip()
        self.correo = self.entrada_correo.get().strip()
        
        self.master.destroy()

        self.ventana_principal = tk.Tk()
        VentanaControlMicroscopio(self.ventana_principal, self.nombre, self.apellido, self.correo)
        self.ventana_principal.mainloop()

        

if __name__ == "__main__":
    root = tk.Tk()
    ventana_bienvenida = VentanaBienvenida(root)
    root.mainloop()