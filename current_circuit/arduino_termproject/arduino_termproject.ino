#include "DHT.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);

int input_data = 0;
unsigned long time_previous, time_current;

int light = A0;
int lightValue;
int lightState = LOW;

// 미세먼지 센서 관련
unsigned long pulse = 0;
float ugm3 = 0;
float pulse2ugm3(unsigned long pulse) {
  float value = (pulse - 1400) / 14.0;
  if (value > 300) {
    value = 0;
  }
  return (value);
}

//습도센서
DHT dht(9, DHT11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  time_previous = millis(); // 시작시간
  pinMode(13, OUTPUT);  // 조명 릴레이
  pinMode(12, INPUT_PULLUP);  //조명 OFF 스위치
  pinMode(11, INPUT);   // 미세먼지 센서
  pinMode(7, OUTPUT);   // 눈깜빢임 LED

  pinMode(6, INPUT);    //초음파 ECHO
  pinMode(5, OUTPUT);   //초음파 TRIG
  pinMode(4, OUTPUT);   //수동부저

  pinMode(2, OUTPUT);   //가습기모듈

  dht.begin();    //습도센서 시작

  lcd.init();
  lcd.backlight();
  lcd.print("Hello, world!");
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

  time_current = millis();

  while (Serial.available()) {
    input_data = Serial.read();
  }
  
  lightValue = analogRead(light); // 광조도센서 
  // delay(1000);
  // Serial.print("light: ");
  // Serial.println(lightValue);

  // 어두어지면 조명 on
  if (lightValue > 500) {
    lightState = HIGH;
    digitalWrite(13, lightState);
  }
  if (lightState == HIGH && digitalRead(12) == LOW) {  // 버튼 누르면 조명 OFF
    lightState = LOW;
    digitalWrite(13, lightState);
  }

  if (input_data == '1') {  // 눈 감음
    time_previous = time_current;
    digitalWrite(7, LOW);     //LED OFF
    // digitalWrite(13, HIGH);
  } 

  if (time_current - time_previous >= 5000) { // 5초 이상 눈 안감빡이면 LED on
    digitalWrite(7, HIGH);
  }
  if (time_current - time_previous >= 10000) {  // 10초 이상 눈 안깜빡이면 LED 깜빡깜빡
    delay(200);
    digitalWrite(7, LOW);
    delay(200);
  }


  // 미세먼지 센서
  pulse = pulseIn(11, LOW, 20000);
  ugm3 = pulse2ugm3(pulse);
  // Serial.print(ugm3, 4);
  // Serial.println("  g/m3");

  //습도센서 관련
  float humidity = dht.readHumidity();
  if (isnan(humidity)) {
    Serial.println("습도 인식 실패");
  }
  // Serial.print((int)humidity);
  // Serial.println("%");

  //가습기모듈
  // if ((int)humidity < 65) {
  //   digitalWrite(2, HIGH);
  // } else {
  //   digitalWrite(2, LOW);
  // }
  digitalWrite(2, HIGH);


  //LCD
  lcd.setCursor(0,0); //첫번째줄 미세먼지 농도
  lcd.print("dust: ");
  lcd.print(ugm3, 2);
  lcd.print(" g/m3 ");
  lcd.setCursor(0,1); //두번째줄 현재 습도
  lcd.print("humidity: ");
  lcd.print((int)humidity);
  lcd.print(" %");

  //초음파 센서
  long duration, distance;
  digitalWrite(5, LOW);   //TRIG
  delayMicroseconds(2);
  digitalWrite(5, HIGH);
  delayMicroseconds(10);
  digitalWrite(5, LOW);
  duration = pulseIn(6, HIGH); //반사돼서 돌아오는 시간
  distance = duration * 17 / 1000; 
  // Serial.print("distance(cm): ");
  // Serial.println(distance);

  //부저
  if (distance < 40) {
    tone(4, 60);
  } else {
    noTone(4);
  }

}
