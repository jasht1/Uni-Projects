#include <Wire.h>
#include "Adafruit_MCP4725.h"
Adafruit_MCP4725 dac;

void setup() {
  // put your setup code here, to run once:
dac.begin(0x60);  //Note: this is an address and could be 0x60, 0x61 or 0x62 depending on manufacturer
}

void loop() {
  // put your main code here, to run repeatedly:
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
