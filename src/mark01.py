import pygame
import curses
import signal
import time
import sys
import os
from ps4_controller import PS4Controller
from drive_controller import DriveController
from noop_driver import NoOpMotorDriver
from motorkit_driver import RealMotorDriver

def get_motor_driver():
    if os.getenv("USE_NOOP_MOTORS", "0") == "1":
        return NoOpMotorDriver()
    else:
        return RealMotorDriver()
        
# Clean-up
def cleanup(signum=None, frame=None):
    stdscr.erase()
    stdscr.refresh()
    try:
        curses.endwin()  # restore terminal
    except:
        pass
    
    pygame.quit()
    sys.exit(0)

signal.signal(signal.SIGABRT, cleanup)
signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGQUIT, cleanup)


motorDriver = get_motor_driver()
ps4 = PS4Controller()
drive_controller = DriveController(ps4)
clock = pygame.time.Clock()
stdscr = curses.initscr()


try:

  motorDriver.set_throttles(None, None);

  ps4.connect()

  ###################
  # Main program loop
  ###################
  while True:
    for event in pygame.event.get():
        pass
        
    motor1, motor4 = drive.get_motor_throttles()
    motorDriver.set_throttles(motor1, motor4);

    stdscr.erase()
    stdscr.addstr(ps4.get_summary())
    stdscr.addstr(f"\n\nMotors: {motor1:.2f}, {motor4:.2f}")
    stdscr.refresh()
    
    # Limit to 20 frames per second.
    clock.tick(20)

except KeyboardInterrupt:
    cleanup()

