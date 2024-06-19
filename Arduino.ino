// Arduino code written by:
// Pascal Sikorski
// Leendert Schrader

// Motor setup
int STBY = 3;
int ENA=5; 
int ENB=6; 
int IN1=7; 
int IN2=8; 
int IN3=9; 
int IN4=11; 

// Ultrasonic Sensor stop distance
int sensorStopDist = 35;

// Ultrasonic Sensor Constants
int TrigPin = 13;
int EchoPin = 12;
int dt = 50;
// The number of readings to smooth
const int windowSize = 5; 
int distanceReadings[windowSize];
int readIndex = 0;
long total = 0;
float average = 0;

void setup() {
  //Initialize 9600 baud rate
  Serial.begin(9600);
  //Setting up all motor control pins
  pinMode(ENA,OUTPUT); 
  pinMode(ENB,OUTPUT); 
  pinMode(IN1,OUTPUT); 
  pinMode(IN2,OUTPUT); 
  pinMode(IN3,OUTPUT); 
  pinMode(IN4,OUTPUT); 
  pinMode(STBY, OUTPUT);
  
  // not max speed
  analogWrite(ENA,125); 
  analogWrite(ENB,125); 
  digitalWrite(STBY, LOW);

  //Ultrasonic Sensor initialization
  pinMode(TrigPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  digitalWrite(TrigPin, LOW);
  for (int i = 0; i < windowSize; i++) {
    distanceReadings[i] = 0;
  }
}

//Sends ultrasonic sensor pulse
void pulse(){
  digitalWrite(TrigPin, LOW);
  delayMicroseconds(20);
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin, LOW);
}

// Forward function with distance and speed
void forward(unsigned long userDistance, float speed){
  digitalWrite(STBY, HIGH);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);

  // calculate PWM for motor
  float PWM = (-0.0264*(speed*speed)) + (5.4266*speed) - 35.889;
  analogWrite(ENA,PWM);
  analogWrite(ENB,PWM);

  // Calculate how long motor should run for
  unsigned long trueDelay = (userDistance/speed) * 1000;
  unsigned long endTime = trueDelay + millis();

  // loop checking time and sensor distance
  while(millis() < endTime) {
    if (ThresholdCheck(sensorStopDist) == 0) {
      break;
    }
    delay(30);
  }
  stop();
}

// Backward function with distance and speed
// See forward() comments for code logic
void backward(float userDistance, float speed){
  digitalWrite(STBY, HIGH);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  float PWM = (-0.0264*(speed*speed)) + (5.4266*speed) - 35.889;
  analogWrite(ENA,PWM);
  analogWrite(ENB,PWM);

  float trueDelay = (userDistance/speed)*1000;
  Serial.println(trueDelay);
  delay(trueDelay);
  stop();
  delay(10);
}

// Left function with angle (degrees) and speed
// Same approach as forward, though not accounting for sensor threshold
void left(float userAngle, float angularSpeed){
  digitalWrite(STBY, HIGH);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  float PWM = (0.001*(angularSpeed*angularSpeed)) + (0.095 * angularSpeed) + 92.3;

  analogWrite(ENA, PWM);
  analogWrite(ENB, PWM);

  //Applying kinematics to relate change in angle versus delay time
  float trueDelay = (userAngle/angularSpeed)*1000;
  delay(trueDelay);

  //Stops motor function after reaching inputted angle
  stop();
  delay(10);
}

// Right function with angle (degrees) and speed
void right(float userAngle, float angularSpeed){
  digitalWrite(STBY, HIGH);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  float PWM = (0.001*(angularSpeed*angularSpeed)) + (0.095 * angularSpeed) + 92.3;
  analogWrite(ENA, PWM);
  analogWrite(ENB, PWM);

  float trueDelay = (userAngle/angularSpeed)*1000;

  delay(trueDelay);
  stop();
  delay(10);
}

// stop all motors function
void stop(){
  digitalWrite(STBY, LOW);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

// Check sensor to see if within threshold
bool ThresholdCheck(int stopDistance){
  pulse();
  int duration = pulseIn(EchoPin, HIGH);
  delay(5);
  int distance = duration/(29.1*2.0);
  float calibratedDis = distance*(0.976) + 0.356;
  /*
  total = total - distanceReadings[readIndex];
  distanceReadings[readIndex] = calibratedDis;
  total = total + distanceReadings[readIndex];
  readIndex = (readIndex + 1) % windowSize;
  average = (float)total / windowSize;
  */
  Serial.println(calibratedDis);
  if((calibratedDis >= 0) && (calibratedDis <= stopDistance)){
    return(0);
  } else {
    return(1);
  }
  delay(dt);
}

// forward motor control
void IndForward(){
  digitalWrite(STBY, HIGH);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  delay(10);
}

// Indefinite moving (with checks)
// If back, do right 180 and move forward
void IndefiniteMovement(String direction){
  if(direction == "f"){
    if(ThresholdCheck(sensorStopDist)){
      stop();
      delay(10);
      IndForward();
      while(1){
        delay(50);
        if(ThresholdCheck(sensorStopDist) == 0){
          stop();
          break;
        }
      }
    }
  } else if (direction == "b") {
    right(180, 141);
    if(ThresholdCheck(sensorStopDist)){
      stop();
      delay(10);
      IndForward();
      while(1){
        delay(50);
        if(ThresholdCheck(sensorStopDist) == 0){
          stop();
          break;
        }
      }
    }
  }
}


// Precise movement function given direction and distance to travel
void PreciseMovement(String direction, String distance){
  if(direction == "f"){
    stop();
    delay(10);
    unsigned long distanceVal = (unsigned long)distance.toInt();
    forward(distanceVal, 35);
    delay(10);
  }
  else if(direction == "b"){
    stop();
    delay(10);
    float distanceVal = (float)distance.toInt();
    backward(distanceVal, 35);
    delay(10);
  }
  else if(direction == "l"){
    stop();
    delay(10);
    float angleVal = (float)distance.toInt();
    left(angleVal, 141);
    delay(10);
  }
  else if(direction == "r"){
    stop();
    delay(10);
    float angleVal = (float)distance.toInt();
    right(angleVal, 141);
    delay(10);
  }
  else if(direction == "s"){
    stop();
    delay(1000);
  }
}

void loop() {
  // Read the input string until newline character
  String inputString = Serial.readStringUntil('\n');
  Serial.println(inputString);

  int startPos = 0;
  int endPos;

  // Split commands into array
  do {
    endPos = inputString.indexOf('/', startPos);
    String token = inputString.substring(startPos, (endPos == -1 ? inputString.length() : endPos));

    int commaCheck = token.indexOf(',');
    if(commaCheck != -1){
      String direction = token.substring(0, commaCheck);
      String distance = token.substring(commaCheck + 1);
      if (direction == "t") {
        sensorStopDist = distance.toInt();
      } else {
        PreciseMovement(direction, distance);
      }
    }

    else if(commaCheck == -1){
      if (token == "r") {
        PreciseMovement("r", "90");
      } else if (token == "l") {
        PreciseMovement("l", "90");
      } else {
        IndefiniteMovement(token);
      }
    }

    startPos = endPos + 1;
  } while (endPos != -1);
}
