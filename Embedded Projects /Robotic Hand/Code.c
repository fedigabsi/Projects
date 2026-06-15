#include<Servo.h>
int s0,s1,s2,s3,s4;
int m0,m1,m2,m3,m4;
Servo x0,x1,x2,x3,x4;
void setup() 
{
x0.attach(3);
x1.attach(5);
x2.attach(6);
x3.attach(9);
x4.attach(10);
  
Serial.begin(9600);
  
pinMode(3 , OUTPUT);
pinMode(5 , OUTPUT);
pinMode(6 , OUTPUT);
pinMode(9 , OUTPUT);
pinMode(10 , OUTPUT);
  
}

void loop() 
{
  
s0 = analogRead(A0);
m0 = map(s0 ,256 , 59 , 0 , 255);
x0.write(m0);

delay(500);
  
s1 = analogRead(A1);
m1 = map(s1 ,256 , 59 , 0 , 255);
x1.write(m1);

delay(500);
  
s2 = analogRead(A2);
m2 = map(s2 ,256 , 59 , 0 , 255);
x2.write(m2);

delay(500);
  
s3 = analogRead(A3);
m3 = map(s3 ,256 , 59 , 0 , 255);
x3.write(m3);

delay(500);
  
s4 = analogRead(A4);
m4 = map(s4 ,256 , 59 , 0 , 255);
x4.write(m4);

delay(500);
   
}
