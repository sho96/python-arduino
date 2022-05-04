String inputBuffer;

String cmds[3] = {};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(500000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    char received = Serial.read();
    if(received == '\n'){
      String cmds[3] = {};
      int index = split(inputBuffer, ' ', cmds);
      if(cmds[0] == "pinMode"){
        if(cmds[2] == "OUTPUT"){
          pinMode(cmds[1].toInt(), OUTPUT);
        }
        if(cmds[2] == "INPUT"){
          pinMode(cmds[1].toInt(), INPUT);
        }
        if(cmds[2] == "INPUT_PULLUP"){
          pinMode(cmds[1].toInt(), INPUT_PULLUP);
        }
      }
      if(cmds[0] == "digitalWrite"){
        digitalWrite(cmds[1].toInt(), cmds[2] == "true");
      }
      if(cmds[0] == "analogWrite"){
        analogWrite(cmds[1].toInt(), cmds[2].toInt());
      }
      if(cmds[0] == "digitalRead"){
        if(digitalRead(cmds[1].toInt())){
          sendData("1");
        }else{
          sendData("0");
        }
      }
      if(cmds[0] == "analogRead"){
        sendData(String(analogRead(cmds[1].toInt())));
      }
      inputBuffer = "";
    }else{
      inputBuffer += received;
    }
  }
}

void sendData(String value){
  int valueSize = value.length() / sizeof(String);
  Serial.print(String(valueSize)+"a");
  Serial.print(value);
}

int split(String data, char delimiter, String *dst){
  int index = 0;
  int arraySize = (sizeof(data))/sizeof((data[0]));
  int datalength = data.length();
  
  for(int i = 0; i < datalength; i++){
    char tmp = data.charAt(i);
    if( tmp == delimiter ){
      index++;
      if( index > (arraySize - 1)) return -1;
    }
    else dst[index] += tmp;
  }
  return (index + 1);
}
