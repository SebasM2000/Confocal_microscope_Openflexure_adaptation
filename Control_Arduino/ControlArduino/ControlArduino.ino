
/***Este código fue inspirado en los videos de YouTube de 
 *  Johann Perez E, cuyo enlace a la fecha de hoy
 *  miércoles 07/06/2023 es: https://youtu.be/XixNg9DGxgo y
 *  Víctor Romero, cuyo enlace a la fecha de hoy jueves 31/08/2023
 *  es: https://youtu.be/BXd-Cceh-R4?si=jDI3Wc2Zp8jtDXYE.
 *  Lo anterior, con el objetivo de tener un código base de Arduino
 *  para trasladarlo posteriormente a Python.
***/

int retardo = 5; // Tiempo de retardo en milisegundos
int pos_origen = 0; // Valor en grados donde se encuentra el motor
int pinesMotor[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

// Variables de la info recibida en Python
int pasos_X = 0; 
int pasos_Y = 0; 
int pasos_Z = 0; 

void setup(){
Serial.begin(9600); // Establecer velocidad de transmision de datos a 9600 baudios

// Motor en X
pinMode(2, OUTPUT);
pinMode(3, OUTPUT);
pinMode(4, OUTPUT);
pinMode(5, OUTPUT);

// Motor en Y
pinMode(6, OUTPUT);
pinMode(7, OUTPUT);
pinMode(8, OUTPUT);
pinMode(9, OUTPUT);

// Motor en Z
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
pinMode(12, OUTPUT);
pinMode(13, OUTPUT);
}

void loop(){
   if (Serial.available() > 0){ // Lee el valor enviado por el puerto serial
     char c = Serial.read(); // Lee el valor
     
     if (c == '1'){
      paso_izq_X();
     }
     if (c == '2'){
      paso_der_X();
     }
     if (c == '3'){
      paso_izq_Y();
     }
     if (c == '4'){
      paso_der_Y();
     }
     if (c == '5'){
      paso_izq_Z();
     }
     if (c == '6'){
      paso_der_Z();
     }
    }

   apagado(); // Evita que los motores se calienten
}

// Paso hacia la derecha motor X
void paso_der_X(){
 digitalWrite(pinesMotor[0], LOW);  
 digitalWrite(pinesMotor[1], LOW); 
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], HIGH);  
 delay(retardo); 
   
 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], HIGH);  
 digitalWrite(pinesMotor[3], HIGH);  
   delay(retardo); 
   
 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], HIGH);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo); 
  
 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], HIGH);  
 digitalWrite(pinesMotor[2], HIGH);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);  

 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], HIGH);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[0], HIGH); 
 digitalWrite(pinesMotor[1], HIGH);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[0], HIGH); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[0], HIGH); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], HIGH);  
  delay(retardo);
}

// Pasos a la izquierda motor X
void paso_izq_X() {     
 digitalWrite(pinesMotor[0], HIGH);  
 digitalWrite(pinesMotor[1], LOW); 
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], HIGH);  
 delay(retardo); 
   
 digitalWrite(pinesMotor[0], HIGH); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
   delay(retardo); 
   
 digitalWrite(pinesMotor[0], HIGH); 
 digitalWrite(pinesMotor[1], HIGH);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo); 
  
 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], HIGH);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);  

 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], HIGH);  
 digitalWrite(pinesMotor[2], HIGH);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], HIGH);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[0], LOW); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], HIGH);  
 digitalWrite(pinesMotor[3], HIGH);  
  delay(retardo);

 digitalWrite(pinesMotor[0], HIGH); 
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[3], LOW);  
  delay(retardo);
}

// Paso hacia la derecha motor Y
void paso_der_Y(){
 digitalWrite(pinesMotor[4], LOW);  
 digitalWrite(pinesMotor[5], LOW); 
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], HIGH);  
 delay(retardo); 
   
 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], HIGH);  
 digitalWrite(pinesMotor[7], HIGH);  
   delay(retardo); 
   
 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], HIGH);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo); 
  
 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], HIGH);  
 digitalWrite(pinesMotor[6], HIGH);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);  

 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], HIGH);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[4], HIGH); 
 digitalWrite(pinesMotor[5], HIGH);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[4], HIGH); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[4], HIGH); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], HIGH);  
  delay(retardo);
}

// Pasos a la izquierda motor Y
void paso_izq_Y() {     
 digitalWrite(pinesMotor[4], HIGH);  
 digitalWrite(pinesMotor[5], LOW); 
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], HIGH);  
 delay(retardo); 
   
 digitalWrite(pinesMotor[4], HIGH); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
   delay(retardo); 
   
 digitalWrite(pinesMotor[4], HIGH); 
 digitalWrite(pinesMotor[5], HIGH);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo); 
  
 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], HIGH);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);  

 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], HIGH);  
 digitalWrite(pinesMotor[6], HIGH);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], HIGH);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[4], LOW); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], HIGH);  
 digitalWrite(pinesMotor[7], HIGH);  
  delay(retardo);

 digitalWrite(pinesMotor[4], HIGH); 
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[7], LOW);  
  delay(retardo);
}

// Paso hacia la derecha motor Z
void paso_der_Z(){     
 digitalWrite(pinesMotor[8], LOW);  
 digitalWrite(pinesMotor[9], LOW); 
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], HIGH);  
 delay(retardo); 
   
 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], HIGH);  
 digitalWrite(pinesMotor[11], HIGH);  
   delay(retardo); 
   
 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], HIGH);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo); 
  
 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], HIGH);  
 digitalWrite(pinesMotor[10], HIGH);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);  

 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], HIGH);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[8], HIGH); 
 digitalWrite(pinesMotor[9], HIGH);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[8], HIGH); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[8], HIGH); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], HIGH);  
  delay(retardo);
}

// Pasos a la izquierda motor Z
void paso_izq_Z() {     
 digitalWrite(pinesMotor[8], HIGH);  
 digitalWrite(pinesMotor[9], LOW); 
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], HIGH);  
 delay(retardo); 
   
 digitalWrite(pinesMotor[8], HIGH); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
   delay(retardo); 
   
 digitalWrite(pinesMotor[8], HIGH); 
 digitalWrite(pinesMotor[9], HIGH);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo); 
  
 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], HIGH);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);  

 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], HIGH);  
 digitalWrite(pinesMotor[10], HIGH);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], HIGH);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);

 digitalWrite(pinesMotor[8], LOW); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], HIGH);  
 digitalWrite(pinesMotor[11], HIGH);  
  delay(retardo);

 digitalWrite(pinesMotor[8], HIGH); 
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[11], LOW);  
  delay(retardo);
}

// Apagado de los motores
void apagado() {       
 digitalWrite(pinesMotor[11], LOW); 
 digitalWrite(pinesMotor[10], LOW);  
 digitalWrite(pinesMotor[9], LOW);  
 digitalWrite(pinesMotor[8], LOW);
 digitalWrite(pinesMotor[7], LOW); 
 digitalWrite(pinesMotor[6], LOW);  
 digitalWrite(pinesMotor[5], LOW);  
 digitalWrite(pinesMotor[4], LOW);
 digitalWrite(pinesMotor[3], LOW); 
 digitalWrite(pinesMotor[2], LOW);  
 digitalWrite(pinesMotor[1], LOW);  
 digitalWrite(pinesMotor[0], LOW);  
 }
