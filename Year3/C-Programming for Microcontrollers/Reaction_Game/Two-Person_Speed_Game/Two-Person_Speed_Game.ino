/*TASK:
 * - press start button to start the game. After X seconds where 0<X<10 buzzzer sounds.
 * - each player has a stop button. The player who hits their button first is winner.
 *    - turn on green LED for winner
 *    - turn on red LED for loser
 * - record the difference in the reactions of winner and loser ( winner speed - loser speed).
 * - if hit stop  button before buzzer, they lose!!
 * - next game should auto start after a new random X seconds.
 * - after 3 games:
 *    - game over, write results of rounds to Serial Monitor
 *    - write winner of each round
 *    - write winning time
 *    - write the difference in player times
 *  
 * EXAMPLE REPORT:
 *  - Winner is Player1:
 *      - Game1 (20ms), Difference (-5ms)
 *      - Game2 (25ms), Difference (3ms)
 *      - Game3 (18ms), Difference (-2ms)
*/
#define ButtonONE 2
#define ButtonTWO 3
#define ButtonSTART 4
//-------------------
#define P1greenLED 13
#define P1redLED 12
//-------------------
#define P2greenLED 11
#define P2redLED 10
//-------------------
#define buzzer 8

int B1state;
int B2state;
int BstartState;
int X;
int startTime;
int P1reactionTime;
int P2reactionTime;
int P1wins;
int P2wins;
String results;

void setup(){
  pinMode(P1greenLED,OUTPUT);
  pinMode(P1redLED,OUTPUT);
  //-------------------------
  pinMode(P2greenLED,OUTPUT);
  pinMode(P2redLED,OUTPUT);
  pinMode(ButtonONE,INPUT);
  pinMode(ButtonTWO,INPUT);
  Serial.begin(9600);
}

void loop(){
  B1state = digitalRead(ButtonONE);
  B2state = digitalRead(ButtonTWO);
  BstartState = digitalRead(ButtonSTART);

  //generate X seconds
  if (BstartState == HIGH){       //start game button
     int var = 1;
     while(var < 3){
        X = random(0,11);             //random X
        X = X*1000;
        delay(X);
        //Sound buzzer
        tone(buzzer,1000,500);
        //start timer
        startTime = millis();         
        if (B1state == HIGH){
          //when player one hits the button stop the timer and calculate thier reaction time
          int P1stopTime;
          P1stopTime = millis();
          P1reactionTime = P1stopTime - startTime;
        }
        if(B2state == HIGH){
          int P2stopTime;
          P2stopTime = millis();
          P2reactionTime = P2stopTime - startTime;
        }
        //find out who is winner turn on Green light for winner and Red light for loser
        if(P1reactionTime < P2reactionTime){    //P1 reacted faster
          String WinningReport = "";
          P1wins++;
          digitalWrite(P1greenLED,HIGH);
          digitalWrite(P2redLED,HIGH);
        }
        else{
          String WinningReport = "";
          P2wins++;
          digitalWrite(P2greenLED,HIGH);
          digitalWrite(P1redLED,HIGH);
        }
     }
     var++;
    //write results to serial monitor
    if(P1wins > P2wins){
      //P1 won
      String winner = "Winner is Player1";
    }else{
      //P2 won
      String winner = "Winner is Player2";
    }
    Serial.print(winner);
  }
}
