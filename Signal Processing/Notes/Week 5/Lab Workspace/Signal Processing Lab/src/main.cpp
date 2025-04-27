#include <daclibs.h>

Adafruit_MCP4725 dac;

unsigned long prevMilis = 0;
unsigned long currMilis = prevMilis;

void setup() {
dac.begin(0x60);  //Note: this is an address and could be 0x60, 0x61 or 0x62 depending on manufacturer
Serial.begin(9600);
}

void ramp(){
  int counter;

  for (counter=0;counter<4095;counter++)
  {
    dac.setVoltage(counter, false);  
  }

  for (counter=4095;counter>0;counter--)
  {
    dac.setVoltage(counter, false);  
  }
}

int enable_sampling(int ADCpin = A0, int samplerate = 1000){
  if (currMilis - prevMilis >= samplerate/1000){
    prevMilis = currMilis;

    int sample = analogRead(ADCpin);
    Serial.println(sample);
    dac.setVoltage(sample*4,false);
    return sample;
  }
}

void loop() {
  ramp();

  enable_sampling();
}

