# botOS
# Kevin McAleer February 2020

import Adafruit_PCA9685
import logging
import servo
from action import Action

# comment out the line below if not using MicroPython
import machine 

class Bot():
    
    '''
    # Bot class

    Models
    '''

    name = "MyBot"
    PWM = ""
    pinouts = {}


    # a collection of servos
    servos = {}

    # a collection of actions
    actions = {}

    def add_servo_controller(self, controller_type):
        if controller_type == "PCA9685":

            # Initialise the PCA9685 using the default address (0x40).
            try:
                self.PWM = Adafruit_PCA9685.PCA9685()
            except OSError as error:
                LOG_STRING = "failed to initialise the servo driver (Adafruit PCA9685): "
                logging.error(LOG_STRING)

                # tell later parts of the code not to actually use the driver
                do_no_use_PCA_driver = True

                PWM = ""
            except:
                print("There was an error loading the adafruit driver; loading without PCA9685.")
                do_no_use_PCA_driver = True # tell later parts of the code not to actually use the driver
            else:
                LOG_STRING = "PCA9685 Driver loaded)."
                do_no_use_PCA_driver = False # tell later parts of the code to use the driver
                logging.error(LOG_STRING)
    
    def add_servo(self, servo: servo):
        """
        Add Servos and register the pin connections
        """
        self.servos[servo.name] = servo
        self.pinouts[servo.pin] = servo.name
       
    def show_pinouts(self):
        '''
        Lists the currently registered pinouts to the console
        '''
        print()
        print('Pin | Connection')
        print('-----------------')
        for keys, values in self.pinouts.items():
            print (" ", keys, "|", values)
        print()
