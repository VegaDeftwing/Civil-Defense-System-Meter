// pins for the LEDs:
const int redPin = 11;
const int greenPin = 10;
const int bluePin = 9;
const int yellowPin = 6;
const int radPin = 3;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(radPin, OUTPUT);

}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {

    // look for the next valid integer in the incoming serial stream:
    int outPin = Serial.parseInt();
    int outVal = Serial.parseInt();

    // look for the newline. That's the end of your sentence:
    if (Serial.read() == '\n') {

      // fade the red, green, and blue legs of the LED:
      if(outPin == 1){
        analogWrite(redPin, outVal);
      }
      
      if (outPin == 2){
        analogWrite(greenPin, outVal);
      }
      if (outPin == 3) {
        analogWrite(bluePin, outVal);
      }
      
      if (outPin == 4) {
        analogWrite(yellowPin, outVal);
      }
      
      if (outPin == 5) {
        analogWrite(radPin, outVal);
      }
    }
  }
}
