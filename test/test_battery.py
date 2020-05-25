# Battery test harness

import botos
from botos.battery import Battery
import unittest

class test_battery(unittest.TestCase):

    bat = Battery(10)

    def test_pin(self):
        print("testing pin assignment")
        t_pin = self.bat.pin
        self.assertTrue(t_pin == 10)

    def test_voltage(self):

        print("voltage is:", self.bat.fake_low())
        self.assertEqual(self.bat.fake_low(), 4.1)

    def test_level(self):
        print("testing level")
        self.assertEqual(self.bat.level(), 5.0)

if __name__ == '__main__':
    unittest.main()