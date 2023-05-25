  int val = 0; //Vb-Ba
  int val2 = 0; // Va 값 인식
  int val3 = 0; // Vb 값 인식
  float R1 = 10000; // Wheatstone Bridge R1 값
  float R2 = 10000; // Wheatstone Bridge R2 값
  float R3 = 10000; // Wheatstone Bridge R3 값
  float Vin = 5;  // Wheatstone Bridge input 전압값
  int Va = A0;  // A0 port
  int Vb = A1;  // A1 port
  float Vout = 0; // Vout 초기값 설정
  float voltage2 = 0; // Voltage2 초기값 설정
  float voltage3 = 0; // Voltage3 초기값 설정
  float Resistance = 0; // 상용압력센서의 저항 초기값 설정



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  val2 = analogRead(Va);  // Analog-to-Digital Conversion (ADC)
  voltage2 = (float)val2/1024*5; // 아두이노 ADC 해상도: 1024
  Serial.print(voltage2);// voltage2 값 출력
  val3 = analogRead(Vb);
  voltage3 = (float)val3/1024*5;
  Serial.print(",");
  Serial.print(voltage3);
  Vout = voltage3-voltage2;
  Serial.print(",");
  Serial.print(Vout);
  // Resistance = R3/((Vout/Vin)+(R1/(R1+R2)))-1;  // Resistance 값 계산식
  float up = R3 * (-R2/(R1+R2) + (Vout/Vin));
  float down = (- 1 + (R2/(R1+R2)) - (Vout/Vin));
  // Resistance = R1/(-Vout/Vin + R1/(R2+R3))-R1;
  Resistance = up / down;
  Serial.print(","); // Resistance 이름 출력
  Serial.println(Resistance); // Resistance 값 출력
  // (voltage2, voltage3, Vout, Resistance)
  delay(100); // 100 ms로 출력
  // v_a = analogRead(A0);
  // v_b = analogRead(A1);
  // // v_b = 100;
  // float voltage = v_a - v_b;
  // // Serial.print(v_a); Serial.print(", "); Serial.println(v_b);
  // Serial.print(v_a); Serial.print(","); Serial.print(v_b); Serial.print(",")
  // Serial.println(voltage);
  // delay(100);
}
