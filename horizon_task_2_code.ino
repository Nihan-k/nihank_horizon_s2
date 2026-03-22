#include <Servo.h>
Servo s1;

//pin labels;
int servopin = 10;
int ledpin = 13;
int potpin = A0;

// pin setup;
void setup() {
  s1.attach(servopin);
  pinMode(ledpin,OUTPUT);
}


void loop() {
  // reading input from potentiometer
  int reading = analogRead(potpin);
  // converting to potentiometer angle
  int p_angle = map(reading,0,1023,0,180);
  // declaring servo motor angle
  int s_angle = 0;
  if (p_angle >= 68) {
    s_angle = 68;
    // LED ON
    digitalWrite(ledpin,HIGH);
  }
  else {
    s_angle = p_angle;
    // LED OFF
    digitalWrite(ledpin,LOW);
  }
  s1.write(s_angle);
  delay(100);
}
