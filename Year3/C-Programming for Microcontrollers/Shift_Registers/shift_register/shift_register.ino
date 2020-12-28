#include <IRremote.h>           //include infrared remote hander file.
int RECIERVER_PIN = 7;          //set the pin that is connected to IR Reciever.
IRrecv irrecv(RECIERVER_PIN);  
decode_results results;     

//Pin connected to ST_CP of 74HC595
int latchPin = 8;
//Pin connected to SH_CP of 74HC595
int clockPin = 12;
////Pin connected to DS of 74HC595
int dataPin = 11;

#define pd2 2

void setup() {
  Serial.begin(9600);           //initalise the serial monitor with 9600 bits per second data rate.
  irrecv.enableIRIn();          //initalise to recieve IR signals.
  pinMode(latchPin,OUTPUT);     //set all pins as OUTPUT for the main loop.
  pinMode(clockPin,OUTPUT);
  pinMode(dataPin,OUTPUT);
  pinMode(pd2,OUTPUT);
}

byte LSBmask = 0xff;
void loop() {
  if(irrecv.decode(&results)){              //returns 0 if no data ready, 1 if data ready.
    if(results.value != 4294967295){        
/*PART A: */
      digitalWrite(latchPin, LOW);          
      myShiftOut(clockPin, LSBFIRST, results.value&LSBmask);
      digitalWrite(latchPin, HIGH); 
      /*Uncomment these to see the program running in the Serial Moniotr.
      Serial.println(results.value,HEX);
      Serial.print("HEX Least significant Byte: ");
      Serial.println(results.value&LSBmask, HEX); 
      Serial.println(results.value&LSBmask, BIN);*/
      delay(1000);
/* PART B*/  
      digitalWrite(latchPin, LOW);          
      myShiftOut(clockPin, LSBFIRST, (results.value&0xff00)>>8);
      digitalWrite(latchPin, HIGH);
      /* Uncomment these to see the program running in the Serial Moniotr.
      Serial.println(results.value,HEX);
      Serial.print("HEX Middle Byte: ");
      Serial.println((results.value&0xff00)>>8, HEX);
      Serial.println((results.value&0xff00)>>8, BIN);*/
    }
   Serial.println();
   irrecv.resume();     
  }
}

/* PART C*/
void myShiftOut(uint8_t clockPin, uint8_t bitOrder, uint8_t val){
  uint8_t i;
  for(i = 0; i<8; i++){
    if(bitOrder == LSBFIRST){
      if(val&(1<<i)){   //check if the bit is 1
        PORTD &= B00000100;   //set pin 2 to 1
      }else{            //else its 0
        PORTD &= B00000000;   //set pin 2 to 0.
      }
    }else{
      if(val&(1<<(7-i))){
        PORTD &= B00000100;   //set pin 2 to 1
      }else{
        PORTD &= B00000000;   //set pin 2 to 0.
      }
    }
      digitalWrite(clockPin, HIGH);
      digitalWrite(clockPin, LOW); 
  }
}
