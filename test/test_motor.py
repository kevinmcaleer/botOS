# Kevin McAleer May 2020

import botos
from botos.motor import Motor
from botos.machine import Pin
from time import sleep
import unittest

m = Motor(0,1000)

m.on()
sleep(0.5)
m.off()

pins =  [0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16]

def test_pins():
    for n in pins:
        p = Pin(n, Pin.OUT, value=1)
        print('n is ',n)
        sleep(1)

def do_test():
    for n in pins:
        p = Pin(n, Pin.OUT)
        sleep(1)
        print('P:', n ,'setting value to 1')
        p.value(1)
        sleep(1)
        print('P:',n,'setting value to 0')
        p.value(0)
    
def go():
    m1 = Motor(4, 1000)
    m2 = Motor(5, 1000)

    m1.forward()
    m2.forward()
    m1.backwards()
    m2.backwards()
    sleep(1)
    
class test_motor(unittest.TestCase):

    def test_pins_assignment(self):
        pin = 4
        speed = 40
        p1 = Motor(pin, speed)   
        self.assertEqual(p1.motor_pin, pin)
        self.assertEqual(p1.motor_speed, speed) 

if __name__ == '__main__':
    do_test()
    unittest.main()
    
