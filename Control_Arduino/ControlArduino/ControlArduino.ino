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

// Variables de la info recibida en Python
int pasos_X = 0; 
int pasos_Y = 0; 
int pasos_Z = 0; 

// Almacenamiento de la posición previa de los motores
int prev_X = 0;
int prev_Y = 0;
int prev_Z = 0;

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
     int c = Serial.read(); // Lee el valor
     
     if (c == 1){
      pasos_X++;
     }
     if (c == 2){
      pasos_Y++;
     }
     if (c == 3){
      pasos_Z++;
     }
    }

   if(c = 1){
      while (pasos_X > prev_X){
        paso_izq_X();
        prev_X++;
      }

      while (pasos_X < prev_X){
        paso_der_X();
        prev_X--;
      }
    }
    
   if(c = 2){
      while (pasos_Y > prev_Y){
        paso_izq_Y();
        prev_Y++;
      }

      while (pasos_Y < prev_Y){
        paso_der_Y();
        prev_Y--;
      }
    }

    if(c = 3){
      while (pasos_Z > prev_Z){
        paso_izq_Z();
        prev_Z++;
      }

      while (pasos_Z < prev_Z){
        paso_der_Z();
        prev_Z--;
      }
    }

   apagado(); // Evita que los motores se calienten
   pasos_X = 0;
   pasos_Y = 0;
   pasos_Z = 0;
}

// Paso hacia la derecha motor X
void paso_der_X(){
 digitalWrite(5, LOW); 
 digitalWrite(4, LOW);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, HIGH);  
   delay(retardo); 
   
 digitalWrite(5, LOW); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, LOW);  
   delay(retardo); 
   
 digitalWrite(5, HIGH); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, LOW);  
 digitalWrite(2, LOW);  
  delay(retardo); 
  
 digitalWrite(5, HIGH); 
 digitalWrite(4, LOW);  
 digitalWrite(3, LOW);  
 digitalWrite(2, HIGH);  
  delay(retardo);  
}

// Pasos a la izquierda motor X
void paso_izq_X() {     
 digitalWrite(5, HIGH); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, LOW);  
 digitalWrite(2, LOW);  
  delay(retardo); 
 digitalWrite(5, LOW); 
 digitalWrite(4, HIGH);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, LOW);  
  delay(retardo); 
 digitalWrite(5, LOW); 
 digitalWrite(4, LOW);  
 digitalWrite(3, HIGH);  
 digitalWrite(2, HIGH);  
  delay(retardo); 
 digitalWrite(5, HIGH); 
 digitalWrite(4, LOW);  
 digitalWrite(3, LOW);  
 digitalWrite(2, HIGH);  
  delay(retardo); 
}

// Paso hacia la derecha motor Y
void paso_der_Y(){     
 digitalWrite(9, LOW); 
 digitalWrite(8, LOW);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, HIGH);  
   delay(retardo); 
   
 digitalWrite(9, LOW); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, LOW);  
   delay(retardo); 
   
 digitalWrite(9, HIGH); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, LOW);  
 digitalWrite(6, LOW);  
  delay(retardo); 
  
 digitalWrite(9, HIGH); 
 digitalWrite(8, LOW);  
 digitalWrite(7, LOW);  
 digitalWrite(6, HIGH);  
  delay(retardo);  
}

// Pasos a la izquierda motor Y
void paso_izq_Y() {     
 digitalWrite(9, HIGH); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, LOW);  
 digitalWrite(6, LOW);  
  delay(retardo); 
 digitalWrite(9, LOW); 
 digitalWrite(8, HIGH);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, LOW);  
  delay(retardo); 
 digitalWrite(9, LOW); 
 digitalWrite(8, LOW);  
 digitalWrite(7, HIGH);  
 digitalWrite(6, HIGH);  
  delay(retardo); 
 digitalWrite(9, HIGH); 
 digitalWrite(8, LOW);  
 digitalWrite(7, LOW);  
 digitalWrite(6, HIGH);  
  delay(retardo); 
}

// Paso hacia la derecha motor Z
void paso_der_Z(){     
 digitalWrite(13, LOW); 
 digitalWrite(12, LOW);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, HIGH);  
   delay(retardo); 
   
 digitalWrite(13, LOW); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, LOW);  
   delay(retardo); 
   
 digitalWrite(13, HIGH); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, LOW);  
 digitalWrite(10, LOW);  
  delay(retardo); 
  
 digitalWrite(13, HIGH); 
 digitalWrite(12, LOW);  
 digitalWrite(11, LOW);  
 digitalWrite(10, HIGH);  
  delay(retardo);  
}

// Pasos a la izquierda motor Z
void paso_izq_Z() {     
 digitalWrite(13, HIGH); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, LOW);  
 digitalWrite(10, LOW);  
  delay(retardo); 
 digitalWrite(13, LOW); 
 digitalWrite(12, HIGH);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, LOW);  
  delay(retardo); 
 digitalWrite(13, LOW); 
 digitalWrite(12, LOW);  
 digitalWrite(11, HIGH);  
 digitalWrite(10, HIGH);  
  delay(retardo); 
 digitalWrite(13, HIGH); 
 digitalWrite(12, LOW);  
 digitalWrite(11, LOW);  
 digitalWrite(10, HIGH);  
  delay(retardo); 
}

// Apagado de los motores
void apagado() {       
 digitalWrite(13, LOW); 
 digitalWrite(12, LOW);  
 digitalWrite(11, LOW);  
 digitalWrite(10, LOW);
 digitalWrite(9, LOW); 
 digitalWrite(8, LOW);  
 digitalWrite(7, LOW);  
 digitalWrite(6, LOW);
 digitalWrite(5, LOW); 
 digitalWrite(4, LOW);  
 digitalWrite(3, LOW);  
 digitalWrite(2, LOW);  
 }
