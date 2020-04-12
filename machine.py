# machine stubb

class Pin():

    def __init__(self, value):
        print ('created Pin', value)

class PWM():

    pfreq = 50
    pduty = 77
    def __init__(self, value):
        print('created PWM with value ', value)

    def freq(self, value):
        print('frequency')
        self.pfreq = value 
        return value 

    def duty(self, value):
        print('duty')
        self.pduty = value 
        return value 