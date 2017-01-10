/*

Desibelimittari, kehittämisprojekti

*/

#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
#ifndef _DB_METER_LIB_
#define _DB_METER_LIB_
 
#define ANALOG_SOUND_PIN 0
#define ADC_SOUND_REF 40
#define DB_SOUND_REF 50
#define SOUND_PIN A0
 
#include "Arduino.h"
#include "math.h"
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
 
// Returns noise level in decibels double get_abs_db(int *input = NULL, int sound_pin = 0);
 
#endif
 
// Returns noise level in decibels
double get_abs_db(int *input, int sound_pin) {
  int x = (!input) ? analogRead(sound_pin) : *input;
  return 20 * log((double)x / (double)ADC_SOUND_REF) + DB_SOUND_REF; }
 
  //Connection begin
RF24 radio(40, 53);
 
int Desibels=1;
 
const uint64_t RecvAddresses = 0x0000000022LL;
const uint64_t SendAddresses = 0x0000000002LL;
const int RequestData = 1111;
 
void setup() {
 
    // Initilize hardware serial
    lcd.begin(16, 2);   // Print a message to the LCD.
    lcd.print("Desibelit!");
    //pinMode(A0, INPUT);
    
    // initialize serial:
    Serial.begin(9600);
 
  radio.begin();
  radio.openWritingPipe(SendAddresses);
  radio.openReadingPipe(1, RecvAddresses);
 
  radio.startListening();
 
  //radio stop
  }
 
 
int msgint=0;
char message[4];
char msgtosend[4];
 
void loop() {
 
  int level = analogRead(SOUND_PIN);
  int *plevel = &level;
  
  lcd.setCursor(0, 1);  //print to LCD
  lcd.print(get_abs_db(plevel));
  delay(300);
  
  int numero = get_abs_db(plevel);
  
    while(radio.available())
    {
      radio.read(&message, sizeof(message));
      memcpy(&msgint, &message, sizeof(int));
      Serial.println("got message.");
      
      if(msgint==1111)
      {
        Serial.println("sending.");
        radio.stopListening();
        memcpy(&msgtosend, &numero, sizeof(int));
        Serial.println(numero);
        radio.openWritingPipe(SendAddresses);
        
        radio.write(&msgtosend, sizeof(msgtosend));
        radio.startListening();
        } 
 
     } 
 } 
