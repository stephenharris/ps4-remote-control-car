'''
    See Playstation 4 Controller (name: "Wireless Controller") section https://www.pygame.org/docs/ref/joystick.html

'''
import pygame
import curses
import time
import signal
#from gusbots import joystick
#import RPi.GPIO as GPIO
#import subprocess

tmp_file = open("/var/log/robot.log", "a")
tmp_file.write('================= init ================')

# Off button
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(3, GPIO.FALLING)
#subprocess.call(['shutdown', '-h', 'now'], shell=False)


# Initialize pygame (used to read the joystick)
pygame.init()

# Used to manage how fast the main loop runs
clock = pygame.time.Clock()

stdscr = curses.initscr()

def cleanup (signumber, stackframe):
    # TODO flash quickly
    tmp_file.close()
    stdscr.erase()
    stdscr.refresh()
    pygame.quit()

signal.signal(signal.SIGABRT, cleanup)
signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGQUIT, cleanup)


axisNames = [
    "Left analog (left/right)", 
    "Left analog (up/down)", 
    "Right analog (left/right)", 
    "L2", 
    "R2", 
    "Right analog (up/down)"
]
buttonNames = ["Square", "Cross", "Circle", "Triangle", "L1", "R1", "L2", "R2","share", "options","l-stick", "r-stick",  "ps4", "pad"]
leftRight = ["Left", "", "Right"]
downUp = ["Down", "", "Up"]

# Main program loop
###################
try:
    while pygame.joystick.get_count() == 0:
        # TODO flash slowly
        pygame.joystick.quit()
        pygame.init()
        print("Waiting for joy stick connection...")
        tmp_file.write('Waiting for joy stick connection...')

        print(pygame.joystick.get_count())
        time.sleep(10)

    joy = pygame.joystick.Joystick(0)
    joy.init()
    axes = joy.get_numaxes()
    buttons = joy.get_numbuttons()
    # TODO solid
    while True:
        for event in pygame.event.get(): # User did something.
                pass

        str = ""
        for i in range(min(buttons, len(buttonNames))):
            button = joy.get_button(i)
            str = str + "\t" + "%s (%s) = %s\n" % (buttonNames[i], i, button)
            if i == 0 and int(button) == 1:
                tmp_file.write('square button pressed!')

        for i in range(joy.get_numhats()):
            hat = joy.get_hat(i)
            leftRightValue = leftRight[hat[0]+ 1]
            downUpValue = downUp[hat[1] + 1]
            str = str + "\t" + "Left/Right = %s \n\tUp/Down = %s\n" % (leftRightValue, downUpValue)

        for i in range(min(axes, len(axisNames))):
            axis = joy.get_axis(i)
            str = str + "\t" + "%s (%s)= %s\n" % (axisNames[i], i, axis)

        stdscr.erase()
        stdscr.addstr(str)
        stdscr.refresh()
    
        # Limit to 20 frames per second.
        clock.tick(20)

except KeyboardInterrupt:
    # Press Ctrl+C to exit the application
    pass

cleanup()

