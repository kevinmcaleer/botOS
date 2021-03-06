import unittest
import botos
from botos.servo import Servo

class TestServo(unittest.TestCase):

    def test_servo_create(self):
        s = Servo()
        result = s.pin
        self.assertTrue(result == 1)

    def test_set_angle(self):
        print('** test_set_angle **')
        s = Servo()
        a = s.angle
        print('before angle:', a)
        s.set_angle(100)
        b = s.angle
        print('after angle:', b)
        result = (b == a)
        self.assertFalse(result == True)

if __name__ == '__main__':
    unittest.main()