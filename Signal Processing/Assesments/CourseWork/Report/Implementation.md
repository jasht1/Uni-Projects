
To test the difference equation derived in the previous section based on the Butterworth filter it was used onboard an Arduino Nano to filter an incoming analogue signal with high noise content.

The firmware uses two synchronous functions. The first generated the noisy signal using a MCP4725 digital to analogue converter (DAC). The signal being a 2 Hz sinusoid ranging from $0.25 - 0.75 \text{V}$ disturbed by random noise of $\pm 0.2 \text{V}$. 

```cpp title="Noisy Signal Function"
void generateSignal() {
  static float t = 0.0;

  // 2Hz sine wave
  // float sineWave = 0.5 * (sin(2 * PI * signalFreq * t) + 2.5); // 1.5 to 3.5 as can't do -ve V
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
```

This noisy signal is returned to the Nano at pin `A0` where the second function sampled it at $\approx 8 \text{Hz}$ and used the difference equation to filter the incoming data. The sampling rate was based on a the cut off frequency $\omega_{b} = 5 \frac{\text{rad}}{\text{sec}}$ times $10$. 

```cpp title="Signal Filtering Function"
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
  y[0] = 0.0675 * x[0] + 0.1350 * x[1] + 0.0675 * x[2]
         + 1.2765 * y[1] - 0.4129 * y[2];

  // Print for monitoring
  Serial.print(vin, 4); 
  // Serial.print(", "); // the Arduion IDE serial plotter likes commas
  Serial.print(" "); // However, my Serial plotter dosen't like commas
  Serial.print(y[0], 4);
  Serial.println();
}
```

The main body of the script can be found [here on the git repo](https://github.com/jasht1/Uni-Projects/blob/master/Signal%20Processing/Assesments/CourseWork/Answers/Question%201/Q1viiArduinoButterworthFilter/src/main.cpp) allong with it's platformIO `.ini` build config and can be read in the snippet below.

```cpp title="main.cpp"
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
	// See Def "Noisy Signal Function" Above
}

void filterSignal() {
	// See Def "Signal Filtering Function" Above
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
```

The traces from which can be seen in the following 2 plots. The first has both traces on the main axis (left) for consistency, the second has the "Filtered" trace on axis 2 (right) scaled and translated to match "Analogue In" to more easily compare noise.

###### Figure 8: Arduino Butterworth Filter Traces
![Arduino Butterworth Filter Traces](Arduino%20Butterworth%20Filter%20Traces.png)

Serial Plots where generated using [nathandunk's BetterSerialPlotter](https://github.com/nathandunk/BetterSerialPlotter).