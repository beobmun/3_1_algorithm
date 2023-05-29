int input_data = 0;
unsigned long time_previous, time_current;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  time_previous = millis(); // 시작시간
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  time_current = millis();

  while (Serial.available()) {
    input_data = Serial.read();
  }
  
  if (input_data == '1') {  // 눈 감음
    time_previous = time_current;
    digitalWrite(13, LOW);
    // digitalWrite(13, HIGH);
  } 
  // else { // 눈뜨고 있는 상태
  //   digitalWrite(13, LOW);
  // }
  if (time_current - time_previous >= 15000) {
    digitalWrite(13, HIGH);
  }
  // delay(500);
}
