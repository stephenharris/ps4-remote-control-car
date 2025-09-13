import pygame
import time

class PS4Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        self.axis_map = {
            "left_x": 0,
            "left_y": 1,
            "right_x": 2,
            "L2_axis": 3,   # analog trigger
            "R2_axis": 4,   # analog trigger
            "right_y": 5,
        }
        self.button_map = {
            "square": 0,
            "cross": 1,
            "circle": 2,
            "triangle": 3,
            "L1": 4,
            "R1": 5,
            "L2": 6,   # button click
            "R2": 7,   # button click
            "share": 8,
            "options": 9,
            "l_stick": 10,
            "r_stick": 11,
            "ps4": 12,
            "pad": 13,
        }
        self.hat_map = {"dpad": 0}

        self.joy = None
        self.connect()
        
        self.R2NeverPressed = True
        self.L2NeverPressed = True

    def connect(self):
        while True:
            if pygame.joystick.get_count() > 0:
                self.joy = pygame.joystick.Joystick(0)
                self.joy.init()
                print("Controller connected:", self.joy.get_name())
                break
            else:
                print("Waiting for controller...")
                time.sleep(1)

    def update(self):
        pygame.event.pump()

    # Generic accessors
    def _get_button(self, name):
        idx = self.button_map[name]
        return self.joy.get_button(idx)

    def _get_axis(self, name, deadzone=0.1):
        idx = self.axis_map[name]
        val = self.joy.get_axis(idx)
        return 0 if abs(val) < deadzone else val

    def get_dpad(self):
        return self.joy.get_hat(self.hat_map["dpad"])

    # Convenience button methods
    def get_cross(self): return self._get_button("cross")
    def get_square(self): return self._get_button("square")
    def get_circle(self): return self._get_button("circle")
    def get_triangle(self): return self._get_button("triangle")

    def get_L1(self): return self._get_button("L1")
    def get_R1(self): return self._get_button("R1")
    def get_L2_button(self): return self._get_button("L2")  # digital click
    def get_R2_button(self): return self._get_button("R2")  # digital click

    # Triggers (analog axes)
    def get_L2_axis(self): 
    
        axis = self._get_axis("L2_axis");
    
        # When never pressed L2 has a value of 0. After the first use, when released,
        # L2 has a value of -1. When full pressed it has a value of 1.
        if axis == 0 and self.L2NeverPressed:
           return -1;
        
        self.L2NeverPressed = False
        return axis
    
    
    def get_R2_axis(self): 
        # When never pressed R2 has a value of 0. After the first use, when released,
        # R2 has a value of -1. When full pressed it has a value of 1.
        axis = self._get_axis("R2_axis");
        
        if axis == 0 and self.R2NeverPressed:
           return -1;
        
        self.R2NeverPressed = False
        return axis

    # Sticks
    def get_left_stick(self):
        return (self._get_axis("left_x"), self._get_axis("left_y"))

    def get_right_stick(self):
        return (self._get_axis("right_x"), self._get_axis("right_y"))


    def get_summary(self):
        pygame.event.pump()  # update state

        summary = []

        # Buttons
        for name in ["square", "cross", "circle", "triangle",
                     "L1", "R1", "L2", "R2",
                     "share", "options", "l_stick", "r_stick",
                     "ps4", "pad"]:
            summary.append(f"{name}: {self._get_button(name)}")

        # Triggers & sticks
        lx, ly = self.get_left_stick()
        rx, ry = self.get_right_stick()
        summary.append(f"L-stick: ({lx:.2f}, {ly:.2f})")
        summary.append(f"R-stick: ({rx:.2f}, {ry:.2f})")
        summary.append(f"L2: {self.get_L2_axis():.2f}")
        summary.append(f"R2: {self.get_R2_axis():.2f}")

        # D-pad
        #hat = self.get_hat()
        #summary.append(f"D-pad: {hat}")

        return ("\n".join(summary))
  
