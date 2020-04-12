# otto example

from botos import Bot
from servo import Servo
from action import Action

otto = Bot()

# add Ottos feet

left_foot = Servo(name="left_foot", pin = 1)
right_foot = Servo("right_foot", pin = 2)

otto.add_servo(left_foot)
otto.add_servo(right_foot)

# add Ottos legs

left_leg = Servo("left_leg", pin = 3)
right_leg = Servo("right_leg", pin = 4)

otto.add_servo(left_leg)
otto.add_servo(right_leg)

otto.show_pinouts()

walk = Action()
walk.add_step('set servo:left_leg angle=90')
walk.add_step('set servo:left_foot angle=10')
otto.actions.show()

# add rangefinder

