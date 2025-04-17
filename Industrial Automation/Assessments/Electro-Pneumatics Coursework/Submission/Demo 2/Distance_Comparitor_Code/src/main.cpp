
#include <Arduino.h>
#include <HCSR04.h>

const int bluePin = 8;
const int greenPin = 9;
const int yellowPin = 10;

byte triggerPin = 4;
byte echoCount = 2;
byte* echoPins = new byte[echoCount] {3, 5};

void doubleActingPiston_out(){
  Serial.println("doubleActingPiston_out");
  digitalWrite(bluePin, HIGH);
  digitalWrite(yellowPin, LOW);
}
void doubleActingPiston_in(){
  Serial.println("doubleActingPiston_in");
  digitalWrite(bluePin, LOW);
  digitalWrite(yellowPin, HIGH);
}
void doubleActingPiston_lock(){
  Serial.println("doubleActingPiston_lock");
  digitalWrite(bluePin, LOW);
  digitalWrite(yellowPin, LOW);
}
void singleActingPiston_trigger(){
  Serial.println("singleActingPiston_trigger");
  digitalWrite(greenPin, HIGH);
  delay(500);
  digitalWrite(greenPin, LOW);
}

void setup () {
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  Serial.begin(9600);
  HCSR04.begin(triggerPin, echoPins, echoCount);
}

void loop () {
  double* distances = HCSR04.measureDistanceCm();

  if (trunc(distances[0]) == trunc(distances[1])){ 
    doubleActingPiston_lock();
    singleActingPiston_trigger();
  }
  if (distances[0] >= distances[1]){ 
    doubleActingPiston_in(); }
  else if (distances[0] <= distances[1]){
    doubleActingPiston_out(); }

  for (int i = 0; i < echoCount; i++) {
    Serial.print(i + 1);
    Serial.print(": ");
    Serial.print(distances[i]);
    Serial.println(" cm");
  }
  
  Serial.println("---");
}
