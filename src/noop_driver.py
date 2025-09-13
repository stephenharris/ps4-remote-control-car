from motor_driver import MotorDriver

class NoOpMotorDriver(MotorDriver):
    def set_throttles(self, m1: float, m4: float):
       pass

