/***Este código fue inspirado en el video de YouTube de 
 *  Johann Perez E, cuyo enlace a la fecha de hoy
 *  miércoles 07/06/2023 es: https://youtu.be/XixNg9DGxgo.
 *  Lo anterior, con el objetivo de tener un código base de Arduino
 *  para trasladarlo posteriormente a Python.
***/

// Librería motor paso a paso
#include <Stepper.h>


// Pasos para dar una revolución completa
const int stepsPerRevolution = 2048;
const int motorPin1 = 6;
const int motorPin2 = 7;
const int motorPin3 = 8;
const int motorPin4 = 9;

int vel = 5; // Revoluciones/min
unsigned long retraso = 2000; // ms
int direction = 1; // 1 sentido horario, -1 sentido antihorario

Stepper motor(stepsPerRevolution, motorPin1, motorPin2, motorPin3, motorPin4); // Nombrar motor y pines de control


void setup() {
  motor.setSpeed(vel);
}

void loop() {
  // Girar en el sentido actual
  for (int i = 0; i < stepsPerRevolution; i++) {
    motor.step(1);
    delayMicroseconds(1000);
  }

  // Esperar el tiempo de retraso
  delay(retraso);

  // Cambiar de sentido
  direction *= -1;
  motor.setSpeed(5 * abs(direction));
}
