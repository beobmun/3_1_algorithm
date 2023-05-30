#include "DHT.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

Servo servo;

LiquidCrystal_I2C lcd(0x27,16,2);

int input_data = 0;   // 파인썬에서 오는 눈깜빡임 신호
unsigned long time_previous, time_current;  // 시간체크

int light = A0;   // 광조도 센서 포트
int lightValue;   // 광조도 센서 값
int lightState = LOW; //현재 전구(릴레이) 상태

int humState = 0; //현재 가습기 상태


// 미세먼지 센서 관련
unsigned long pulse = 0;
float ugm3 = 0;           //미세먼지 농도
float pulse2ugm3(unsigned long pulse) {   //pulse 신호를 미세먼지 농도로 계산하는 함수
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

  servo.attach(2);  //서보 모터
  // pinMode(2, OUTPUT);   //가습기모듈

  dht.begin();    //습도센서 시작

  //lcd 초기세팅
  lcd.init();
  lcd.backlight();
  lcd.print("Hello, world!");
  delay(1000);

  //서보모터 세팅
  servo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:

  time_current = millis();  //현재 시간 

  while (Serial.available()) {    
    input_data = Serial.read();   // 파이썬에서 보낸 눈깜빡임신호 저장
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
  } 

  if (time_current - time_previous >= 5000) { // 5초 이상 눈 안 깜빡이면 LED on
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

  //서보 모터
  if ((int)humidity <= 50 && humState == 0) {  //습도 50이하 and 가습기 작동안할 때 
    humState = 1;                             //서보모터 작동으로 가습기 버튼 누르기
    servo.write(60);
    delay(250);
    servo.write(90);
  } else if ((int)humidity > 55 && humState == 1) { //습도 55 초과 and 가습기 작동 중이면
    humState = 0;                                   //서보모터로 가습기버튼눌러서 작동 멈춤
    servo.write(60);                                // 두번 눌러야 종료
    delay(250);
    servo.write(90);
    delay(250);
    servo.write(60);
    delay(250);
    servo.write(90);
  }

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
  distance = duration * 17 / 1000; //시간을 거리로 환산(cm 단위로 저장)
  // Serial.print("distance(cm): ");
  // Serial.println(distance);

  //부저
  if (distance < 40) {  //거리가 40cm미만이면 부저울림
    tone(4, 60);
  } else {
    noTone(4);
  }

}
