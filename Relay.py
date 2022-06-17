import RPi.GPIO as GPIO
import Adafruit_DHT as ad


class Relay ():
    def __init__(self,pin):
        self.pin=pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)  # start OF
    
    def start(self):
        GPIO.output(self.pin,GPIO.LOW)
        return(self)
    
    def stop(self):
        GPIO.output(self.pin,GPIO.HIGH)
        return(self)

    def cleanup(self):
        GPIO.cleanup()

if __name__ == '__main__':
    relay=Relay(4)
    print ("debugging line")
    relay.start()
    relay.stop()
    GPIO.cleanup()

