// // define pins numbers
// const int trigPin = 4;
// const int echoPin = 5;
//
// // define variables
// long duration;
// int distance;
// void setup() {
//   pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
//   pinMode(echoPin, INPUT); // Sets the echoPin as an Input
//   Serial.begin(9600); // Starts the serial communication
// }
// void loop() {
//   // Clear the trigPin
//   digitalWrite(trigPin, LOW);
//   delayMicroseconds(2);
//   // Set the trigPin on HIGH state for 10 micro seconds
//   digitalWrite(trigPin, HIGH);
//   delayMicroseconds(10);
//   digitalWrite(trigPin, LOW);
//   // Read the echoPin, returns the sound wave travel time in microseconds
//   duration = pulseIn(echoPin, HIGH);
//   // Calculate the distance
//   distance = duration * 0.034 / 2;
//   // Print the distance on the Serial Monitor
//   Serial.print("Distance: ");
//   Serial.println(distance);
// }
