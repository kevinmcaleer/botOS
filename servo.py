# servo class
# botOS 
# import machine

class Servo():
    '''
        Models a physical servo 
    '''

    angle = 90
    name = "my servo"
    pin = 1 # the GPIO pin used to control this servo

    def __init__(self, name=None, angle=None, pin=None):
        '''
        constructure for Servo class
        '''

        # self.p12 = machine.Pin(12)

        if name is None:
            self.name = "My Servo"
        else:
            self.name = name
        if angle is None:
            # set the default angle to 90 degrees
            self.angle = 90 
        else:
            self.angle = angle
        if pin is None:
            self.pin = 1
        else: 
            self.pin = pin

    def angle(self, angle_a=None):
        '''
        set the angle of the 
        '''
        if angle_a is None:
            print("Angle value is missing")
        else:
            if (angle_a <= 180) and (angle_a >= 0):
                self.angle = angle_a
                # self.pwm12 = machine.PWM(p12)
                # self.pwm12.freq(500)
                # self.pwm12.duty(512)

            else:
                print("that angle is either less than 0 or greater than 180")
        