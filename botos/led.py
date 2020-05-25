# led class
# botOS 
from .machine import PWM, Pin

class LED():

    # expressed as a percentage
    brightness = 100 
    pin = 15

    def __init__(self, pin=None, value=None):
        '''
            default pin is 15
        '''
        if pin is None:
            pin = 15
        self.p = PWM(Pin(pin))
        self.p.freq(1000)
        if value is None:
            value = 100
        # check value is between 0 and 100
        if (value <= 100) and (value >= 0):
            self.brightness = value * 10
            self.p.duty(self.brightness)
        else:
            print("Brightness is either less than 0 or higher than 100, please use a percentage")

    def dim(self):
        if pin is None:
            pin = 15
        p = PWM(Pin(pin))
        p.freq(1000)
        p.duty(500)
       
        
    def bright(self):
        if pin is None:
            pin = 15
        p = PWM(Pin(pin))
        p.freq(1000)
        p.duty(1000)

    def set_brightness(self, value):
        # check value is between 0 and 100
        if (value <= 100) and (value >= 0):
            self.brightness = value * 10
            self.p.duty(self.brightness)
        else:
            print("Brightness is either less than 0 or higher than 100, please use a percentage")        
        
    def on(self):
        self.set_brightness(100)

    def off(self):
        self.set_brightness(0)

    def is_on(self):
        if self.brightness > 0:
            return True
        else:
            return False    

    def is_off(self):
        if self.brightness == 0:
            return True
        else: 
            return False

    def level(self):
        return self.brightness 
