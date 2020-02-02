# servo class
# botOS 

class Servo():
    name = "My Servo"

    # set the default angle to 90 degrees
    angle = 90 

    def angle(self, angle: angle):
        if (angle < 180) and (angle > 0):
            self.angle = angle

        
        