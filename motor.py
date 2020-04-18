# Motor class
# botOS 
from machine import PWM, Pin

class Motor():
    '''
    Motor Model
    '''
    motor_pin = 0

    # a speed value between 0 and 100
    speed = 0
    def __init__(self, motor_pin=None, speed=None):
        if motor_pin is None:
            motor_pin = 1
        if speed is None:
            speed = 0
        self.speed_pin = PWM(Pin(motor_pin))
        self.motor = Pin(motor_pin, Pin.OUT)
        
    def speed(self, value=None):
        if value is None:
            print (self.speed)
            return self.speed
        else:
            if (value >= 0) and (value <= 100):
                self.speed = value
                self.speed_pin.freq(1000)
                self.speed_pin.duty(self.speed)
    
    def on(self):
        self.motor.on()

    def off(self):
        self.motor.off()
