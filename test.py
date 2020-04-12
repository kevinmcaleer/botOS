# test.py

from botos import Bot
from servo import Servo
from object_view import object_view

smars_bot = Bot()

# lets give our robot a name
smars_bot.name = "SMARS Quad"

# lets add a servo controller
smars_bot.add_servo_controller(controller_type="PCA9685")

# lets add some servos to the controller
left_leg = Servo("Left_Leg")
# left_leg.name = "Left_Leg"
smars_bot.add_servo(left_leg)

right_leg = Servo()
right_leg.name = "Right_Leg"
smars_bot.add_servo(right_leg)

# set the angle of the left leg
o = object_view(smars_bot.servos)
print("Angle of Left_Leg is:")
print(o.Left_Leg.angle)

o.Left_Leg.angle = 180
o.Left_Leg.pin = 10

print(o.Left_Leg.angle)
print(o.Left_Leg.pin)
