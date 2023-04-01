#include <EEPROM.h>
char userInput;
int AddrHigh =0;
int AddrLow =1;

int dataHIGH = 0;
int dataLOW = 0;

int TimeHigh = 0;
int TimeLow = 0;

int dataTimeHigh = 0;
int dataTimeLow = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void getUserData(){
  String userDataUpdate;
  String delayString;
  String blinkCountString;
  String findDelimiter;
  int delimiterInt = 0;

  delay(2000); //Need to wait PySerial send Time
  userDataUpdate = Serial.readString();

  findDelimiter = userDataUpdate.indexOf('-');
  delimiterInt = findDelimiter.toInt();

  delayString = userDataUpdate;
  delayString.remove(delimiterInt);
  
  blinkCountString = userDataUpdate;
  blinkCountString.remove(0,delimiterInt+1);

  dataHIGH = delayString.toInt();
  dataLOW = blinkCountString.toInt();
  
  EEPROM.update(AddrHigh, dataHIGH);
  EEPROM.update(AddrLow, dataLOW);
}


void loop() {
    if (Serial.available()){
        userInput = Serial.read();

      if(userInput == 'u'){
        getUserData();
      }
    }
       dataTimeHigh = EEPROM.read(AddrHigh);
       dataTimeLow = EEPROM.read(AddrLow);

       TimeHigh = dataTimeHigh*100;
       TimeLow = dataTimeLow*100;

    digitalWrite(13, HIGH);
    delay(TimeHigh);
    digitalWrite(13, LOW);
    delay(TimeLow);
 
}
