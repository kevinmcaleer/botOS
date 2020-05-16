# Motor class
# botOS 
from machine import PWM, Pin
from time import sleep

class Motor():
    '''
    Motor Model
    '''
    motor_pin = 0
    motor_direction_pin = 0

    # a speed value between 0 and 100
    motor_speed = 0
    motor_direct = 0    
    def __init__(self, motor_pin=None, speed=None):
        if motor_pin is None:
            motor_pin = 1
        if speed is None:
            speed = 0
        self.speed_pin = PWM(Pin(motor_pin))
        self.motor = Pin(motor_pin, Pin.OUT)
                
    def speed(self, value=None):
        if value is None:
            print (self.motor_speed)
            return self.motor_speed
        else:
            if (value >= 0) and (value <= 100):
                self.motor_speed = value
                self.speed_pin.freq(1000)
                self.speed_pin.duty(self.motor_speed)
    
    def on(self):
        self.motor.on()
        print('Motor On')
        print('Motor Speed = ', self.motor_speed)
        print('Motor Pin = ', self.motor_pin)

    def off(self):
        self.motor.off()
        print('Motor Off')

    def forward(self):
        self.motor.value(1)
        sleep(0.5)
        self.motor.value(0)
    
    def backwards(self):
        self.motor.value(0)
        sleep(0.5)
        self.motor.value(1)