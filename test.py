# test.py

from botos import Bot
from servo import Servo

smars_bot = Bot()

# lets give our robot a name
smars_bot.name = "SMARS Quad"

# lets add a servo controller
smars_bot.add_servo_controller(controller_type= "PCA9685")

# lets add some servos to the controller
left_leg = Servo()
left_leg.name = "Left Leg"
smars_bot.add_servo(left_leg)

right_leg = Servo()
right_leg.name = "Right Leg"
smars_bot.add_servo(right_leg)

print(len(smars_bot.servos))

# set the angle of the left leg

smars_bot.servos.index(val) if val.name == "Left Leg" else print("not found")

# .set_angle(50)