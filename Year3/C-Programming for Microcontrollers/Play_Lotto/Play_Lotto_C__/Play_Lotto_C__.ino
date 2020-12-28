/*
 * Task: write program to generate sets of 6, unique, randomly chosen numbers in the range 1 to 42.
 *        These will be sets of lotto numbers.
 *        The program should produce a set of lotto numbers on a new line of the Serial Monitor 
 *        approximately every 10 seconds.
 *        Hint: use random() and milis() functions.
 *        
 * - random(min,max):
 *      returns a random number between min and max-1, data type = long.
 * 
 * - milis():
 *      time = milis().
 *      returns number of milisieconds passed since program started, data type = unsigned long.
 *      
 * Solution:
 *    - use random(1,43) to generate number between 1 and 42. 
 *      Do this for all 6 unique numbers of the lotto ticekt.
 *      Store in an array. (int lotto[6];)
 *        to append to arary we use lotto[0] = 10; 
 *                                  lotto[1] = 33;
 *                                  ...
 *      print to serial monitor.
 *      
 *    - Use milis() to check if 10 seconds has passed, if true then generate a new lotto array.
 *            
*/            
#define ARRAY_SIZE(arr) sizeof(arr)/sizeof(arr[0])

long lotto_Numbers[6];             //initaites array of size 6 of all 0's.
long random_Number;                //random number to be appended to lotto array.

unsigned long time_passed;         //millis() returns unsigned long.
long seconds=10;                 //***must use a long when doing calculation operations on another long!!!!

void setup(){
    Serial.begin(9600);            //begin serial monitor at bit rate of 9600 bits per second.  
    randomSeed(analogRead(0));     
    /* if analog input pin 0 is unconnected, random analog
     noise will cause the call to randomSeed() to generate
     different seed numbers each time the sketch runs.
     randomSeed() will then shuffle the random function.
    */
}
                                       
void loop(){  
  delay(1000);
  time_passed = millis();          //return how long has passed since program began in milliseconds
  time_passed = time_passed/1000; //divide this by ten seconds (1000) to convet to 1.2345.
  time_passed = time_passed%seconds;    //modulus divide to calculate if its divisable by 10 (seconds).
  if(time_passed == 0){
    //call function that prints lotto array
    printTicket(lotto_Numbers,ARRAY_SIZE(lotto_Numbers));
  }else(Serial.println(time_passed));
}

//function to print lotto array
void printTicket(long array_Input[],int arraySize){
    //generate 6 random numbers
    for(int i = 0; i < arraySize; i++){
      //generate random numer
      random_Number = random(1,43);    //43(not 42) because random(min,max) loops up to max-1
      //append to lotto array
      array_Input[i] = random_Number;
    }
    //print array
    Serial.print("Lotto_Numbers: [");
    for (int i = 0; i < arraySize -1; i++){
      Serial.print(array_Input[i]);
      Serial.print(",");
    }
    Serial.print(array_Input[arraySize-1]);
    Serial.println("]");
}
