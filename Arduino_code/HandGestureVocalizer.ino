//#include <SoftwareSerial.h>
//#define txPin 18
//#define rxPin 19
//int LED = 13;

//SoftwareSerial BTserial(rxPin,txPin);
//constant values for flexsensors
const int sensorPinTHUMB = A0;    // pin that the THUMB flex sensor is attached to
const int sensorPinINDEX = A1;    // pin that the INDEX flex sensor is attached to
const int sensorPinMIDDLE = A2;    // pin that the MIDDLE flex sensor is attached to
const int sensorPinRING = A3;    // pin that the RING flex sensor is attached to
const int sensorPinPINKEY = A4;    // pin that the PINKEY flex sensor is attached to
const int accXpin = A5;
const int accYpin = A6;
const int accZpin = A7; 

//variables
int SVTHUMB = 0;         // the sensor value
int SVINDEX = 0;         // the sensor value
int SVMIDDLE = 0;         // the sensor value
int SVRING = 0;         // the sensor value
int SVPINKEY = 0;         // the sensor value
int X=0;
int Y=0;
int Z=0;
//int count=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
 // BTserial.begin(9600);
  pinMode(sensorPinTHUMB,INPUT);
  pinMode(sensorPinINDEX,INPUT);
  pinMode(sensorPinMIDDLE,INPUT);
  pinMode(sensorPinRING,INPUT);
  pinMode(sensorPinPINKEY,INPUT);
 // pinMode(txPin,OUTPUT);
 pinMode(accXpin,INPUT);
 pinMode(accYpin,INPUT);
 pinMode(accZpin,INPUT);
  Serial.flush();
}

void loop() {

//read flexsensor value
 SVTHUMB = analogRead(sensorPinTHUMB);
 SVINDEX = analogRead(sensorPinINDEX);
 SVMIDDLE = analogRead(sensorPinMIDDLE);
 SVRING = analogRead(sensorPinRING);
 SVPINKEY = analogRead(sensorPinPINKEY);
 X= analogRead(accXpin);
 Y= analogRead(accYpin);
 Z= analogRead(accZpin);


//if data is comming from the flex sensor then show the value 
// Serial.print ("SVTHUMB = "); 
Serial.print(SVTHUMB);
Serial.print(",");
//Serial.print ("SVINDEX = ");
Serial.print(SVINDEX);
Serial.print(",");
//Serial.print ("SVMIDDLE = ");
Serial.print(SVMIDDLE);
Serial.print(",");
//Serial.print ("SVRING = ");
Serial.print(SVRING);
Serial.print(",");
//Serial.print ("SVPINKEY = ");
Serial.print(SVPINKEY);
Serial.print(",");
Serial.print(X);
Serial.print(",");
Serial.print(Y);
Serial.print(",");
Serial.print(Z);
//Serial.print(",");
//Serial.print("And");
Serial.print('\n');
//count= count+1;
Serial.flush();
delay(10);

//if (count==200)
//{
//  Serial.println("!!!!!!!!!!!!@@@@@@@@@@############$$$$$$$$$$$%%%%%%%%%%%^^^^^^^^^^");
//  Serial.println("!!!!!!!!!!!!@@@@@@@@@@############$$$$$$$$$$$%%%%%%%%%%%^^^^^^^^^^");
//  Serial.println("!!!!!!!!!!!!@@@@@@@@@@############$$$$$$$$$$$%%%%%%%%%%%^^^^^^^^^^");
//  Serial.println("!!!!!!!!!!!!@@@@@@@@@@############$$$$$$$$$$$%%%%%%%%%%%^^^^^^^^^^");
//  Serial.println("!!!!!!!!!!!!@@@@@@@@@@############$$$$$$$$$$$%%%%%%%%%%%^^^^^^^^^^");
//  Serial.println("!!!!!!!!!!!!@@@@@@@@@@############$$$$$$$$$$$%%%%%%%%%%%^^^^^^^^^^");
//}

}

//if(Serial.available()>0)//check if there is data incoming or not
//{
//
//char c= Serial.read();
//BTserial.print(c);
//Serial.print("ok");
////digitalWrite(LED,LOW);
////delay(2000);
//}
//delay(10);
//}



  


