#ifndef SONAR_H
#define SONAR_H

#include <Arduino.h>

struct SonarSensor{
  int trigPin;
  int echoPin;
  long duration;
  int distance;
};

class Sonar {
  public:
    Sonar();

    void init(SonarSensor);

  private:
    SonarSensor _sensor[]

}
