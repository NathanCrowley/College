/*
 * Nathan Crowley - 118429092
 * Code to play an inputed note (from Serial Monitor) on a buzzer connected to an Arduino UNO.
 * **Note: since I defined F as 22 there is an error mentioning that I am redefining F.
 *          I am aware of this error and I have left it as it looks better having all notes in Capital letters.
 *          And the code still works with this warning.
 ****
 *TO RUN:
 *    open Serial monitor.
 *    enter notes (Capital letters only).
 *    press send.
 *Example:  
 *  - Jingle Bells.
        EEE EEE EGCDE   FFF FFEE EE  EDDED G   EEE EEE EGCDE GGFDCC
 *  - Happy Birthday song.
        CCDCFE  CCDCGF  CC CC A FED A A AFGF
 *  - Twinkle twinkle.
        CCGGAAG FFEEDDC GGFFEED GGFFEEDCCGGAAG FFEE DD C
*/

//set pin 9 as pin for buzzer.
#define buzzer 9
//frequencies of notes.
#define C 263
#define D 294
#define E 330
#define F 350                        //be careful of error with redefining F.
#define G 392
#define A 440
#define B 467
#define highC 1046

//lists to check if input notes are correct.
int notes[] = {C,D,E,F,G,A,B};                 //list of frequencies used in the play function.
char PossibleNotes[] = {'C','D','E','F','G','A','B'};   //list of notes used to compare with Serial input as to play the correct note.

char inputNote;                     // what type the users input from the serial monitor is.
//*Important as we compare this with char in possiblenotes list to determine what note to play.

int spaceDelay = 25;                // how long space input will delay for.
int notedelay = 100;                //how long each note is played for.

void setup() {
  pinMode(buzzer,OUTPUT);           //set buzzer as output.
  Serial.begin(9600);               //begin the serial input with rate of 9600 bits per second.
}

void loop() {
  if(Serial.available()>0){         //is there input available.
    inputNote = Serial.read();      //save the input as inputNote.
    Serial.print(inputNote);
    //conditional statement to check what to do with input
    if(isNote(inputNote)){          //if input in set of notes then play it.
      //play the inputed note
      for(int i=0; i<sizeof(PossibleNotes); i++){   //loop through list of possible notes
        if(PossibleNotes[i] == inputNote){          //if note is in this list
          play(notes[i]);                           //call fucntion to play the corresponding note
        }
       /**why I use both PossibleNote and Notes:
        *     use PossibleNotes to compare the input character with list of characters
        *     use notes list to select the corresponding frequency.
       */  
      }
    }
    else if(isSpace(inputNote)){    //or if its a space have period of silence.
      delay(spaceDelay);
    }
    //else ignore.
  }
}

//fucntion to check if the input is in the set of notes
boolean isNote(char input){         //return true or false for the fucntion in conditon if statement.
  for(int i=0; i<sizeof(PossibleNotes); i++){
    if(PossibleNotes[i] == input){
      return true;
    }
  }
  return false;
}

//fucntion to calculate period based on frequency
int play(float frequency){            //NB** must be floats to allow the calculation!!!!
   int var = 0;
   while(var < notedelay){                  //while loop to play the note for 200 miliseconds.
    float period;
    period = ((1/frequency)*1000000);   //multiply 0.0038 seconds by million to convert to microseconds.
    digitalWrite(buzzer,HIGH);          //digital output on
    delayMicroseconds(period/2);        //delay is half the period
    digitalWrite(buzzer,LOW);           //digital output off
    delayMicroseconds(period/2);        //delay is half the period
    var++;
   }
}
