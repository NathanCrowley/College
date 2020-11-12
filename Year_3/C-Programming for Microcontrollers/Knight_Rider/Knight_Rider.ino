/* Nathan Crowley - 118429092
 *  
  -Create ciruit and code for 6 LEDs to "chase" back and forth.
  -Speed should depend on the ambiant light level
    light level drops - speed increase
    light level increases - speed slows
*/

/*analog input "AmbLS" = Ambiant light sensor connected to analog input A0.
  define the fast and slow speed of LED.
  define the ambiant light level for which the speed should change.
  declare LED number in scope.
*/
int AmbLS = A0;   //connected to port A0.
int LED_speed;    //speed of LED changed by changing delay between LED high and low.
int LED_fast=70;
int LED_slow=300;
int ambiantLL = 150;    //150 is how bright desk side lamp is.
int LED;

/*enable Ambiant light sensor as INPUT
 *DDR states if Input(0) or Output(1)
 */
void setup(){
  pinMode(AmbLS,INPUT);
  DDRB = B111111;    //0x3F;
}

/*
 * Two for loops to go from LED1 to LED5 and back.
 * Call Chekc_ligthtLevel function to check photoresistor and change delay accordinly.
 * Reset LED to all off before moving onto next LED.
*/
void loop(){
  for (LED = 1;LED <= 5;LED++){
    PORTB |= (1<<LED);  //OR LED with 1 so 0|1 = 1. (to loop through LEDs turning them on one after another)
    LED_speed = Check_lightLevel(analogRead(AmbLS));
    delay(LED_speed);
    PORTB = B000000;    //turn all LEDs off again before moving onto next LED.
 }
 for (LED = 4;LED >= 1;LED--){
    PORTB |= (1<<LED);
    LED_speed = Check_lightLevel(analogRead(AmbLS));
    delay(LED_speed);
    PORTB = B000000;
 }
}

//Function to check the ligth value and change speed accordingly
int Check_lightLevel(int lightV){
  int speed_ofLED;
  if (lightV > ambiantLL){                        //if its very bright
    speed_ofLED = LED_slow;                      //slowest LED speed
  }
  else{speed_ofLED = LED_fast;}                  //if its very dark
  return speed_ofLED;                           //fastest speed
}
