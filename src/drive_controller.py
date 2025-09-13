

class DriveController:

    def __init__(self, ps4_controller):
        self.controller = ps4_controller

    def get_motor_throttles(self):
        """Return (motor1, motor4) throttle values based on controller state."""
        self.controller.update()

        motor1 = (self.controller.get_L2_axis() + 1)/2
        motor4 = (self.controller.get_R2_axis() + 1)/2
    
        if self.controller.get_L1() > 0:
          motor1 = -1;
       
        if self.controller.get_R1() > 0:
          motor4 = -1;    
       
        # Clamp between -1 and 1
        motor1 = max(min(motor1, 1), -1)
        motor4 = max(min(motor4, 1), -1)

        return motor1, motor4

