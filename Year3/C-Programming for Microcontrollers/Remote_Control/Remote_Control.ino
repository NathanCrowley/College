/*
 * TASK: write a program and build circuit to capture button presses fro  the IR Remote.
 *      if one of the remote buttons is pressed, the corresponding number should be wirtten to the 
 *      Serial monitor
 * SOLUTION:
 * - decode the signal 
 * - store decoding resutls in an integer variable
 * - array of the results values for 0-9 stored in the same index as the digit. (So value for 0 is at index 0)
 * - for loop to check if the incoming IR sensor result is in the list of 0-9.
 *    - if it is then print out the index of the digit to the serial monitor.
 * - restart the ISR state machine with resume function.
   * 0 = 26775
   * 1 = 12495
   * 2 = 6375
   * 3 = 31365
   * 4 = 4335
   * 5 = 14535
   * 6 = 23205
   * 7 = 17085
   * 8 = 19125
   * 9 = 21165
*/

#include <IRremote.h>           //include infrared remote hander file.
int RECIERVER_PIN = 7;          //set the pin that is connected to IR Reciever.
IRrecv irrecv(RECIERVER_PIN);  
decode_results results;         

void setup() {
  Serial.begin(9600);           //initalise the serial monitor with 9600 bits per second data rate.
  irrecv.enableIRIn();          //initalise to recieve IR signals.
}

void loop() {
  if(irrecv.decode(&results)){              //returns 0 if no data ready, 1 if data ready.
    int resutlsValue = results.value;      
    Serial.println(resutlsValue);
    int numberButtons[10] = {26775,12495,6375,31365,4335,14535,23205,17085,19125,21165};
    for(int i=0; i<(sizeof(numberButtons)/sizeof(numberButtons[0])); i++){
      if(numberButtons[i] == resutlsValue){ 
        Serial.println(i);
      }
    }
    irrecv.resume();
  }
}
