import arduinoController as arduino

#windows
controller = arduino.Controller("COM5") #/dev/tty/... for linux/mac

buttonPin = 4
ledPin = 3

controller.pinMode(ledPin, "OUTPUT")
controller.pinMode(buttonPin, "INPUT") #INPUT_PULLUP can also be used

while True:
    pinState = controller.digitalRead(buttonPin)
    controller.digitalWrite(ledPin, not pinState)
    #※cannot put more than two arduino functions into another arduino function:
    #ex: controller.digitalWrite(ledPin, controller.digitalRead(buttonPin))
