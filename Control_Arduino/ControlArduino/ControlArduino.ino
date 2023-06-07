/***Este código fue inspirado en el video de YouTube de 
 *  Johann Perez E, cuyo enlace a la fecha de hoy
 *  miércoles 07/06/2023 es: https://youtu.be/XixNg9DGxgo.
 *  Lo anterior, con el objetivo de tener un código base de Arduino
 *  para trasladarlo posteriormente a Python.
***/

// Librería motor paso a paso
#include <Stepper.h>


// Pasos para dar una revolución completa
int pasosRev = 2048; // Esto, para el motor 28BYJ-48
int vel = 10; // Revoluciones/min
int retraso = 500; // ms

Stepper motor(pasosRev, 2, 3, 4, 5); // Nombrar motor y pines de control


void setup() {
  motor.setSpeed(vel);
  
}

void loop() {
  motor.step(pasosRev);
  delay(retraso);
  motor.step(-pasosRev);
  delay(retraso);
}
