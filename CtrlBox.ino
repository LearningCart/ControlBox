/* Arduino code for the control box */

int Pins[] = {4, 5, 6, 7 };
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  for(int i = 0; i < 4; i++)
  {
    pinMode(Pins[i],OUTPUT);
    /* Some relays are reverse */
    digitalWrite(Pins[i],HIGH);
  }
}

String Cmd;


// the loop routine runs over and over again forever:
void loop() {
  char Command[4];
  Serial.print("ctrlbox@com # ");

  while (Serial.available() == 0)
  {
    delayMicroseconds(1000);
  }
  Cmd = Serial.readString();
  if(Cmd.length() > 0)
  {
    Serial.println(Cmd);
    Cmd.toCharArray(Command, 4);
    if((Command[0] >= '1' && Command[0] <= '4') && (Command[2] == '0' || Command[2] == '1'))
    {
      /* Relay board is reverse */
      digitalWrite(Pins[Command[0] - '1'] , Command[2] == '1' ? LOW : HIGH);
    }else if (Command[0] == 'a' || Command[0] == 'A' )
    {
      int state;
      state = Command[2] == '1' ? LOW : HIGH;
      for(int i = 0; i < 4; i++)
      {
        digitalWrite(Pins[i] , state);
      }
    }
  }
}

