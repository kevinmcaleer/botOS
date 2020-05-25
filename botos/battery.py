# Battery Monitor
# botOS
# Kevin McAleer May 2020

from .machine import ADC

class Battery():
    """
    Battery model, used to read in the current battery level
    """
    def __init__(self, bat_pin=None):
        if bat_pin is None:
            bat_pin = 0
        self.pin = bat_pin
        
        # set default voltate
        self.voltage = 5.0 

        # create ADC object on ADC pin
        self.adc = ADC(self.pin)  

                    
    def take_reading(self):
        # read value, 0-1024 
         
        reading = self.adc.read()
        self.voltage = (reading * 5.0) / 1024.0

        return reading

    def level(self):
        analogue = self.take_reading()
        voltage = (analogue * 5.0) / 1024.0

        print(voltage," volts")
        # (analogValue * 5.0) / 1024.0;
        return self.voltage

    def fake_low(self):
        return 4.1