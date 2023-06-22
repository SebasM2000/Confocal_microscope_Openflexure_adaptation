import serial
import time

class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print(f"El {self.marca} {self.modelo} ha arrancado")

    def frenar(self):
        self.arrancado = False
        print(f"El {self.marca} {self.modelo} ha frenado")

nombre = carro("Renault", "Laguna")
tesla = carro("Tesla", "Modelo 3")

print(type(nombre))
print(type(tesla))

print(nombre.marca, nombre.modelo)
print(tesla.marca, tesla.modelo)

nombre.arrancar()
tesla.arrancar()

print(nombre.arrancado)
print(tesla.arrancado)

nombre.frenar()
tesla.frenar()