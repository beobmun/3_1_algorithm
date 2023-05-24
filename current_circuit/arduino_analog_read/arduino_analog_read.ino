float v_a; // analog_A0 input
float v_b;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  v_a = analogRead(A0);
  v_b = analogRead(A1);
  // v_b = 100;
  float voltage = v_a - v_b;
  // Serial.print(v_a); Serial.print(", "); Serial.println(v_b);
  Serial.println(voltage);
  delay(100);
}
