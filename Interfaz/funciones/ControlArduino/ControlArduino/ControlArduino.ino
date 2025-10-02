
/***Este código fue inspirado en los videos de YouTube de 
 *  Johann Perez E, cuyo enlace a la fecha de hoy
 *  miércoles 07/06/2023 es: https://youtu.be/XixNg9DGxgo y
 *  Víctor Romero, cuyo enlace a la fecha de hoy jueves 31/08/2023
 *  es: https://youtu.be/BXd-Cceh-R4?si=jDI3Wc2Zp8jtDXYE.
 *  Lo anterior, con el objetivo de tener un código base de Arduino
 *  para trasladarlo posteriormente a Python.
***/

// Constantes para ejes
#define EJE_X 0
#define EJE_Y 1
#define EJE_Z 2

int retardo = 5; // Tiempo de retardo en milisegundos
int pos_origen = 0; // Valor en grados donde se encuentra el motor
const int laserPin = A0; // Pin laser

// Pines motores
int pinesMotor[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
char ultimoCaracter = '0';

// Variables de posición global
int pos_x = 0, pos_y = 0, pos_z = 0; 

void setup(){
Serial.begin(115200); // Velocidad de transmision de datos

// Configura pines de motores
for(int i = 0; i < 12; i++) {
  pinMode(pinesMotor[i], OUTPUT);
}

// Láser para Arduino
pinMode(laserPin, OUTPUT);
digitalWrite(laserPin, LOW);

Serial.println("ARDUINO_READY"); // Mensaje de inicialización
}

void loop(){
  if (Serial.available() > 0){ // Revisa información disponible en el puerto serial
   String coordenadas = Serial.readStringUntil("\n");
   ejecucionCoordenadas(coordenadas);
  }
  apagado(); // Evita calentamiento
}

void ejecucionCoordenadas(String cmd) {
  cmd.trim(); // Remueve espacios 

  if (cmd.startsWith("M")){
    cmd = cmd.substring(1); // Remueve la "M"

    // Ubica que haya dos comas para tener el formato correcto (x, y, z)
    int coma1 = cmd.indexOf(",");
    int coma2 = cmd.indexOf(",", coma1 + 1);

    // verifica que se cumpla la condición anterior
    if (coma1 != -1 && coma2 != -1) {
      int pasos_x = cmd.substring(0, coma1).toInt();
      int pasos_y = cmd.substring(coma1 + 1, coma2).toInt();
      int pasos_z = cmd.substring(coma2 + 1).toInt();

      // Ejecuta movimiento
      moverMotor(EJE_X, pasos_x);
      moverMotor(EJE_Y, pasos_y);
      moverMotor(EJE_Z, pasos_z);

      Serial.println("OK"); // Confirmación
    }
  }

  // Controlador Láser
  else if (cmd == "LASER_ON") {
    digitalWrite(laserPin, HIGH);
    Serial.println("LASER_ON_OK");
  }
  else if (cmd == "LASER_OFF") {
    digitalWrite(laserPin, LOW);
    Serial.println("LASER_OFF_OK");
  }

  // Comando de posición: "GET_POS"
  else if (cmd == "GET_POS") {
    Serial.print("POS: ");
    Serial.print(pos_x);
    Serial.print(",");
    Serial.print(pos_y);
    Serial.print(",");
    Serial.print(pos_z);
  }
}

// Función que mueve los motores
void moverMotor(int eje, int pasos) {
  if (pasos == 0) return;

  int direccion = (pasos > 0) ? 1 : -1;
  int pasos_abs = abs(pasos);
  int pin_inicio, pin_final;

  // Define pines según eje
  switch (eje) {
    case EJE_X: pin_inicio = 8; pin_final = 11; break;
    case EJE_Y: pin_inicio = 0; pin_final = 3; break;
    case EJE_Z: pin_inicio = 4; pin_final = 7; break;
    default: return;
  }

  // Ejecuta los pasos
  for (int i = 0; i < pasos_abs; i++) {
    if (direccion > 0) {
      paso_derecha(pin_inicio, pin_final);
    } else {
      paso_izquierda(pin_inicio, pin_final);
    }

    // Actualiza posición
    switch (eje) {
      case EJE_X: pos_x += direccion; break;
      case EJE_Y: pos_y += direccion; break;
      case EJE_Z: pos_z += direccion; break;
    }
  }
}

// Funciones para movimiento de motores
void paso_derecha(int pin_inicio, int pin_final) {
  byte secuencia[8] = {
    B0001, B0011, B0010, B0110, B0100, B1100, B1000, B1001
  };

  ejecutar_secuencia(pin_inicio, pin_final, secuencia);
}

void paso_izquierda(int pin_inicio, int pin_final) {
  byte secuencia[8] = {
    B1001, B1000, B1100, B0100, B0110, B0010, B0011, B0001
  };

  ejecutar_secuencia(pin_inicio, pin_final, secuencia);
}

void ejecutar_secuencia(int pin_inicio, int pin_final, byte secuencia[8]) {
  for (int paso = 0; paso < 0; paso++) {
    for (int pin = pin_inicio; pin <= pin_final; pin++) {
      digitalWrite(pinesMotor[pin], bitRead(secuencia[paso], pin - pin_inicio));
    }
    delayMicroseconds(retardo * 1000); 
  }
}

// Apagado de motores
void apagado() {
  for(int i = 0; i < 12; i++) {
    digitalWrite(pinesMotor[i], LOW);
  }
}