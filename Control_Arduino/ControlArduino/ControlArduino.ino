/***Este código fue inspirado en el video de YouTube de 
 *  Johann Perez E, cuyo enlace a la fecha de hoy
 *  miércoles 07/06/2023 es: https://youtu.be/XixNg9DGxgo.
 *  Lo anterior, con el objetivo de tener un código base de Arduino
 *  para trasladarlo posteriormente a Python.
***/

int retardo = 5; // Tiempo de retardo en milisegundos
int valor_grados; // Valor ingresado en grados
int num_pasos = 0; // Valor en grados donde se encuentra el motor
String texto; // Text ingresado en la interfaz

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
   while(Serial.available()){ // Lee el valor enviado por el puerto serial
     delay(retardo);
     char c = Serial.read(); // Lee los caracteres
     texto += c; // Convierte caracteres a cadena de caracteres
   }

   if(texto.length() > 0){
    valor_grados = texto.toInt(); // Convierte cadena de caracteres a enteros
    Serial.print(valor_grados);
    Serial.println(" grados");
    delay(retardo);
    valor_grados = valor_grados * 1.4222222222; // Ajuste de 512 vueltas a los 360 grados
    }

   while(valor_grados > num_pasos){ // Gira hacia la izquierda
    paso_izq();
    num_pasos += 1;
   }

   while(valor_grados < num_pasos){ // Gira hacia la derecha
    paso_der();
    num_pasos -= 1;
   }

   texto = ""; // Cadena de texto inicial
   apagado(); // Evita que los motores se calienten
}

void paso_der(){ // Paso hacia la derecha
 digitalWrite(11, LOW); 
 digitalWrite(10, LOW);  
 digitalWrite(9, HIGH);  
 digitalWrite(8, HIGH);  
   delay(retardo); 
   
 digitalWrite(11, LOW); 
 digitalWrite(10, HIGH);  
 digitalWrite(9, HIGH);  
 digitalWrite(8, LOW);  
   delay(retardo); 
   
 digitalWrite(11, HIGH); 
 digitalWrite(10, HIGH);  
 digitalWrite(9, LOW);  
 digitalWrite(8, LOW);  
  delay(retardo); 
  
 digitalWrite(11, HIGH); 
 digitalWrite(10, LOW);  
 digitalWrite(9, LOW);  
 digitalWrite(8, HIGH);  
  delay(retardo);  
}

void paso_izq() {        // Pasos a la izquierda
 digitalWrite(11, HIGH); 
 digitalWrite(10, HIGH);  
 digitalWrite(9, LOW);  
 digitalWrite(8, LOW);  
  delay(retardo); 
 digitalWrite(11, LOW); 
 digitalWrite(10, HIGH);  
 digitalWrite(9, HIGH);  
 digitalWrite(8, LOW);  
  delay(retardo); 
 digitalWrite(11, LOW); 
 digitalWrite(10, LOW);  
 digitalWrite(9, HIGH);  
 digitalWrite(8, HIGH);  
  delay(retardo); 
 digitalWrite(11, HIGH); 
 digitalWrite(10, LOW);  
 digitalWrite(9, LOW);  
 digitalWrite(8, HIGH);  
  delay(retardo); 
}
        
void apagado() {         // Apagado del Motor
 digitalWrite(11, LOW); 
 digitalWrite(10, LOW);  
 digitalWrite(9, LOW);  
 digitalWrite(8, LOW);  
 }
