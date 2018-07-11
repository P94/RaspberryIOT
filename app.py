from gpiozero import LED
from time import sleep
from pycnic.core import WSGI, Handler
from pycnic.errors import HTTP_400

class piLight(Handler):
    def get(self):
        led = LED(25)

        while True:
            led.on()
            sleep(1)
            led.off()
            sleep(1)
        
        return { 
            "response": "OK"
        }

class app(WSGI):
    routes = [('/pi/light', piLight())]