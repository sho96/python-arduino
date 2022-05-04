import arduinoController as controller

controller = controller.Controller("COM3")

buttonPin = 4
ledPin = 3

controller.pinMode(ledPin, "OUTPUT")
controller.pinMode(buttonPin, "INPUT")

while True:
    pinState = controller.digitalRead(buttonPin)
    controller.digitalWrite(ledPin, not pinState)
    #※cannot put more than two arduino functions into another arduino function:
    #ex: controller.digitalWrite(ledPin, controller.digitalRead(buttonPin))
