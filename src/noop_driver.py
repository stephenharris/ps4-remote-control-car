class NoOpMotorDriver(MotorDriver):
    def set_throttles(self, m1: float, m4: float):
        # Just log instead of driving motors

