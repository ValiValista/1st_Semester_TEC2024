// Sumo arena = 45cm of radius


// pin definition variables

const int IR_sensor_1_pin = 3;  
const int IR_sensor_2_pin = 4;  

//This is a for a HC_05 bluetooth module ignore
// const int HC_05_EN_pin = 5;
// const int HC_05_TXD_pin = 6;
// const int HC_05_RXD_pin = 7;
// const int HC_05_STATE_pin = 8;

const int UltraSonic_1_ECHO_pin = 9;
const int UltraSonic_1_TRIGGER_pin = 10;

const int H_Bridge_IN1 = 11;
const int H_Bridge_IN2 = 12;
const int H_Bridge_IN3 = 13;
const int H_Bridge_IN4 = 14;


// Definition comments
      // Definition of IR_sensor_1(Left), pin 3 (INPUT)
      // Definition of IR_sensor_2(Right), pin 4 (INPUT)

      // Definition of HC-05
      // D5 = EN(Orange)[Output]
      // D6 = TXD(Blue)[Input]
      // D7 = RXD(Purple)[Output]
      // D8, State(Gray)[Input]

      // Definition of Ultrasonic
      // D9 = Echo (Input)
      // D10 = Trigger (Output)

      // H_Bridge 
      // D11 = IN1 (Orange)
      // D12 = IN2 (Yellow)
      // D13 = IN3 (Green)
      // A1 = IN4 (Blue)


// void built_in_led(){
//   const int time_var = 75;
//   digitalWrite(13, HIGH);
//   delay(time_var);
//   digitalWrite(13, LOW);
//   delay(time_var);
// }

// For the HC_05
// char read_input(){
//   if (Serial.available() > 0) {
//     char instruction_movement;
//     instruction_movement = Serial.read();
//     Serial.println(instruction_movement);
//     return instruction_movement;
//   }
// }

int ultra1() {
  const int delay_ultrasonics_ms = 10;
  const int delay_ultrasonics_us = 10;
  long trigger_1_US;
  int  distance_1_US;
  digitalWrite(UltraSonic_1_TRIGGER_pin, HIGH);
  delayMicroseconds(delay_ultrasonics_us);
  digitalWrite(UltraSonic_1_TRIGGER_pin, LOW);

  trigger_1_US = pulseIn(UltraSonic_1_ECHO_pin, HIGH);
  distance_1_US = trigger_1_US / 59;  //distancia en centimetros
  //Serial.print("Distancia: ");
  //Serial.print(distance_1_US);
  //Serial.println(" cm");
  delay(delay_ultrasonics_ms);
  return distance_1_US;
}


void movement_stop(){
  digitalWrite(H_Bridge_IN1, LOW); //Motor 1 low on side 1
  digitalWrite(H_Bridge_IN2, LOW); //Motor 1 low on side 2

  digitalWrite(H_Bridge_IN3, LOW); //Motor 2 low on side 1
  digitalWrite(H_Bridge_IN4, LOW); //Motor 2 low on side 2

  Serial.println("Stopped");
}
void adelante(){
  digitalWrite(H_Bridge_IN1, LOW); //Motor 1 low on side 1
  digitalWrite(H_Bridge_IN2, HIGH); //Motor 1 high on side 2

  digitalWrite(H_Bridge_IN3, LOW); //Motor 2 low on side 1
  digitalWrite(H_Bridge_IN4, HIGH); //Motor 2 high on side 2

  //Serial.println("Adelante");
}
void atras(){
  digitalWrite(H_Bridge_IN1, LOW); //Motor 1 low on side 1
  digitalWrite(H_Bridge_IN2, HIGH); //Motor 1 high on side 2

  digitalWrite(H_Bridge_IN3, LOW); //Motor 2 low on side 1
  digitalWrite(H_Bridge_IN4, HIGH); //Motor 2 low on side 2

  //Serial.println("Atras");
}
void gira_izquierda(){
  digitalWrite(H_Bridge_IN1, LOW); //Motor 1 low on side 1
  digitalWrite(H_Bridge_IN2, HIGH); //Motor 1 high on side 2

  digitalWrite(H_Bridge_IN3, HIGH); //Motor 2 low on side 1
  digitalWrite(H_Bridge_IN4, LOW); //Motor 2 low on side 2

  //Serial.println("Izquierda");

}
void gira_derecha(){
  digitalWrite(H_Bridge_IN1, HIGH); //Motor 1 low on side 1
  digitalWrite(H_Bridge_IN2, LOW); //Motor 1 low on side 2

  digitalWrite(H_Bridge_IN3, LOW); //Motor 2 low on side 1
  digitalWrite(H_Bridge_IN4, HIGH); //Motor 2 high on side 2

  //Serial.println("Derecha");
}

// void motors_manual(char instruction_movement){
//   if(instruction_movement == 'w') //fowards
//   {
//     adelante();
//   }

//     else if(instruction_movement == 's') //backwards
//     {
//       atras();
//     }

//     else if(instruction_movement == 'd') //right
//     {
//       gira_derecha();
//     }

//     else if (instruction_movement == 'a') //left
//     {
//       gira_izquierda();
//     }
//     else{
//       movement_stop();
//     }

// }

// void motors_delay(){
//   const int motors_time = 500;
//   char instruction_movement = read_input();
//   motors_manual(instruction_movement);
//   delay(motors_time);

// }

void main_logic(){

  bool edge_state = digitalRead(IR_sensor_1_pin);
  Serial.println(edge_state);

  //sensor logic
  if ((ultra1() < 30) && edge_state){
    adelante();
    Serial.println("Attack");
  }

  else if ((ultra1() >=30) && edge_state){
    gira_izquierda();
    delay(100);
    gira_derecha();
    delay(100);
    Serial.println("Searching");
  }

  else if (!edge_state){
    delay(750);
    gira_izquierda();   
    adelante();
    Serial.println("On edge");
  }


}

void setup() {
  // PinMode Definitions
  pinMode(13, OUTPUT);
  pinMode(IR_sensor_1_pin, INPUT);
  pinMode(IR_sensor_2_pin, INPUT);
  // pinMode(HC_05_EN_pin, OUTPUT);
  // pinMode(HC_05_TXD_pin, INPUT);
  // pinMode(HC_05_RXD_pin, OUTPUT);
  // pinMode(HC_05_STATE_pin, INPUT);
  pinMode(UltraSonic_1_ECHO_pin, INPUT);
  pinMode(UltraSonic_1_TRIGGER_pin, OUTPUT);
  pinMode(H_Bridge_IN1, OUTPUT);
  pinMode(H_Bridge_IN2, OUTPUT);
  pinMode(H_Bridge_IN3, OUTPUT);
  pinMode(H_Bridge_IN4, OUTPUT);


  //Initiate serial at BAUD 9600
  Serial.begin(9600);


}

void loop() {
  // led upload confirm function
  //built_in_led();

  //Read input function
  //read_input(); //uncomment to call

  //ultrasonic 1 function call
  //ultra1(); //uncomment to call


  //IR sensors function 
  //sensors(); //uncomment to call

  //Motors delay function only useful for debugging
  //motors_delay(); //uncomment to call

  //Do not call the motors function directly

  //Main function, this one does all the logic and processes for sumo fights
  //delay(5000); //Startup delay, uncomment when not debugging
  main_logic(); //uncomment to call
}
