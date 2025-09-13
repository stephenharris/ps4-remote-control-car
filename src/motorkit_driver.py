from adafruit_motorkit import MotorKit
from motor_driver import MotorDriver

class RealMotorDriver(MotorDriver):
    def __init__(self):
        self.kit = MotorKit()

    def set_throttles(self, m1: float, m4: float):
        self.kit.motor1.throttle = m1
        self.kit.motor4.throttle = m4

