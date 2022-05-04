import serial
import time

class Controller:
    pinmodes = ["OUTPUT", "INPUT", "INPUT_PULLUP"]
    def __init__(self, portid, baud = 500000, waitTime = 5):
        print("connecting...")
        self.ser = serial.Serial(portid, baudrate = baud, timeout = 1)
        #self.ser.open()
        time.sleep(waitTime)
        print("connection established")
    def __del__(self):
        self.ser.close()
    def readValue(self):
        datasize = b""
        while True:
            byte = self.ser.read()
            #print(byte)
            if byte == b"a":
                datasize = int(datasize.decode("ascii"))
                break
            else:
                datasize += byte
        return self.ser.read(size = datasize)
    def pinMode(self, pin, mode):
        if not mode in self.pinmodes:
            self.ser.close()
            raise ValueError(f"pin mode named: {mode} is not supported\nuse one of {pinmodes}")
        self.ser.write(f"pinMode {pin} {mode}\n".encode("ascii"))
    def digitalWrite(self, pin, state):
        if not isinstance(state, bool):
            self.ser.close()
            raise ValueError("state only supports boolean values")
        if state:
            state = "true"
        else:
            state = "false"
        self.ser.write(f"digitalWrite {pin} {state}\n".encode("ascii"))
    def analogWrite(self, pin, value):
        if not isinstance(value, int):
            self.ser.close()
            raise ValueError("value only supports integer values")
        self.ser.write(f"analogWrite {pin} {value}\n".encode("ascii"))
    def digitalRead(self, pin):
        self.ser.write(f"digitalRead {pin}\n".encode("ascii"))
        return bool(int(self.readValue().decode("ascii")))
    def analogRead(self, pin):
        self.ser.write(f"analogRead {pin}\n".encode("ascii"))
        return int(self.readValue())
    def close(self):
        self.ser.close()
    
