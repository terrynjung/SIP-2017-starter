void setup() {
  pinMode(13, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(6,OUTPUT);
}

int pin [] = {6, 9, 13};
int dely [] = {100, 200, 300};

void loop() {
  int s;
  int p;

for (s = 0, p = 0; s < 3, p < 3; s ++, p ++) {
    digitalWrite(pin[s], HIGH);
    delay(dely[p]);
    digitalWrite(pin[s], LOW);
    delay(dely[p]);
//    digitalWrite(pin[1], LOW);
//    dely[1];
//    digitalWrite(pin[1], HIGH);
//    dely[1];
//     digitalWrite(pin[0], LOW);
 //   dely[2];
  //  digitalWrite(pin[0], HIGH);
  //  dely[2];
}
}
