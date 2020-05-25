import unittest
import botos
from botos.led import LED

class TestLED(unittest.TestCase):

    def test_led_create(self):
        print("testing LED Creation on pin 15")
        l = LED()
        result = l.pin
        self.assertTrue(result == 15)

    def test_on(self):
        print("testing on state")
        l = LED()
        l.set_brightness(99)
        self.assertTrue(l.is_on())

    def test_off(self):
        print("testing off state")
        l = LED()
        l.set_brightness(0)
        self.assertTrue(l.is_off())

    def test_brightness(self):
        print("testing brightness level")
        l = LED()
        l.set_brightness(99)
        print(l.level)
        self.assertEqual(l.level(), 990)

if __name__ == '__main__':
    unittest.main()