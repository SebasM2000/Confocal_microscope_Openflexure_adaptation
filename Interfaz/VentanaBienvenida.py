 # Librerías
import tkinter as tk
from tkinter import PhotoImage
import os
from VentanaPrincipal import VentanaControlMicroscopio

# Colores
color_base = "#72cae2"
color_letra = "#000000"
color_entrada = "#ffffff"


class VentanaRegistro(tk.Tk):

    def __init__(self, abrir_ventana_principal):
        super().__init__()
        self.abrir_ventana_principal = abrir_ventana_principal

        self.visibilidadBoton = tk.BooleanVar()
        self.visibilidadBoton.set(True)


        # Configuración ventana de bienvenida
        self.title("Reconocimiento de usuario")
        self.geometry("750x500")

        # ícono ventana
        self.ruta_abs_img = os.path.dirname(__file__)
        self.imagen_icono = os.path.join(self.ruta_abs_img, "icono", "logo.png")
        self.imagen = PhotoImage(file = self.imagen_icono)
        self.iconphoto(True, self.imagen)
        self.resizable(0, 0)
        self.config(bg = color_base, cursor = "dot")

        #-----------------------------------------------------#
        #               Etiquetas y entradas                  #
        #-----------------------------------------------------#

        # Titulo
        self.mensaje_bienvenida = tk.Label(self, text = "¡Bienvenido al laboratorio de Acusto-óptica\n y Radiometría!", 
                        bd = 14, bg = color_base, 
                        fg = color_letra, font = "TimesNewRoman 23 italic")
        self.mensaje_bienvenida.place(x = 100, y = 50)

        # Nombres, apellidos y correo

        # Nombre
        self.info_nombre = tk.Label(self, text = "Nombre(s): ", bg = color_base,
                          font = "TimesNewRoman 13", fg = color_letra)
        self.info_nombre.place(x = 180, y = 200)

        self.entrada_nombre = tk.Entry(self, bd = 1, bg = color_entrada, width = 30)
        self.entrada_nombre.insert(0, "Investigador")
        self.entrada_nombre.place(x = 275, y = 202)


        # Apellido
        self.info_apellido = tk.Label(self, text = "Apellido(s):", bg = color_base,
                          font = "TimesNewRoman 13", fg = color_letra)
        self.info_apellido.place(x = 180, y = 240)

        self.entrada_apellido = tk.Entry(self, bd = 1, bg = color_entrada, width = 30)
        self.entrada_apellido.insert(0, "Anónimo")
        self.entrada_apellido.place(x = 275, y = 242)


        # Correo
        self.info_correo = tk.Label(self, text = "Correo:", bg = color_base,
                           font = "TimesNewRoman 13", fg = color_letra)
        self.info_correo.place(x = 180, y = 280)

        self.entrada_correo = tk.Entry(self, bd = 1, bg = color_entrada, width = 30)
        self.entrada_correo.insert(0, "Escriba aquí su correo")
        self.entrada_correo.place(x = 275, y = 282)

        # Función que elimina texto de las entradas de información del usuario
        self.borrarTextoEntradas()


        # Botones
        self.boton_salir = tk.Button(self, text = "Salir", 
                            command = self.destroy, bg = "#bb9778")
        self.boton_salir.place(x = 610, y = 420)


        self.boton_usuario_frecuente = tk.Button(self, text = "Usuario frecuente", 
                                       bg = "#c4c4c4", state = "normal",
                                       command = self.usuarioFrecuente)
        self.boton_usuario_frecuente.place(x = 325, y = 375)


        self.boton_ingresar = tk.Button(self, text = "Ingresar", bg = "#c4c4c4",
                            command = self.confirmacionDatos)
        self.boton_ingresar.place(x = 355, y = 330)


        self.boton_atras = tk.Button(self, text = "Atrás", command = self.usuarioFrecuente, bg = "#3a85f7")


        self.info_no_usuario_frecuente = tk.Label(self, text = "Actualmente no hay ningún\n usuario frecuente", bd = 14, bg = color_base, fg = color_letra, font = "TimesNewRoman 23")
        
        
    # Función que elimina el texto de las entradas nombre y apellido
    def borrarTextoEntradas(self):

        # Definición de funciones lambda para eliminar texto
        self.borrar_texto_nombre = lambda event: self.entrada_nombre.delete(0, tk.END)
        self.borrar_texto_apellido = lambda event: self.entrada_apellido.delete(0, tk.END)
        self.borrar_texto_correo = lambda event: self.entrada_correo.delete(0, tk.END)

        # Asociación de evento con las entradas correspondientes
        self.entrada_nombre.bind("<Button-1>", self.borrar_texto_nombre)
        self.entrada_apellido.bind("<Button-1>", self.borrar_texto_apellido)
        self.entrada_correo.bind("<Button-1>", self.borrar_texto_correo)


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


    # Validación de los datos
    def confirmacionDatos(self):
            nombre = self.entrada_nombre.get().strip()
            apellido = self.entrada_apellido.get().strip()
            correo = self.entrada_correo.get().strip()

            if nombre == "Investigador" or nombre == "":
                self.Advertencia()

            elif apellido == "Anónimo" or apellido == "":
                self.Advertencia()

            elif correo == "Escriba aquí su correo" or correo == "":
                self.Advertencia()

            else:
                self.destroy()
                self.abrir_ventana_principal(nombre, apellido, correo)


    def Advertencia(self):
        self.mensajeAdvertencia = tk.Label(self, text = "Datos inválidos. Por favor completar todos los campos",
                                            font = "TimesNewRoman 12 italic", bg = color_base, fg = "red")
        self.mensajeAdvertencia.place(x = 210, y = 150)
        

if __name__ == "__main__":
    def abrir_ventana_registro(nombre, apellido, correo):

        # Guardar datos del usuario en archivo .txt
        with open("datosUsuario.txt", "w") as file:
            file.write(f"{nombre},{apellido},{correo}")

    ventana_bienvenida = VentanaRegistro(abrir_ventana_registro)
    ventana_bienvenida.mainloop()