'''
    See Playstation 4 Controller (name: "Wireless Controller") section https://www.pygame.org/docs/ref/joystick.html

'''
import pygame
import curses
import time
import signal
import sys
from ps4_controller import PS4Controller

# Initialize pygame (used to read the joystick)
pygame.init()

ps4 = PS4Controller()


# Used to manage how fast the main loop runs
clock = pygame.time.Clock()

stdscr = curses.initscr()

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

try:

  ps4.connect()

  ###################
  # Main program loop
  ###################
  while True:
    for event in pygame.event.get():
        pass
        
    motor1 = (ps4.get_L2_axis() + 1)/2
    motor4 = (ps4.get_R2_axis() + 1)/2
    
    if ps4.get_L1() > 0:
       motor1 = -1;
       
    if ps4.get_R1() > 0:
       motor4 = -1;
     
    stdscr.erase()
    stdscr.addstr(ps4.get_summary())
    stdscr.addstr(f"\n\nMotors: {motor1:.2f}, {motor4:.2f}")
    stdscr.refresh()
    
    # Limit to 20 frames per second.
    clock.tick(20)

except KeyboardInterrupt:
    cleanup()

