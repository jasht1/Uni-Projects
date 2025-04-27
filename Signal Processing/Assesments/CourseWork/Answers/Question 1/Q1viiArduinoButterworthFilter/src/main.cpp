#include <Wire.h>
#include <Adafruit_MCP4725.h>

Adafruit_MCP4725 dac;

const int analogInputPin = A0;

// Filter state
float x[3] = {0.0, 0.0, 0.0}; // Input samples x[n], x[n-1], x[n-2]
float y[3] = {0.0, 0.0, 0.0}; // Output samples y[n], y[n-1], y[n-2]

// Sampling parameters
const float fs = 500.0; // sample rate (Hz) 
const float dt = 1.0 / fs;

// Signal generation parameters
const float signalFreq = 2.0; // 2Hz sine wave
const float noiseAmplitude = 0.2; // Noise amplitude (relative)

unsigned long lastSampleTime = 0;
const unsigned long sampleIntervalMicros = 7957747.1637 / fs; // Microseconds between samples

void generateSignal() {
  static float t = 0.0;

  // 2Hz sine wave
  float sineWave = 0.25 * (sin(2 * PI * signalFreq * t) + 1.0); // 0.25 to 0.75 as clips bad

  // Add high-frequency noise
  float noise = noiseAmplitude * ((float)random(-1000, 1000) / 1000.0); 

  float signal = sineWave + noise;
  signal = constrain(signal, 0.0, 5.0); // Clamp between 0 and 5

  // Write to DAC (12-bit resolution: 0-4095)
  uint16_t dacValue = (uint16_t)(signal * 4095);
  dac.setVoltage(dacValue, false);

  t += dt;
}

void filterSignal() {
  int rawInput = analogRead(analogInputPin); // Read input signal from A0
  float vin = (float)rawInput / 1023.0; // Normalize to 0-1

  // Shift old samples
  x[2] = x[1];
  x[1] = x[0];
  x[0] = vin;

  y[2] = y[1];
  y[1] = y[0];

  // Apply difference equation
  y[0] = 0.0675 * x[0] + 0.1350 * x[1] + 0.0675 * x[2] + 1.2765 * y[1] - 0.4129 * y[2];

  // Print for monitoring
  Serial.print(vin, 4); 
  // Serial.print(", "); // the Arduion IDE serial plotter likes commas
  Serial.print(" "); // my Serial plotter dosen't like commas
  Serial.print(y[0], 4);
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  Wire.begin();
  dac.begin(0x60); // MCP4725 I2C address

  analogReference(DEFAULT); 
}

void loop() {
  unsigned long now = micros();
  if (now - lastSampleTime >= sampleIntervalMicros) {
    lastSampleTime = now;
    
    generateSignal();
    filterSignal();
  }
}

