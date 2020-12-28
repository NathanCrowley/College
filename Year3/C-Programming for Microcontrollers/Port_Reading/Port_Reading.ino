/*PORT D = pins 0 to 7
 * 
 *TASK:
 *Wrtie a program that simultaneously read the values of Port D.
 *  - turn on Red LED if any two adjacent pins are HIGH
 *  - turn on Green LED if any two adjacent pins are LOW 
 *  
 * NOTE: you can connect the Port D pins to +5v or 0v with wires. As you change the connections,
 *  your program should illuminate the LEDs appropriately.
 *  
 *  SOLUTION:                    Pins - 01234567
 *    two adjacent pins HIGH would be = 00011000
 *    two adjacent pins HIGH would be = 11100111
 *    set PORT D as all outputs.
 *    Loop through Port D and check if two adjacent pins (i and i+1) are either HIGH or LOW
 *    Turn on red if both high
 *    turn on green ifboth low

 */
int LED_RED = 9;
int LED_GREEN = 8;

void setup() {
  // 0 = input  1 = output
  DDRD = B00000000;
}

void loop() {
           //76543210
    for(int i=0; i<7;i++){
      if(digitalRead(i)==HIGH && digitalRead(i+1)==HIGH){
        digitalWrite(LED_GREEN,LOW);
        digitalWrite(LED_RED,HIGH);
      }
      else if(digitalRead(i)==LOW && digitalRead(i+1)==LOW){
        digitalWrite(LED_RED,LOW);
        digitalWrite(LED_GREEN,HIGH);
      }
    }
    delay(1000);
}
